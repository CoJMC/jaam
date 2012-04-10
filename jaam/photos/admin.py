from django.contrib import admin
from jaam.photos.models import Photo, PhotoGallery, PhotoExifData, PhotoGalleryItem
from jaam.journalism.admin import BaseAdmin

class PhotoAdmin(BaseAdmin):
    add_form_template = 'admin/photo_add.html'
    search_fields = ('title', 'caption',)
    list_display = ('__unicode__', 'project', 'caption', 'journalist', 'published')
    list_filter = ( 'project', 'journalist', 'published')
    date_hierarchy = 'modified_at'
    prepopulated_fields = { 'slug': ('title',)}
    filter_horizontal = ('tags',)
    fieldsets = (
                 (None, { 'fields': ('project', 'image', 'title', 'slug', 'caption',) },),
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
    add_form_template = 'admin/photogallery_form.html'
    change_form_template = 'admin/photogallery_form.html'

    inlines = [ PhotoGalleryInline ]
    list_display = ('__unicode__', 'project', 'introduction', 'size', 'published',)
    list_filter = ('project', 'published',)
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
