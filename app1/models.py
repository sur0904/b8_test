from django.db import models

# Create your models here.
class Library(models.Model):
    lname = models.CharField(max_length=120)
    lprice = models.IntegerField()
    lcreateddate = models.DateTimeField(auto_now_add=True)
    lis_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.lname}"

    class Meta:
        db_table = "library"

class Employee(models.model):
    name = models.CharField(max_length=120) 
    salary = models.IntegerField()
    hobby = models.CharField(max_length=120)       