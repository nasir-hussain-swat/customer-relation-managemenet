from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def home(request):
    #check to see if logging in
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have been logged in successfully")
            return redirect('home')
        else:
            messages.success(request,'there was an error plz try again')
            return redirect('home')

    else:
        return render(request,'home.html',{})





def logout_user(request):
    logout(request)
    messages.success(request,'you have logout')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            #authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']

            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Registered ')
            return redirect('home')
        
    else:
        
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})