from django.shortcuts import render

# Create your views here.
def form(request):
    if request.method == 'POST':
       first= request.POST.get("first_name")
       post= request.POST.get("post")
       context={
           'first':first,
           'post':post
       }
       return render(request, 'User/form.html',context)
    return render(request,'User/form.html')