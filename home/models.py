from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 300)
    subject =models.TextField()
    email = models.CharField(max_length = 200,blank = True)
    message = models.TextField()

    def __str__(self):
        return self.name