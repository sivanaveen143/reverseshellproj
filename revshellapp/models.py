from django.db import models

# Create your models here.
class commands(models.Model):
    cmd = models.CharField(max_length=50)

class text(models.Model):
    text = models.TextField(max_length=500)