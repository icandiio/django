import logging

from django.conf import settings
from django.contrib.auth.hashers import make_password

from django_common.views import DispatchView
from m1auth.const import SessionK, AuthK
from m1auth.models import User

logger = logging.getLogger(__name__)


def set_password(password, user_salt):
    k = "%s|%s|%s" % (password, user_salt, settings.M1AUTH_SALT)
    # return make_password(password, hasher="unsalted_md5")
    return make_password(k, hasher="unsalted_md5")


class AuthView(DispatchView):

    def login(self, request):
        data = self.body2json(request)
        try:
            obj = User.objects.get(username=data.get(AuthK.username))
            password = set_password(data.get(AuthK.password), data.get(AuthK.username))
            if password == obj.password:
                request.session[SessionK.auth_user_key] = obj.id
                request.session[SessionK.auth_user_tp] = obj.tp
            else:
                return self.reply(0, "", "密码错误")
        except Exception as ex:
            logger.exception(ex)
            return self.reply(0, "", "用户不存在")
        return self.reply()

    def logout(self, request):
        if SessionK.auth_user_key in request.session:
            del request.session[SessionK.auth_user_key]
        return self.reply()

    def current_userinfo(self, request):
        logger.info(request.session)
        uid = request.session.get(SessionK.auth_user_key, 0)
        obj = list(User.objects.values("username", "rname", "mobile", "email").filter(id=uid))
        if len(obj) == 0:
            return self.reply(0, "", "登录已过期或用户信息有误")
        else:
            return self.reply(data=obj[0])

    def change_password(self, request):
        data = self.body2json(request)
        uid = request.session.get(SessionK.auth_user_key, 0)
        if uid != 0:
            obj = User.objects.get(id=uid)
            password = set_password(data.get(AuthK.password), data.get(AuthK.username))
            if password == obj.password:
                _password = set_password(data.get("npassword"), obj.username)
                obj.password = _password
                obj.save()
            else:
                return self.reply(0, "", "原始密码错误")
        else:
            return self.reply(0, "", "参数错误")
        return self.reply()

    def change_userinfo(self, request):
        data = self.body2json(request)
        uid = request.session.get(SessionK.auth_user_key, 0)
        if uid != 0:
            User.objects.filter(id=uid).update(**data)
        else:
            return self.reply(0, "", "参数错误")

        return self.reply()

    def edit_userinfo(self, request):
        data = self.body2json(request)
        User.objects.filter(id=data.get("id", 0)).update(**data)
        return self.reply()

    def rset_userpassword(self, request):
        data = self.body2json(request)
        uid = data.get("id", None)
        password = data.get("password", None)
        username = data.get("username", None)
        if uid and password and username:
            _password = set_password(password, username)
            User.objects.filter(id=uid).update(password=_password)
        else:
            return self.reply(0, "", "参数错误")

        return self.reply()

    def change_state(self, request):
        data = self.body2json(request)
        oid = data.get("id", None)
        state = data.get("state", None)
        if oid and state:
            User.objects.filter(id=oid).update(state=state)
        else:
            return self.reply(0, "", "参数有误")
        return self.reply()

    def new_user(self, request):
        data = self.body2json(request)

        username = data.get(AuthK.username)
        password = data.pop(AuthK.password)
        _password = set_password(password, username)
        data.update({AuthK.password: _password})
        try:
            if not User.objects.filter(username=data.get(AuthK.username)).exists():
                User.objects.create(**data)
            else:
                return self.reply(0, "", "用户名已存在")
        except Exception as ex:
            logger.exception(ex)
            return self.reply(0)

        return self.reply()

    def update_or_create(self, request):
        data = self.body2json(request)

        _id = data.get("id", None)
        username = data.get(AuthK.username)
        password = data.pop(AuthK.password)
        _password = set_password(password, username)
        data.update({"password": _password})
        try:
            if _id:
                User.objects.filter(id=_id).update(**data)
            else:
                User.objects.create(**data)
        except Exception as ex:
            logger.exception(ex)
            return self.reply(0)

        return self.reply()
