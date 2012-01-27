from django.contrib import admin
from jaam.photos.models import Photo, PhotoGallery, PhotoExifData, PhotoGalleryItem
from jaam.journalism.admin import BaseAdmin


class PhotoAdmin(BaseAdmin):
    search_fields = ('title', 'caption',)
    list_display = ('__unicode__', 'caption', 'journalist',)
    list_filter = ( 'project', )
    prepopulated_fields = { 'slug': ('title',)}
    filter_horizontal = ('tags',)
    fieldsets = (
                 (None, { 'fields': ('project', 'title', 'slug', 'image', 'caption',) },),
                 ('Admin', { 'fields': ('journalist', 'published',) },),
                )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('published')
            self.exclude.append('journalist')
        return super(PhotoAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.journalist = request.user
        obj.save()

class PhotoGalleryInline(admin.TabularInline):
    template = 'admin/edit_inline/photo_gallery.html'
    model = PhotoGalleryItem
    ordering = ['order']
    extra = 0

class PhotoGalleryAdmin(admin.ModelAdmin):
    inlines = [ PhotoGalleryInline ]
    list_display = ('project', '__unicode__', 'introduction')
   # list_filter = ('video gallery')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
                 (None, { 'fields': ('project', 'title', 'slug', 'introduction', 'tags',) },),
                 ('Admin', { 'fields': ('published',) },),
                )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('published')
            self.exclude.append('author')
        return super(PhotoGalleryAdmin, self).get_form(request, obj, **kwargs)

class PhotoExifDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(PhotoExifData, PhotoExifDataAdmin)
