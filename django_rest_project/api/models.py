from django.db import models
from django.utils import timezone

# Create your models here.

class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    body = models.TextField()
    image = models.TextField()
    date_updated = models.DateTimeField()
