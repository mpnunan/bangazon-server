from django.db import models

class Cashier(models.Model):

    uid = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    manager = models.BooleanField()
