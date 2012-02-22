from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from jaam.projects.models import Project
from jaam.photos.models import Photo, PhotoGallery
# Create your views here.
def galleries(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    galleries = project.photogallery_set.all()
    return render_to_response('photos/photo_galleries.html', { 'galleries': galleries, 'project': project }, context_instance=RequestContext(request))

def gallery_details(request, project_slug, gallery_slug):
    project = get_object_or_404(Project, slug=project_slug)
    gallery = get_object_or_404(PhotoGallery, slug=gallery_slug)
    photos = [i.photo for i in gallery.photogalleryitem_set.order_by('order')]
    return render_to_response('photos/photo_gallery.html', { 'gallery': gallery, 'photos': photos, 'project': project }, context_instance=RequestContext(request))

def details(request, project_slug, photo_id):
    project = get_object_or_404(Project, slug=project_slug)
    photo = get_object_or_404(Photo, pk=photo_id)
    return render_to_response('photos/photo_details.html', { 'photo': photo, 'project': project }, context_instance=RequestContext(request))

def index(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    photos = project.photo_set.all()
    return render_to_response('photos/index.html', {'photos': photos, 'project': project }, context_instance=RequestContext(request))