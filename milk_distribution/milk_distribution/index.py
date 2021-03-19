from django.shortcuts import render
from django.shortcuts import redirect
def homepage(request):
    return render(request,'index.html')
def customer(request):
    return render(request,'customer.html')
def customer1(request):
    return render(request,'customer1.html')
def Billing(request):
    return render(request,'Billing.html')
def newuser(request):
    return render(request,'newuser.html')
def contact(request):
    return render(request,'contact.html')
def delivery(request):
    return render(request,'delivery.html')
def delivery_login(request):
    return render(request,'delivery_login.html')