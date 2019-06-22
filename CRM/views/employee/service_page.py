from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db import connection
from src.CRM.models import services,customers
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Services_page(request):
 if request.session.has_key("username") == False :
     return redirect("/")
 cursor = connection.cursor()
 if request.method == 'POST':
      result_set=""
      nameofservice=request.POST.get('nameofservice')
      emailcustomer=request.POST.get('emailcustomer')


      if  not nameofservice or not emailcustomer  or len(nameofservice)>40 or len(emailcustomer)>50:
           print("empty")
           context={
               "error":"error in data"
           }
           return render(request, "employees/extendforemployee/Services.html",context)
      else :


           nameemp=request.session['username']
           active="1"
           try:
               idcustomer=customers.objects.get(email=emailcustomer)
               service=services(email_employees=nameemp, email_customers=idcustomer.email,name_service=nameofservice, active=active
                            )
               service.save()
           except:
              result_sets=services.objects.all()
              result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
              context={
                  "data":result_set,
                  "error":"email not found"
                 }
              return render(request, "employees/extendforemployee/Services.html",context)


           result_sets=services.objects.all()
           result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
           context={
               "success":"yes ,success",
               "data":result_set
            }

           return render(request, "employees/extendforemployee/Services.html",context)

 else :

     result_sets =services.objects.all()
     result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
     # # result_set = Paginator.page(1)
     # for item in result_set:
     #
     #   print(item.name_service)

     return render(request,"employees/extendforemployee/Services.html",{'data': result_set} )

def update_service(request):
 if request.session.has_key("username") == False :
     return redirect("/")
 cursor = connection.cursor()
 if request.method == 'POST':
      result_set=""
      id=request.POST.get('id')
      nameofservice=request.POST.get('nameofservice1')
      emailcustomer=request.POST.get('emailcustomer1')


      if  not nameofservice or not emailcustomer  or len(nameofservice)>40 or len(emailcustomer)>50:
          print("empty")
          print(nameofservice)
          print(emailcustomer)
          context={
               "error":"error in data"
           }
          return render(request, "employees/extendforemployee/Services.html",context)
      else :


           result_sets=services.objects.all()
           result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
           print("full")
           try:
               idcustomer=customers.objects.get(email=emailcustomer)
           except:
              context={
                  "data":result_set,
                  "error":"email not found"
                 }
              return render(request, "employees/extendforemployee/Services.html",context)


           try:
            services.objects.filter(id=id).update(email_employees=request.session['username'], email_customers=idcustomer.email,
             name_service=nameofservice, active="1")
           except:
            return redirect("/home/Services" )
           context={
               "success":"yes ,success",
               "data":result_set
           }
           return render(request, "employees/extendforemployee/Services.html",context)

 else :
     result_sets=services.objects.all()
     result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
     return render(request,"employees/extendforemployee/Services.html",{'data': result_set} )


def search_service(request):
 if request.session.has_key("username") == False :
     return redirect("/")
 cursor = connection.cursor()

 if request.method == 'GET':
      print("yesssss")
      result_set=""
      name=request.GET.get('searchservice')
      print(name)


      result_set=services.objects.filter(email_customers__icontains=name)

      # result_set = Paginator(result_sets,1).get_page(request.GET.get('page'))
      return render(request,"employees/extendforemployee/Services.html",{'data': result_set} )
 else :
     result_sets=services.objects.all()
     result_set = Paginator(result_sets,10).get_page(request.GET.get('page'))
     return render(request,"employees/extendforemployee/Services.html",{'data': result_set} )


def stop_service(request):
    if request.session.has_key("username") == False :
     return redirect("/")
    cursor = connection.cursor()
    if request.is_ajax():


     services.objects.filter(id=request.GET.get('id')).update( active="0")
     return redirect("/home/Services" )
    else :
     return redirect("/home/Services" )


def get_service(request):
    if request.session.has_key("username") == False :
     return redirect("/")


    if request.is_ajax():

     try:
          result_set=services.objects.get(id=request.GET.get('id'))

          return HttpResponse(result_set.name_service+":::::::"+result_set.email_customers)
     except ObjectDoesNotExist:
         return redirect("/home/Services" )




    else :
     return redirect("/home/Services" )


def active_service(request):
    if request.session.has_key("username") == False :
     return redirect("/")
    cursor = connection.cursor()
    if request.is_ajax():


     services.objects.filter(id=request.GET.get('id')).update( active="1")
     return redirect("/home/Services" )
    else :
     return redirect("/home/Services" )



