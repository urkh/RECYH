# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categorias'
        db.create_table('categorias', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['areas.Areas'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'categorias', ['Categorias'])


    def backwards(self, orm):
        # Deleting model 'Categorias'
        db.delete_table('categorias')


    models = {
        u'areas.areas': {
            'Meta': {'object_name': 'Areas', 'db_table': "'areas'"},
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'categorias.categorias': {
            'Meta': {'object_name': 'Categorias', 'db_table': "'categorias'"},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['areas.Areas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['categorias']