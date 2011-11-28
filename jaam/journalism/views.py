from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
from django.contrib.auth.models import User
from jaam.shortcuts import render_to_response, RequestContext

def activate_layout(request, layout_name):
    if layout_name in ['dora', 'tico']:
        request.session['layout'] = layout_name
        return redirect('/')
    else:
        return HttpResponse("Invalid layout")

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render_to_response('user_profile.html', { 'user': user }, context_instance=RequestContext(request))

def login_dump(request):
    return render_to_response('success.html')

