"""milk_distribution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import index

urlpatterns = [
    path('', index.homepage),
    path('index.html',index.homepage),
	path('customer.html', index.customer),
	path('customer1.html', index.customer1),
	path('Billing.html', index.Billing),
	path('newuser.html', index.newuser),
	path('contact.html', index.contact),
	path('delivery.html', index.delivery),
	path('delivery_login.html', index.delivery_login),
]
