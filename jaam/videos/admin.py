from django.contrib import admin
from jaam.videos.models import Video, VideoGallery, VideoGalleryItem
from jaam.journalism.admin import BaseAdmin

class VideoAdmin(BaseAdmin):
    search_fields = ('title', 'caption',)
    list_display = ('__unicode__', 'project', 'caption', 'journalist', 'published')
    list_filter = ( 'project', 'published')
    prepopulated_fields = { 'slug': ('title',)}
    filter_horizontal = ('tags',)
    fieldsets = [
                 (None, { 'fields': ('project', 'title', 'slug', 'videoUrl', 'caption',) },),
                 ('Admin', { 'fields': ('journalist', 'published',) },),
                ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.journalist = request.user
        obj.save()

class VideoGalleryItemInline(admin.TabularInline):
    template = 'admin/edit_inline/video_gallery.html'
    model = VideoGalleryItem
    ordering = ['order']
    extra = 0

class VideoGalleryAdmin(BaseAdmin):
    inlines = [VideoGalleryItemInline]
    list_display = ('project', '__unicode__', 'introduction', 'published')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
                 (None, { 'fields': ('project', 'title', 'slug', 'introduction', 'tags',) },),
                 ('Admin', { 'fields': ('published',) },),
                ]

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('published')
            self.exclude.append('journalist')
        return super(VideoGalleryAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoGallery, VideoGalleryAdmin)
