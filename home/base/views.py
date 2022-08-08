from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
# Create your views here.
def home(request):
    users = User.objects.all()
    context={'users':users}
    return render(request,'base/home.html',context)

def userForms(request):
    form=UserForm()
    if request.method=='POST':
        print(request.POST)
        form= UserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context={'form':form}
    
    return render(request,'base/user.html',context)