from django.db import models

class User(models.Model):
    name    = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.IntegerField(null = True)
    user_type = models.IntegerField(default=0) # 0: User #1: Lawyer

