# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        orm.Type.objects.create(code="file.video")
        orm.Type.objects.create(code="file.image")
        orm.Type.objects.create(code="file.music")
        orm.Type.objects.create(code="file.text")
        orm.Type.objects.create(code="file.unknown")
        appconfig_type = orm.Type.objects.create(code="config.app")
        orm.Type.objects.create(code="config.rename")
        orm.Type.objects.create(code="config.convert")

        orm.Configuration.objects.create(key="folder.tmp", value="/tmp", \
                                         type=appconfig_type)

        orm.Status.objects.create(code="pending")
        orm.Status.objects.create(code="convert")
        orm.Status.objects.create(code="rename")
        orm.Status.objects.create(code="move")
        orm.Status.objects.create(code="failed")

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'sorter.action': {
            'Meta': {'object_name': 'Action'},
            'acknowledged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'command': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'completion': ('django.db.models.fields.IntegerField', [], {}),
            'date_completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_started': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'failed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediafile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sorter.MediaFile']"})
        },
        u'sorter.configuration': {
            'Meta': {'object_name': 'Configuration'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sorter.Type']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sorter.mediafile': {
            'Meta': {'object_name': 'MediaFile'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'filepath': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sorter.Status']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sorter.Type']"})
        },
        u'sorter.mediafolder': {
            'Meta': {'object_name': 'MediaFolder'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sorter.MediaFolder']", 'null': 'True'})
        },
        u'sorter.status': {
            'Meta': {'object_name': 'Status'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'sorter.type': {
            'Meta': {'object_name': 'Type'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['sorter']
    symmetrical = True
