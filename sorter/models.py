import os

from django.utils import timezone
from django.db import models

class Type(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    code = models.CharField(max_length=100)

    def __unicode__(self):
        return self.code

    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.date_created is None:
            self.date_created = now
        self.date_updated = now
        super(Type, self).save(*args, **kwargs)

class Status(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    code = models.CharField(max_length=100)

    def __unicode__(self):
        return self.code

    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.date_created is None:
            self.date_created = now
        self.date_updated = now
        super(Status, self).save(*args, **kwargs)

class MediaFile(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    type = models.ForeignKey(Type)
    status = models.ForeignKey(Status)
    filepath = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.filepath

    def get_filename(self):
        return os.path.basename(self.filepath)
    
    def get_extension(self):
        fn = self.get_filename()
        ext = os.path.splitext(fn)[1]
        ext = ext.replace('.','')
        return ext

    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.date_created is None:
            self.date_created = now
        self.date_updated = now
        super(MediaFile, self).save(*args, **kwargs)

class Action(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    date_executed = models.DateTimeField(null=True)
    mediafile = models.ForeignKey(MediaFile)
    command = models.CharField(max_length=255)
    completion = models.IntegerField()
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.date_created is None:
            self.date_created = now
        self.date_updated = now
        super(Action, self).save(*args, **kwargs)

class DownloadFolder(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    folder = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('self', null=True)
    level = models.IntegerField()

    def __unicode__(self):
        return self.folder

    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.date_created is None:
            self.date_created = now
        self.date_updated = now
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
        self.level = level
        super(DownloadFolder, self).save(*args, **kwargs)

class Configuration(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    key = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return self.key

    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.date_created is None:
            self.date_created = now
        self.date_updated = now
        super(Configuration, self).save(*args, **kwargs)
