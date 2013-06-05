# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Type'
        db.create_table(u'sorter_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sorter', ['Type'])

        # Adding model 'Status'
        db.create_table(u'sorter_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sorter', ['Status'])

        # Adding model 'MediaFile'
        db.create_table(u'sorter_mediafile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sorter.Type'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sorter.Status'])),
            ('filepath', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'sorter', ['MediaFile'])

        # Adding model 'Action'
        db.create_table(u'sorter_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_started', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('date_completed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('mediafile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sorter.MediaFile'])),
            ('command', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('completion', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('failed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('acknowledged', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sorter', ['Action'])

        # Adding model 'MediaFolder'
        db.create_table(u'sorter_mediafolder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('folder', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sorter.MediaFolder'], null=True)),
        ))
        db.send_create_signal(u'sorter', ['MediaFolder'])

        # Adding model 'Configuration'
        db.create_table(u'sorter_configuration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sorter.Type'])),
            ('locked', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sorter', ['Configuration'])


    def backwards(self, orm):
        # Deleting model 'Type'
        db.delete_table(u'sorter_type')

        # Deleting model 'Status'
        db.delete_table(u'sorter_status')

        # Deleting model 'MediaFile'
        db.delete_table(u'sorter_mediafile')

        # Deleting model 'Action'
        db.delete_table(u'sorter_action')

        # Deleting model 'MediaFolder'
        db.delete_table(u'sorter_mediafolder')

        # Deleting model 'Configuration'
        db.delete_table(u'sorter_configuration')


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