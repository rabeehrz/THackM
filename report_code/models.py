from django.db import models

from reports.models import Report

class ReportCode(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    ipc_code = models.IntegerField()
