from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from forms import UserProfileForm

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render_to_response('journalism/user_profile.html', { 'user': user }, context_instance=RequestContext(request))

def about(request):
    return render_to_response('journalism/about_us.html', context_instance=RequestContext(request))

@csrf_protect
def profile_set(request):
    user = request.user
    profile = user.get_profile()
    is_journalist = profile.is_journalist

    if request.method == 'POST': # If the form has been submitted...
        profile_form = UserProfileForm(request.POST, request.FILES)
            
        if profile_form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data and return to the admin
            profile.full_name = profile_form.cleaned_data['full_name']
            profile.avatar = request.POST.get('avatar')
            profile.bio = profile_form.cleaned_data['bio']
            profile.major = profile_form.cleaned_data['major']

            user.email = profile_form.cleaned_data['email']
            user.save()
            profile.save()
        
        return HttpResponseRedirect('/admin') # Redirect after POST
    else:      
        profile_form = UserProfileForm(initial={'full_name': profile.full_name, 'email': user.email}) # An unbound form
        return render_to_response('journalism/success.html', {
           'profile_form': profile_form, 
        },  context_instance=RequestContext(request))
