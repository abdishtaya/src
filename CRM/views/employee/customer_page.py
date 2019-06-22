from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db import connection
from src.CRM.models import customers
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def Customers_page(request):
 if request.session.has_key("username") == False :
     return redirect("/")

 cursor = connection.cursor()
 if request.method == 'POST':
      result_set=""
      username=request.POST.get('required')
      email=request.POST.get('email')
      password=request.POST.get('pwd')
      confirmpassword=request.POST.get('pwd2')
      print(username)
      print(password)

      if not email or not username or not password  or not confirmpassword or password != confirmpassword or len(username)>40 or len(password)>50 or len(email)>40:
           print("empty")
           context={
               "error":"error in data"
           }
           return render(request, "employees/extendforemployee/Customers.html",context)
      else :
           found=customers.objects.filter(email=email).all()
           if  found:
                result_sets=customers.objects.filter(active="1")
                result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
                print("full")
                context={
                    "error":"duplicate email",
                    'data':result_set
                   }
                return render(request, "employees/extendforemployee/Customers.html",context)

           customer=customers(email=email,username=username, password=password,active="1")
           customer.save()
           result_sets=customers.objects.filter(active="1")
           result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
           print("full")
           context={
               "success":"yes ,success",
               'data':result_set
           }
           return render(request, "employees/extendforemployee/Customers.html",context)

 else :
     result_sets=customers.objects.filter(active="1")
     result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
     return render(request,"employees/extendforemployee/Customers.html",{'data': result_set} )

def update_customers(request):
 if request.session.has_key("username") == False :
     return redirect("/")

 if request.method == 'POST':
      result_set=""
      id=request.POST.get('id')
      username=request.POST.get('required1')
      email=request.POST.get('email1')
      password=request.POST.get('pwd1')
      confirmpassword=request.POST.get('pwd21')
      print(username)
      print(password)
      print(id)
      if not email or  not username or not password  or not confirmpassword or password != confirmpassword or len(username)>40 or len(password)>50 or len(email)>40:
           print("empty")
           context={
               "error":"error in data"
           }
           return render(request, "employees/extendforemployee/Customers.html",context)
      else :
           found=customers.objects.filter(email=email).exclude(id=id).all()
           if  found:
                result_sets=customers.objects.filter(active="1")
                result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
                print("full")
                context={
                    "error":"duplicate email",
                    'data':result_set
                   }
                return render(request, "employees/extendforemployee/Customers.html",context)
           try:
            customers.objects.filter(id=id).update(email=email,username=username, password=password)
           except:
            return redirect("/home/Customers" )
           result_sets=customers.objects.filter(active="1")
           result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
           print("full")
           context={
               "success":"yes ,success",
               "data":result_set
           }
           return render(request, "employees/extendforemployee/Customers.html",context)

 else :
     result_sets=customers.objects.filter(active="1")
     result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
     return render(request,"employees/extendforemployee/Customers.html",{'data': result_set} )


def search_customers(request):
 if request.session.has_key("username") == False :
     return redirect("/")
 cursor = connection.cursor()

 if request.method == 'GET':
      print("yesssss")
      result_set=""
      name=request.GET.get('searchcustomer')


      result_set=customers.objects.filter(username__icontains=name , active="1")
      # result_set = Paginator(result_sets,1).get_page(request.GET.get('page'))
      return render(request,"employees/extendforemployee/Customers.html",{'data': result_set} )
 else :
     result_set=customers.objects.filter(active="1")
     return render(request,"employees/extendforemployee/Customers.html",{'data': result_set} )


def delete_customer(request):
    if request.session.has_key("username") == False :
     return redirect("/")
    cursor = connection.cursor()
    if request.is_ajax():


     customers.objects.filter(id=request.GET.get('id')).update(active="0")

     return redirect("/home/Customers" )
    else :
     return redirect("/home/Customers" )


def get_customer(request):
    if request.session.has_key("username") == False :
     return redirect("/")
    cursor = connection.cursor()
    if request.is_ajax():


         try:
              result_set=customers.objects.get(id=request.GET.get('id'))

              return HttpResponse(result_set.email+":::::::"+result_set.username)
         except ObjectDoesNotExist:
              return redirect("/home/Customers" )



    else :
     return redirect("/home/Customers" )
