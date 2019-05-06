import logging

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse

from django_common.views import DispatchView
from m1.tasks import call_task

"""
request => django.htpp.request.HttpRequest
"""

# Create your views here.


logger = logging.getLogger(__name__)


# function-based-view
def index(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    return HttpResponse("Hello World %s" % ip)


def path_variable(request, p1):
    logger.info(getattr(settings, "SECRET_KEY", None))
    return HttpResponse("Hello World %s %s" % (p1, request.GET.get("k1")))


# class-based-view <== recommand
class Index2View(DispatchView):
    def _get(self, request, *args, **kwargs):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        request.session["1"] = "1"
        request.session["k2"] = "k2"

        return HttpResponse("vindex Hello World %s" % ip)

    def cache(self, request):
        if "k" in request.GET:
            v = request.GET.get("k")
            cache.set("k", request.GET.get("k"), None)  # None:no timeout
        else:
            v = cache.get("k")
        return HttpResponse("cached %s " % v)

    def task(self, request):
        # call_task() # 普通调用
        result = call_task.delay()  # celery调用
        # AsyncResult.get(timeout=None, propagate=True, interval=0.5) # 同步调用
        v = result.get(timeout=5, propagate=False, interval=0.5)  # Wait until task is ready, and return its result.

        return HttpResponse("task return %s" % v)
