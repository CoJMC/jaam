from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
from django.contrib.auth.models import User

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render_to_response('user_profile.html', { 'user': user }, context_instance=RequestContext(request))

def login_dump(request):
    return render_to_response('success.html')

