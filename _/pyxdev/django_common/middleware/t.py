import logging

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class TestMiddleware(MiddlewareMixin):
    """
    process_request()方法，在配置URLconf之前被调用
    process_view()方法，在执行视图之前被调用

    process_template_response()方法，在执行视图之后被调用
    process_response()方法，在返回浏览器之前(调用模板之后)被调用
    process_exception()方法，在执行视图过程中，出现异常时被调用，返回给浏览器

    基本流程：process_request -> URLconf -> process_view -> view [ -> process_template_response ] -> process_response

    在某个环节中直接返回 HttpResponse 会跳过后续流程

    不能在process_request 或者process_view 来访问request.POST
    """

    def __init__(self, get_response=None):
        MiddlewareMixin.__init__(self, get_response)

    def process_request(self, request):
        pass

    def process_view(self, request, callback, callback_args, callback_kwargs):
        pass

    def process_template_response(self, request, response):
        # views函数中返回的对象中具有render方法
        return response

    def process_exception(self, request, exception):
        pass

    def process_response(self, request, response):
        return response
