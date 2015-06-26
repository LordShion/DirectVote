from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    last_login = models.DateTimeField(auto_now=True)
