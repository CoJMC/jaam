from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jaam.shortcuts import render_to_response, RequestContext

from jaam.stories.models import Story
from jaam.photos.models import Photo
from jaam.videos.models import Video

def details(request, project_slug, story_slug):
    from django_inlines import inlines
    inlines.registry.register('photo', inlines.inline_for_model(Photo));
    inlines.registry.register('video', inlines.inline_for_model(Video));
    story = get_object_or_404(Story, slug=story_slug)
    return render_to_response('story_details.html', { 'story': story }, context_instance=RequestContext(request))