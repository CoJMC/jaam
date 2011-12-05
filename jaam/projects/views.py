from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jaam.shortcuts import render_to_response, RequestContext

from jaam.projects.models import Project
from jaam.blog.models import BlogPost
from django.contrib.auth.models import User

def index(request):
    projects = Project.objects.all()
    return render_to_response('index.html', { 'projects': projects }, context_instance=RequestContext(request))

def details(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    #in your template, filter out. We need the whole list.
    photos = project.photo_set.all()
    video = project.video_set.all()
    story = project.story_set.all()
    blog_post = BlogPost.objects.filter(blog__project__slug=project_slug)
    contributors = User.objects.filter(photo__project__slug=project_slug).distinct()
    return render_to_response('project_details.html', {
        'project': project,
        'photos': photos,
        'video': video,
        'story': story,
        'blog_post': blog_post,
        'contributors': contributors,
    }, context_instance=RequestContext(request))
