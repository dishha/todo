from django.db import models
import datetime

# Create your models here.

class tasks(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    modified_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title
