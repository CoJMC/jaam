from django.conf import settings

def constants(context):
	return {
		'GOOGLE_UA_ID': settings.GOOGLE_UA_ID
	}