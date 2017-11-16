from django.db import models

class LoginAdmin(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_pass = models.CharField(max_length=64)
    user_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'iw_admin'