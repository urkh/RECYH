# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Publicaciones.lecturas'
        db.alter_column('publicaciones', 'lecturas', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Publicaciones.lecturas'
        db.alter_column('publicaciones', 'lecturas', self.gf('django.db.models.fields.IntegerField')(default=1))

    models = {
        u'areas.areas': {
            'Meta': {'object_name': 'Areas', 'db_table': "'areas'"},
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
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
        },
        u'categorias.categorias': {
            'Meta': {'object_name': 'Categorias', 'db_table': "'categorias'"},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['areas.Areas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'publicaciones.comentarios': {
            'Meta': {'object_name': 'Comentarios', 'db_table': "'comentarios_pub'"},
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publicacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publicaciones.Publicaciones']"})
        },
        u'publicaciones.publicaciones': {
            'Meta': {'object_name': 'Publicaciones', 'db_table': "'publicaciones'"},
            'autores': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['autores.Autores']"}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['categorias.Categorias']"}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'fechaPub': ('django.db.models.fields.DateField', [], {}),
            'fechaReg': ('django.db.models.fields.DateField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informacion': ('django.db.models.fields.TextField', [], {}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'issn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lecturas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resumen': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['publicaciones']