# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PhotoExifData'
        db.create_table('photos_photoexifdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('camera_manufacturer', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('camera_model', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('shutter_speed', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('fnumber', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('focal_length', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('flash_used', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('height_dimension', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('width_dimension', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('gps_latitude', self.gf('django.db.models.fields.CharField')(max_length=45, null=True)),
            ('gps_longitude', self.gf('django.db.models.fields.CharField')(max_length=45, null=True)),
            ('altitude', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
        ))
        db.send_create_signal('photos', ['PhotoExifData'])

        # Adding model 'Photo'
        db.create_table('photos_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('journalist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('exif_data', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['photos.PhotoExifData'], unique=True, null=True, blank=True)),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('photos', ['Photo'])

        # Adding M2M table for field tags on 'Photo'
        db.create_table('photos_photo_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo', models.ForeignKey(orm['photos.photo'], null=False)),
            ('tag', models.ForeignKey(orm['journalism.tag'], null=False))
        ))
        db.create_unique('photos_photo_tags', ['photo_id', 'tag_id'])

        # Adding model 'PhotoGallery'
        db.create_table('photos_photogallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('introduction', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
        ))
        db.send_create_signal('photos', ['PhotoGallery'])

        # Adding M2M table for field tags on 'PhotoGallery'
        db.create_table('photos_photogallery_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photogallery', models.ForeignKey(orm['photos.photogallery'], null=False)),
            ('tag', models.ForeignKey(orm['journalism.tag'], null=False))
        ))
        db.create_unique('photos_photogallery_tags', ['photogallery_id', 'tag_id'])

        # Adding model 'PhotoGalleryItem'
        db.create_table('photos_photogalleryitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Photo'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.PhotoGallery'])),
        ))
        db.send_create_signal('photos', ['PhotoGalleryItem'])


    def backwards(self, orm):
        
        # Deleting model 'PhotoExifData'
        db.delete_table('photos_photoexifdata')

        # Deleting model 'Photo'
        db.delete_table('photos_photo')

        # Removing M2M table for field tags on 'Photo'
        db.delete_table('photos_photo_tags')

        # Deleting model 'PhotoGallery'
        db.delete_table('photos_photogallery')

        # Removing M2M table for field tags on 'PhotoGallery'
        db.delete_table('photos_photogallery_tags')

        # Deleting model 'PhotoGalleryItem'
        db.delete_table('photos_photogalleryitem')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'journalism.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exif_data': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['photos.PhotoExifData']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'}),
            'journalist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['journalism.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'photos.photoexifdata': {
            'Meta': {'object_name': 'PhotoExifData'},
            'altitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'camera_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'camera_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'flash_used': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'fnumber': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'focal_length': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'gps_latitude': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True'}),
            'gps_longitude': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True'}),
            'height_dimension': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shutter_speed': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'width_dimension': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'})
        },
        'photos.photogallery': {
            'Meta': {'object_name': 'PhotoGallery'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['photos.Photo']", 'through': "orm['photos.PhotoGalleryItem']", 'symmetrical': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['journalism.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'photos.photogalleryitem': {
            'Meta': {'object_name': 'PhotoGalleryItem'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.PhotoGallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']"})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'accentColor': ('django.db.models.fields.CharField', [], {'default': "'FFFFFF'", 'max_length': '7'}),
            'coverGallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['photos.PhotoGallery']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.ProjectLocation']", 'symmetrical': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'primaryColor': ('django.db.models.fields.CharField', [], {'default': "'FF0000'", 'max_length': '7'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['journalism.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.projectlocation': {
            'Meta': {'object_name': 'ProjectLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['photos']
