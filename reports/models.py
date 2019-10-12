from django.db import models

from users.models import User
class Report(models.Model):
    user = models.IntegerField(default=0)
    description = models.TextField()
    lawyer = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
