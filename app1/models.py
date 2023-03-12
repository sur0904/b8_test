from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=230,null=True)
    qty = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    is_published = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)  #soft dlt kai liye chaiye

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.name   
