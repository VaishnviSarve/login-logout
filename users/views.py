from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .form import UserRegistertionForm


# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegistertionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created. Yon can log in now!')
            return redirect('login')
    else:
        form=UserRegistertionForm()
    context={'form':form}
    return render (request,'users/register.html',context)


