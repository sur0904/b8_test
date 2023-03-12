from django.shortcuts import render,redirect
from .models import Book
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def get_single_book(request,id):
    book_obj = Book.objects.get(id=1)
    return HttpResponse(book_obj)

def get_all_books(request):
    book_obj = Book.objects.all()
    return HttpResponse(book_obj) 

def show_active_books(request):
    book_obj = Book.objects.filter(is_active=True)
    return render(request,"show_book.html",context={'books':book_obj}) 

@csrf_exempt
def home(request):  #ye create aur update dono kai liye hota hai
    if request.method == "POST":
        print(request.POST) #here data get means backend mai data aa jata hai
        #yaha update aur create dono ka data aayega
        bid = request.POST.get("library_id")
        name = request.POST.get("library_name")  #that name is come from frontend
        qty = request.POST.get("library_qty")
        price = request.POST.get("library_price")
        is_pub = request.POST.get("library_is_published")
        print(name,qty,price,is_pub)
        if is_pub == "Yes":
            is_pub = True  #here sing equal is required
        else:
            is_pub = False
        if not bid:   #ye update kai liye nhi hai  #ye create kai liye hai  
            Book.objects.create(name=name,qty=qty,price=price,is_published=is_pub) #here data created in databse
        #ye update kai liye hai    
        else:
            book_obj = Book.objects.get(id=bid) #ye update kai liye hai
            book_obj.name = name 
            book_obj.qty = qty
            book_obj.price = price
            book_obj.is_published=is_pub 
            book_obj.save()

        return redirect("home")  #here redirect on same page   
    elif request.method == "GET":  #get method aati hai tho simply form display ho jayega
        print(request.GET)
        return render(request,"home.html")
    
def update_book(request,pk):
    book_obj = Book.objects.get(id=pk)
    return render(request,"home.html",context={'single_book':book_obj})

def hard_delete_book(requst,pk):  #delete data 
    book_obj = Book.objects.get(id=pk)
    book_obj.delete()
    return redirect("show-active-books")  

def soft_delete_book(request,pk):  #delete data 
    book_obj = Book.objects.get(id=pk)
    book_obj.delete()
    return redirect("show-active-books") 

def show_inactive_books(request):
    return render(request,"show_book.html",context={"books":Book.objects.filter(is_active=False)})     







    

               

    # return render(request,"home.html")         
