from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import User

from jaam.projects.models import Project
from jaam.photos.models import Photo, PhotoGallery
# Create your views here.
def galleries(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    #galleries = project.photogallery_set.all()
    #galleries = project.photogallery_set.filter(published=True)
    galleries = PhotoGallery.objects.filter(project_id=project.id)
    return render_to_response('photos/photo_galleries.html', { 'galleries': galleries, 'project': project }, context_instance=RequestContext(request))

def gallery_details(request, project_slug, gallery_slug, start_number=1):
    #This is REALLY jankety and should be fixed :p
    project = get_object_or_404(Project, slug=project_slug)
    gallery = get_object_or_404(PhotoGallery, slug=gallery_slug)
    previous_number = int(start_number) -3
    
    size = gallery.photogalleryitem_set.order_by('order').__len__() -1 
    available_photos = gallery.photogalleryitem_set.filter(photo__published=True)
    
    if int(start_number) ==  size:
        photos_before = [i.photo for i in available_photos.filter(order__lte=start_number).order_by('order').reverse()[:6]]
    elif int(start_number) ==  size-1:
        photos_before = [i.photo for i in available_photos.filter(order__lte=start_number).order_by('order').reverse()[:5]]
    elif int(start_number) ==  size-2:
        photos_before = [i.photo for i in available_photos.filter(order__lte=start_number).order_by('order').reverse()[:4]]       
    else :
        photos_before = [i.photo for i in available_photos.filter(order__lte=start_number).order_by('order').reverse()[:3]]
    
    photos_before.reverse()
    number_before = photos_before.__len__()
    if number_before == 0: 
        photos_after = [i.photo for i in available_photos.filter(order__gt=start_number).order_by('order')[:7]]
    elif number_before == 1:
        photos_after = [i.photo for i in available_photos.filter(order__gt=start_number).order_by('order')[:6]]
    elif number_before == 2:
        photos_after = [i.photo for i in available_photos.filter(order__gt=start_number).order_by('order')[:5]]
    else:
        photos_after = [i.photo for i in available_photos.filter(order__gt=start_number).order_by('order')[:4]] 
    first_photo = available_photos.order_by('order')[int(start_number)].photo
    photos_swipe = [i.photo for i in available_photos.filter(order__gte=start_number).order_by('order')]
    return render_to_response('photos/gallery_details.html', { 'gallery': gallery, 'photos_before': photos_before, 'photos_after': photos_after, 'photos_swipe': photos_swipe, 'project': project, 'first_photo': first_photo, 'previous_number': previous_number, 'next_number': start_number}, context_instance=RequestContext(request))

def details(request, project_slug, photo_id):
    project = get_object_or_404(Project, slug=project_slug)
    photo = get_object_or_404(Photo, pk=photo_id)
    journalist = User.objects.get(username=photo.journalist)
    return render_to_response('photos/photo_details.html', { 'photo': photo, 'project': project, 'journalist': journalist }, context_instance=RequestContext(request))

def index(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    photos = project.photo_set.all()
    return render_to_response('photos/index.html', {'photos': photos, 'project': project }, context_instance=RequestContext(request))