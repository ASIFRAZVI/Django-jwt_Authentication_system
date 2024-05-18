from django.db import models

class Register_user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, blank=False, null=False) 
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phnumber = models.BigIntegerField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
