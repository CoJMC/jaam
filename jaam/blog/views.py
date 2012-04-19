from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jaam.projects.models import Project

from jaam.blog.models import Blog, BlogPost

def blog_details(request, project_slug, blog_title_slug):
    project = get_object_or_404(Project, slug=project_slug)
    blog = get_object_or_404(Blog, slug=blog_title_slug)
    return render_to_response('blog/blog_details.html', { 'blog': blog, 'project': project, 'title': blog.title }, context_instance=RequestContext(request))

def post_details(request, project_slug, blog_title_slug, blog_post_slug):
    post = get_object_or_404(BlogPost, slug=blog_post_slug)
    return render_to_response('blog/post_details.html', { 'post': post }, context_instance=RequestContext(request))

def index(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    blogs = project.blog_set.all()
    return render_to_response('blog/blog_gallery.html', {'project': project, 'blogs': blogs, 'title': 'blogs' } ,context_instance=RequestContext(request))