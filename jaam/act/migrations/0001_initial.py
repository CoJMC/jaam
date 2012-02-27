# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Act'
        db.create_table('act_act', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('act_code', self.gf('ckeditor.fields.RichTextField')()),
        ))
        db.send_create_signal('act', ['Act'])


    def backwards(self, orm):
        
        # Deleting model 'Act'
        db.delete_table('act_act')


    models = {
        'act.act': {
            'Meta': {'object_name': 'Act'},
            'act_code': ('ckeditor.fields.RichTextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['act']
