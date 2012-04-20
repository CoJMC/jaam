from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
import datetime
import math
import string

from django.contrib.auth import logout
from django.contrib.auth.models import User
from forms import UserProfileForm

def user_profile(request, username):
    journalist = get_object_or_404(User, username=username)
    embed = False
    if "embedded" in request.GET and request.GET["embedded"]:
        embed = True
    return render_to_response('journalism/user_profile.html', { 'journalist': journalist, 'embed': embed }, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@csrf_protect
def profile_set(request):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseNotFound('You must be logged in to see this page.')

    profile = user.get_profile()
    is_journalist = profile.is_journalist()

    if request.method == 'POST': # If the form has been submitted...
        profile_form = UserProfileForm(request.POST, request.FILES)

        if profile_form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data and return to the admin
            profile.full_name = profile_form.cleaned_data['full_name']
            profile.avatar = request.POST.get('avatar')
            #profile.bio = profile_form.cleaned_data['bio']
            #profile.major = profile_form.cleaned_data['major']
            profile.profile_set = True

            user.email = profile_form.cleaned_data['email']
            user.save()
            profile.save()
        return HttpResponseRedirect('/') # Redirect after POST
    else:
        if profile.profile_set == False: # if the user has not submitted their information
            profile_form = UserProfileForm(initial={'full_name': profile.full_name, 'email': user.email}) # An unbound form
            return render_to_response('journalism/user_profile_edit.html', {
               'profile_form': profile_form,
            },  context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/')

