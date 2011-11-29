from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import UserProfileForm, JournalistForm
from django.views.decorators.csrf import csrf_protect
from jaam.journalism.models import Journalist


# Create your views here.
from django.contrib.auth.models import User
from jaam.shortcuts import render_to_response, RequestContext

def activate_layout(request, layout_name):
    if layout_name in ['dora', 'tico']:
        request.session['layout'] = layout_name
        if('HTTP_REFERER' in request.META):
            return redirect(request.META['HTTP_REFERER'])
        else: return redirect("/")
    else:
        return HttpResponse("Invalid layout")

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render_to_response('user_profile.html', { 'user': user }, context_instance=RequestContext(request))

@csrf_protect
def profile_set(request):   
    user = request.user
    profile = user.userprofile
    is_journalist = False
    #determine if user is a journalist 
    
    if request.method == 'POST': # If the form has been submitted...
        profile_form = UserProfileForm(request.POST, request.FILES)
        if profile_form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data and return to the admin
            profile.full_name = profile_form.cleaned_data['full_name']
            profile.avatar = request.POST.get('avatar')
            user.email = profile_form.cleaned_data['email']
            user.save()
            profile.save()
            
            if is_journalist:
                journalist_form = JournalistForm(request.POST)
                if journalist_form.is_valid():
                    journalist = profile.journalist
                    journalist.user_profile = profile
                    journalist.bio = journalist_form.cleaned_data['bio']
                    journalist.major = journalist_form.cleaned_data['major']
                    journalist.save()
            
            return HttpResponseRedirect('/admin/') # Redirect after POST
    else:      
        profile_form = UserProfileForm(initial={'full_name': profile.full_name, 'email': user.email}) # An unbound form
        if is_journalist is False:
            return render_to_response('success.html', {
            'profile_form': profile_form, 
        },  context_instance=RequestContext(request))
        
        else: 
            journalist_form = JournalistForm()
            return render_to_response('success.html', {
                'profile_form': profile_form,'journalist_form': journalist_form 
            },  context_instance=RequestContext(request))
