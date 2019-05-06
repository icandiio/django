import json

from pyx_gutils.misc.api_const import RspK

from django.http import JsonResponse
from django.views import View
from django_common.util.json import DjangoCustomJSONEncoder

__TARGET_METHOD__ = ""


class DispatchView(View):

    def dispatch(self, request, *args, **kwargs):
        """
        Implement AOP in View layer by overwrite super.dispatch method
        """
        rsp = super(DispatchView, self).dispatch(request, *args, **kwargs)
        return rsp

    def _get(self, request, *args, **kwargs):
        raise Exception("not implement")

    def _post(self, request, *args, **kwargs):
        raise Exception("not implement")

    def __hanlder(self, method, request, target_method, *args, **kwargs):
        handler = getattr(self, target_method, None)
        if handler is None:
            if target_method:  # 把数据拼接回去 {this moment target_method is position arg}
                args = (target_method,) + args
            return method(request, *args, **kwargs)
        else:
            return handler(request, *args, **kwargs)

    def _json_response(self, dic):
        return JsonResponse(dic, encoder=DjangoCustomJSONEncoder)

    def get(self, request, target_method=__TARGET_METHOD__, *args, **kwargs):
        return self.__hanlder(self._get, request, target_method, *args, **kwargs)

    def post(self, request, target_method=__TARGET_METHOD__, *args, **kwargs):
        return self.__hanlder(self._post, request, target_method, *args, **kwargs)

    def body2json(self, request):
        bstr = request.body.decode()
        if not bstr:
            bstr = "{}"
        return json.loads(bstr)

    def reply(self, status=1, data="", msg="", **kwargs):
        dic = {
            RspK.STATUS: status,
            RspK.DATA: data or {},
            RspK.MSG: msg
        }
        dic.update(**kwargs)
        return self._json_response(dic)
