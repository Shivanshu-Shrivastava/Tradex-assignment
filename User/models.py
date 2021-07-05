from django.db import models

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password=models.CharField(max_length=10)
    username=models.CharField(max_length=25)
    def __str__(self):
        return self.first_name

class post(models.Model):
    user=models.CharField(max_length=25)
    text=models.CharField(max_length=25)
    created_at=models.DateField()
    updated_at=models.DateField()
    def __str__(self):
        return self.user