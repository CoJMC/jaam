from django.shortcuts import render_to_response as rtr
from django.template import RequestContext as RContext
import random

class RequestContext(RContext):
    def __init__(self, request):
        self.request = request
        super(RContext, self).__init__(request)

def render_to_response(template_name, dictionary, context_instance):
    if context_instance.request.session.has_key('layout') == False:
        context_instance.request.session['layout'] = random.choice(['dora', 'tico'])
    return rtr(context_instance.request.session['layout'] + '/' + template_name, dictionary, context_instance)

