from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=350)
    