from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from jaam.stories.models import Story

def details(request, project_slug, story_slug):
    story = get_object_or_404(Story, slug=story_slug)
    return render_to_response('story_details.html', { 'story': story }, context_instance=RequestContext(request))
