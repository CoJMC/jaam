from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, RequestContext

from jaam.videos.models import Video, VideoGallery
from jaam.projects.models import Project

# Create your views here.
def gallery_details(request, project_slug, gallery_slug):
    project = get_object_or_404(Project, slug=project_slug)
    gallery = get_object_or_404(VideoGallery, slug=gallery_slug)
    return render_to_response('videos/video_gallery.html', { 'gallery': gallery }, context_instance=RequestContext(request))

def details(request, project_slug, video_id):
    project = get_object_or_404(Project, slug=project_slug)
    video = get_object_or_404(Video, pk=video_id)
    return render_to_response('videos/video_details.html', { 'video': video }, context_instance=RequestContext(request))

def index(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render_to_response('index.html', {'project': project } ,context_instance=RequestContext(request))

