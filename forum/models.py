from django.db import models
# Create your models here.


# Create your models here.

class Message_forum(models.Model):
    title = models.CharField(max_length=500, null=True)
    content = models.CharField(max_length=800, null=True)
    author = models.CharField(max_length=800, null=True)
    date = models.CharField(max_length=100, null=True)
