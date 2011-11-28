from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from jaam.shortcuts import render_to_response, RequestContext

from jaam.blog.models import Blog, BlogPost
def blog_details(request, project_slug, blog_title_slug):
    blog = get_object_or_404(Blog, slug=blog_title_slug)
    return render_to_response('blog_details.html', { 'blog': blog }, context_instance=RequestContext(request))

def post_details(request, project_slug, blog_title_slug, blog_post_slug):
    post = get_object_or_404(BlogPost, slug=blog_post_slug)
    return render_to_response('post_details.html', { 'post': post }, context_instance=RequestContext(request))
