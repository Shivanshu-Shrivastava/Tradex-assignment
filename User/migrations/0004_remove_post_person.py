# Generated by Django 3.2.5 on 2021-07-05 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_post_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='person',
        ),
    ]