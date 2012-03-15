from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jaam.projects.models import Project
from jaam.act.models import Act


def information(request):
    specific = False
    project =""
    if "project" in request.GET and request.GET["project"]:
        specific = True
        project_slug = request.GET["project"]
        project = get_object_or_404(Project, slug=project_slug)
        return render_to_response('act/act_details.html', { 'specific': specific, 'project': project }, context_instance=RequestContext(request))
    else:
                return render_to_response('act/act_information.html', context_instance=RequestContext(request))
