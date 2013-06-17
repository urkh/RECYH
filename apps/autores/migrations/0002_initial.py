# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Autores'
        db.create_table('autores', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fechaNac', self.gf('django.db.models.fields.DateField')()),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('fechaReg', self.gf('django.db.models.fields.DateField')()),
            ('informacion', self.gf('django.db.models.fields.TextField')()),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')()),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'autores', ['Autores'])


    def backwards(self, orm):
        # Deleting model 'Autores'
        db.delete_table('autores')


    models = {
        u'autores.autores': {
            'Meta': {'object_name': 'Autores', 'db_table': "'autores'"},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fechaNac': ('django.db.models.fields.DateField', [], {}),
            'fechaReg': ('django.db.models.fields.DateField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informacion': ('django.db.models.fields.TextField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'telefono': ('django.db.models.fields.IntegerField', [], {}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['autores']