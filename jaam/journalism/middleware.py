# had this middleware implemented but didn't know how to limit to thread

# credit for thread idea goes to http://nedbatchelder.com/blog/201008/global_django_requests.html

# modified from: http://code.google.com/p/dojango/issues/attachmentText?id=67&aid=8141374391356887175&name=dojo_collector.diff&token=NGnm9pcd_9hR0cAmzBOeOPMlSIg%3A1328672858705
#           via: http://code.google.com/p/dojango/issues/detail?id=67

from threading import local
_active = local()

def _show_unpublished():
    return _active._show_unpublished

class PublishFlexMiddleware():
	def process_request(self, request):
		b = False
		if request.user.is_authenticated() and request.user.get_profile().is_journalist and "show_unpublished" in request.GET:
			b = True
		
		_active._show_unpublished = b
		return None