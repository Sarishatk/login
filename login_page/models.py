from django.db import models

# Create your models here.
class loginMode(models.Model):

    name = models.CharField(max_length=30)

    password = models.IntegerField(null=False)
