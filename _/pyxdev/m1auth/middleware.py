import json
import logging

import re
from django.conf import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from m1auth.const import SessionK

logger = logging.getLogger(__name__)


class AuthorizationMiddleware(MiddlewareMixin):
    rpath = re.compile(r"^/static/?|^/admin/?|.*\.ico$")
    ignore_urls = settings.M1AUTH_MIDDLEWARE_IGNORE_URLS
    kwargs = {
        "content_type": 'application/json'
    }

    def __init__(self, get_response=None):
        MiddlewareMixin.__init__(self, get_response)

    def process_request(self, request):
        path = request.path

        if self.rpath.match(path):
            pass
        elif path in self.ignore_urls:
            pass
        else:
            auth_user_id = request.session.get(SessionK.auth_user_key, None)
            if not auth_user_id:  # 未登录
                rjson = {
                    "status": 401,
                    "msg": "noAuthorization"
                }
                return HttpResponse(json.dumps(rjson), **self.kwargs)
            else:  # 已登录，权限验证
                pass
