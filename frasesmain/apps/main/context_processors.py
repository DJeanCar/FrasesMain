from django.conf import settings

def send_debug(request):
	return { 'debug': settings.DEBUG }