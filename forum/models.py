from django.db import models
# Create your models here.


# Create your models here.

class Message_forum(models.Model):
    title = models.CharField(max_length=500, null=True)
    content = models.CharField(max_length=800, null=True)
    author = models.CharField(max_length=800, null=True)
    def __str__(self):
        return self.title + " " + self.content + " " + self.author