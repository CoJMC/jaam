from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jaam.projects.models import Project

from jaam.stories.models import Story
from jaam.photos.models import Photo
from jaam.videos.models import Video

def details(request, project_slug, story_slug):
    from django_inlines import inlines
    inlines.registry.register('photo', inlines.inline_for_model(Photo));
    inlines.registry.register('video', inlines.inline_for_model(Video));
    story = get_object_or_404(Story, slug=story_slug)
    title = story.title
    project = get_object_or_404(Project, slug=project_slug)
    return render_to_response('stories/story_details.html', { 'project': project, 'story': story, 'title': title }, context_instance=RequestContext(request))

def list(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render_to_response('stories/story_gallery.html', { 'project': project, 'title': "stories"}, context_instance=RequestContext(request))
