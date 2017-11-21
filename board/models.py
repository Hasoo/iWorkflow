from django.db import models

class Workflow(models.Model):
    seq = models.AutoField(primary_key=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    attach = models.TextField(blank=True)
    secret_key = models.CharField(max_length=16, blank=True)