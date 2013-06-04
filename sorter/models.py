import os
import validate

from django.utils import timezone
from django.db import models

class Type(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=100)

    def __unicode__(self):
        return self.code

class Status(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=100)

    def __unicode__(self):
        return self.code

class MediaFile(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(Type)
    status = models.ForeignKey(Status)
    filepath = models.CharField(max_length=255, unique=True, \
                                validators=[validate.folder_exists])

    def __unicode__(self):
        return self.filepath

    def get_filename(self):
        return os.path.basename(self.filepath)
    
    def get_extension(self):
        fn = self.get_filename()
        ext = os.path.splitext(fn)[1]
        ext = ext.replace('.','')
        return ext


class Action(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_started = models.DateTimeField(null=True)
    date_completed = models.DateTimeField(null=True)
    mediafile = models.ForeignKey(MediaFile)
    command = models.CharField(max_length=255)
    completion = models.IntegerField()
    description = models.CharField(max_length=255)
    failed = models.BooleanField(default=False)
    acknowledged = models.BooleanField(default=False)

    def __unicode__(self):
        return self.description


class MediaFolder(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    folder = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('self', null=True)

    def __unicode__(self):
        return self.folder

    def get_level(self):
        level = 0
        p = None
        try:
            p = self.parent
        except self.field.rel.to.DoesNotExist:
            #No parent
            pass
        while p is not None:
            level = level + 1
            p = p.parent
        return level


class Configuration(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255)
    type = models.ForeignKey(Type)
    locked = models.BooleanField(default=False)

    def __unicode__(self):
        return self.key
