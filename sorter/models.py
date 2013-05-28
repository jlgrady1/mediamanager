from django.db import models

class Type(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    code = models.CharField(max_length=100)

class Status(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    code = models.CharField(max_length=100)

class MediaFile(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    type = models.ForeignKey(Type)
    status = models.ForeignKey(Status)
    filename = models.CharField(max_length=255)

class Action(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    mediafile = models.ForeignKey(MediaFile)
    command = models.CharField(max_length=255)

class DownloadFolder(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    folder = models.CharField(max_length=255)
    level = models.IntegerField()

class Configuration(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
