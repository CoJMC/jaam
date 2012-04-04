from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from jaam.projects.models import Project

def home(request):
    projects = Project.published_objects.filter(archived=False).all()
    return render_to_response('home.html', {
        'projects': projects,
        'title': "List of All Projects",
    }, context_instance=RequestContext(request))
