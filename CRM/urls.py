"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views.welcome import welcome_page,login_page,logout
from .views.employee.customer_page import Customers_page,delete_customer,update_customers,search_customers,get_customer
from .views.employee.service_page import Services_page,update_service,search_service,stop_service,get_service,active_service
urlpatterns = [
    path('', welcome_page),
    path('login', login_page),
    path('home/Customers',Customers_page ),
    path('home/editCustomers',update_customers ),
    path('home/searchCustomers',search_customers ),

    path('home/deletescustomers',delete_customer ),
    path('home/getcustom',get_customer ),

    path('home/Services',Services_page ),
    path('home/editservice',update_service ),
    path('home/searchService',search_service ),
    path('home/getService',get_service ),

    path('home/stopService',stop_service ),
    path('home/activeService',active_service ),

    path('home/logout', logout),


]
