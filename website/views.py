from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record




# Create your views here.
def home(request):
    #grab the records
    records=Record.objects.all()
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
        return render(request,'home.html',{'records':records})





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



def customer_record(request,pk):
    if request.user.is_authenticated:

        #look up record

        customer_record=Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    
    else:
        messages.success(request,'you must login to view that page')
        return redirect('home')
    


def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record deleted Successfully")
        return redirect('home')
    else:
        messages.success(request,"you must be logined to delete that")
        return redirect('home')
    
def add_record(request):
    return render(request,'add_record.html',{})

