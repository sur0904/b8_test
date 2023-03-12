"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-single-book/<int:id>/',views.get_single_book),
    path('get-all-book/',views.get_all_books),
    path('show-active-books/',views.show_active_books,name="show-active-books"),
    path('show-inactive-books/',views.show_inactive_books,name="show-inactive-books"),
    path('home/',views.home,name="home"),
    path('update/<int:pk>/',views.update_book,name="update-book"),
    path('hard-delete/<int:pk>/',views.hard_delete_book,name="hard-delete-book"),
    path('soft-delete/<int:pk>/',views.soft_delete_book,name="soft-delete-book"),
    
    
]