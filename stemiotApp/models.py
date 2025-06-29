from django.db import models

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=50)
    client_phone = models.IntegerField()
    client_message = models.TextField()

    def __str__(self):
        return self.client_name

