from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.

def home(request):
    print(request.user)
    lib_obj = Library.objects.all()
    # print(lib_obj)
    return render(request,"home.html",context={"lib":lib_obj})

def create_library(request):
    if request.method == "POST":
        print(request.POST)
        # print("in post method")
        lname = request.POST.get("LibraryName")   #data request.POST se lena hai
        lprice = request.POST.get("Libraryprice")
        lis_active = request.POST.get("Libraryis_published")
        if lis_active == "yes":
            lis_active = True
        else:
            lis_active = False    
        print(lname,lprice,lis_active)
        # return HttpResponse("post request")
        Library.objects.create(lname = lname,lprice = lprice,lis_published =lis_active)
        return redirect("show-library")
    elif request.method == "GET":
        return render(request,"show_library.html")    