from django.db import models

# Create your models here.



class User(models.Model):
    name = models.CharField(max_length=255, null = True, blank = True)
    contact = models.CharField(max_length = 255, unique = True)
    address= models.TextField(null=True, blank=True)
    image = models.ImageField(null = True, blank = True)
    message= models.TextField(null=True, blank=True)



    def __str__(self):
            return self.name