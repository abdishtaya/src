from django.contrib.auth import authenticate,login
from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.db import connection
from src.CRM.models import employees
from django.core.exceptions import ObjectDoesNotExist
def welcome_page(request):
    found=employees.objects.filter(email="abd@yahoo.com")
    if not found:
         employee=employees(username="abd ishtaya",email="abd@yahoo.com",type="admin", password="123456789")
         employee.save()
         context={
            "email":"email:abd@yahoo.com,,passwd=123456789"
         }
    else:
        context={
            "email":"email:abd@yahoo.com,,passwd=123456789"
        }
    return render(request,"welcome.html",context )



def login_page(request):
  if request.method == 'POST':
      result_set=""
      email_usename=request.POST.get('email_usename')
      password=request.POST.get('password')
      print(email_usename)
      print(password)
      cursor = connection.cursor()
      if  not  password or not email_usename and not "@" in email_usename:
           print("empty")
           context={
               "error":"error in data"
           }
           return render(request, "welcome.html",context)
      else :
           if not "@" in email_usename:

             return redirect("/")
           else:
             try:
                 result_set=employees.objects.get(email=email_usename , password=password)
             except ObjectDoesNotExist:
                 return redirect("/home/Customers" )
           print(email_usename)
           print(password)

           if not result_set:
                print("empty")
                context={
                    "error":"not found"
                      }
                return render(request, "welcome.html",context)
           else:

               request.session['username']=result_set.email

               return redirect("/home/Customers")



  else :
      return render(request,"welcome.html")


def logout(request):
    request.session.flush()
    return redirect("/")
