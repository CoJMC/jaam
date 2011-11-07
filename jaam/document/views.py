from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def details(request, project_slug, document_slug):
    return HttpResponse(document_slug + ' - ' + project_slug)
