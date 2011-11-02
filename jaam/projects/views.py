from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from jaam.projects.models import Project

def details(request, project_slug):
    print project_slug
    project = get_object_or_404(Project, slug=project_slug)
    return HttpResponse(str(project))
