from django.contrib import admin
from jaam.photos.models import Photo, PhotoGallery, PhotoExifData, PhotoGalleryItem
from jaam.journalism.admin import BaseAdmin
from jaam.photos.widgets import AdminImageWidget
from easy_thumbnails.fields import ThumbnailerImageField

class PhotoAdmin(BaseAdmin):
    search_fields = ('title', 'caption',)
    list_display = ('__unicode__', 'caption', 'journalist', 'published')
    list_filter = ( 'project', 'published')
    prepopulated_fields = { 'slug': ('title',)}
    filter_horizontal = ('tags',)
    fieldsets = (
                 (None, { 'fields': ('project', 'title', 'slug', 'image', 'caption',) },),
                 ('Admin', { 'fields': ('journalist', 'published',) },),
                )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.journalist = request.user
        obj.save()

class PhotoGalleryInline(admin.TabularInline):
    template = 'admin/edit_inline/photo_gallery.html'
    model = PhotoGalleryItem
    ordering = ['order']
    extra = 0

class PhotoGalleryAdmin(BaseAdmin):
    inlines = [ PhotoGalleryInline ]
    list_display = ('__unicode__', 'project', 'introduction', 'published')
   # list_filter = ('video gallery')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
                 (None, { 'fields': ('project', 'title', 'slug', 'introduction', 'tags',) },),
                 ('Admin', { 'fields': ('published',) },),
                )

class PhotoExifDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(PhotoExifData, PhotoExifDataAdmin)
