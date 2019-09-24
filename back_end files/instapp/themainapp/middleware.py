from django.utils.deprecation import MiddlewareMixin
import json
import os
import instapp.settings as settings
from django.http.request import QueryDict


class ParseJsonMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if 'application/json' in request.headers['Content-Type']:
            try:
                request.POST = json.loads(request.body.decode())
            except:
                pass


class SetCookieFromTokenMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        try:
            if settings.DEBUG and request.headers.get('token') is not None:
                for cookie_string in request.headers.get('token').split(';'):
                    cookie = cookie_string.strip().split(':')
                    request.COOKIES[cookie[0].strip()] = cookie[1].strip()
        except Exception as err:
            pass
