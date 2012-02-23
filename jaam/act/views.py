from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jaam.projects.models import Project
from jaam.act.models import Act

def details(request, project_slug, act_slug):
    project = get_object_or_404(Project, slug=project_slug)
    act = get_object_or_404(Act, slug=act_slug)
    return render_to_response('act/act_details.html', { 'act': act, 'project': project, 'title': act}, context_instance=RequestContext(request))

def information(request):
    return render_to_response('act/act_information.html', context_instance=RequestContext(request))