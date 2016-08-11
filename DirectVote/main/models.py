from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ValidUser(models.Model):
    user = models.OneToOneField(User)
    idcard = models.BigIntegerField(primary_key=True)
    
    class Meta:
        unique_together = ('user', 'idcard',)
    
