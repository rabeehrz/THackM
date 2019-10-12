from django.db import models

from users.models import User
class Case(models.Model):
    lawyer = models.ForeignKey(User, on_delete=models.CASCADE)
    ipc_code = models.IntegerField()
    count = models.IntegerField(default = 0)
    status = models.IntegerField(default=0)
