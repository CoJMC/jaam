# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting field 'Project.longitude'
        db.delete_column('projects_project', 'longitude')

        # Deleting field 'Project.latitude'
        db.delete_column('projects_project', 'latitude')

        # Adding field 'Project.coverGallery'
        db.add_column('projects_project', 'coverGallery', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['photos.PhotoGallery']), keep_default=False)

        # Changing field 'Project.published'
        db.alter_column('projects_project', 'published', self.gf('django.db.models.fields.BooleanField')(blank=True))
    
    
    def backwards(self, orm):
        
        # Adding field 'Project.longitude'
        db.add_column('projects_project', 'longitude', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'Project.latitude'
        db.add_column('projects_project', 'latitude', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Deleting field 'Project.coverGallery'
        db.delete_column('projects_project', 'coverGallery_id')

        # Changing field 'Project.published'
        db.alter_column('projects_project', 'published', self.gf('django.db.models.fields.BooleanField')())
    
    
    models = {
        'journalism.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'photos.photogallery': {
            'Meta': {'object_name': 'PhotoGallery'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['journalism.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'coverGallery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['photos.PhotoGallery']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.ProjectLocation']", 'symmetrical': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['journalism.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.projectlocation': {
            'Meta': {'object_name': 'ProjectLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }
    
    complete_apps = ['projects']
