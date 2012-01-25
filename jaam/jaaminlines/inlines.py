# The below is unneccessary.
# from django_inlines import inlines

# Only thing I can imagine is if you ever need to pass more to
# the template in the context.
#
# class PhotoInline(inlines.TemplateInline):
# 	def get_context():
# 		return {
# 			'id': self.value,
# 			''	
# 		};

# class VideoInline(inlines.TemplateInline):
# 	def get_context():
# 		pass

# inlines.registry.register('photo', PhotoInline)
# inlines.registry.register('video', VideoInline)

from django_inlines import inlines
inlines.registry.register('photo', inlines.inline_for_model(Photo));
inlines.registry.register('video', inlines.inline_for_model(Video));