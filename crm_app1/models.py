from django.db import models

# Create your models here.





class CustomerRecord(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=120)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"