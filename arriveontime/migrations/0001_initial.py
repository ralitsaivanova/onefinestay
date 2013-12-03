# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'arriveontime_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'arriveontime', ['City'])

        # Adding model 'Airport'
        db.create_table(u'arriveontime_airport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['arriveontime.City'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'arriveontime', ['Airport'])

        # Adding model 'Booking'
        db.create_table(u'arriveontime_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date_from', self.gf('django.db.models.fields.DateTimeField')()),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['arriveontime.City'])),
            ('flight_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'arriveontime', ['Booking'])

        # Adding M2M table for field user on 'Booking'
        m2m_table_name = db.shorten_name(u'arriveontime_booking_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('booking', models.ForeignKey(orm[u'arriveontime.booking'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['booking_id', 'user_id'])

        # Adding model 'Staff'
        db.create_table(u'arriveontime_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['arriveontime.City'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='staff', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'arriveontime', ['Staff'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'arriveontime_city')

        # Deleting model 'Airport'
        db.delete_table(u'arriveontime_airport')

        # Deleting model 'Booking'
        db.delete_table(u'arriveontime_booking')

        # Removing M2M table for field user on 'Booking'
        db.delete_table(db.shorten_name(u'arriveontime_booking_user'))

        # Deleting model 'Staff'
        db.delete_table(u'arriveontime_staff')


    models = {
        u'arriveontime.airport': {
            'Meta': {'object_name': 'Airport'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['arriveontime.City']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'arriveontime.booking': {
            'Meta': {'object_name': 'Booking'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['arriveontime.City']"}),
            'date_from': ('django.db.models.fields.DateTimeField', [], {}),
            'flight_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'})
        },
        u'arriveontime.city': {
            'Meta': {'ordering': "['country']", 'object_name': 'City'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'arriveontime.staff': {
            'Meta': {'object_name': 'Staff'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['arriveontime.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'staff'", 'to': u"orm['auth.User']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['arriveontime']