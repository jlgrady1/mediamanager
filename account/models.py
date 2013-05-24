from django.db import models

class Account(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)

class Role(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    code = models.CharField(max_length=50)
    parent = models.ForeignKey(Role)
