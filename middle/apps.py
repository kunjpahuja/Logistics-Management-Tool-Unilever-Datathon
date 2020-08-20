from django.apps import AppConfig
from django.utils.deprecation import MiddlewareMixin

class MiddleConfig(AppConfig):
    name = 'middle'

class DisableCSRF(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
