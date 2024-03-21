from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignupForm,CustomerRecordForm
from .models import CustomerRecord




def customer_delete(request,pk):
    customer=CustomerRecord.objects.get(pk=pk)
    customer.delete()
    messages.success(request,"Customer Deleted Successfully")
    return redirect("list-customer")

def update_view(request,pk):
    form_instance = CustomerRecord.objects.get(pk=pk)
    if request.method =="POST":
        form = CustomerRecordForm(request.POST,instance=form_instance)
        if form.is_valid():
            form.save()
            messages.success(request,"Customer Updated Successfully")
            return redirect("list-customer")
        else:
            messages.success(request,"Error Please Enter Correct Information")
            return redirect("list-customer")
    else:
        form = CustomerRecordForm(instance=form_instance)
        return render(request,"update.html",{'form':form})


def detail_customer(request,pk):
    customer = CustomerRecord.objects.get(pk=pk)
    return render(request,"detail.html",{"customer":customer})


def list_customer(request):
    form = CustomerRecord.objects.all()
    return render(request,"list_customer.html",{'form':form})


def create_customer(request):
    form=CustomerRecordForm()
    if request.method == 'POST':
        form = CustomerRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Customer Added Successfully")
            return redirect("list-customer")
        else:
            messages.success(request,"Error Please Enter Correct Customer")
            return redirect("list-customer")
    return render(request,"create.html",{'form':form})





def home_page_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged In")
            return redirect("home")
        else:
            messages.success(request,"There was an Error logging In")
            return redirect('home')
    return render(request,"home.html")


def register_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"You have Registered Successfully")
            return redirect('home')
    else:
        form = SignupForm()
        return render(request,"register.html",{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request,"You have Logout Successfully")
    return redirect('home')

