from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jaam.shortcuts import render_to_response, RequestContext

from jaam.projects.models import Project

def index(request):
    projects = Project.objects.all()
    return render_to_response('index.html', { 'projects': projects }, context_instance=RequestContext(request))

def details(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render_to_response('project_details.html', { 'project': project }, context_instance=RequestContext(request))
