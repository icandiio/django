from django.db import models

from django_common.db.models import AbsTimeModel


class UserK:
    nomral = 1
    admin = 2
    SysAdmin = 9


STATE_CHOICES = ((0, "默认"), (1, "正常"), (-1, "删除"),)
TP_CHOICES = ((0, "默认"), (1, "普通用户"), (2, "管理员"), (9, "系统管理员"))


class User(AbsTimeModel):
    username = models.CharField(max_length=128, null=True, unique=True, verbose_name="登录名")
    password = models.CharField(max_length=256, null=True, verbose_name="密码")

    rname = models.CharField(max_length=256, null=True, verbose_name="姓名")
    mobile = models.CharField(max_length=256, null=True, verbose_name="电话")
    email = models.CharField(max_length=256, null=True, verbose_name="邮箱")

    state = models.IntegerField(null=False, default=0, choices=STATE_CHOICES, verbose_name="状态")
    tp = models.IntegerField(null=False, default=0, choices=TP_CHOICES, verbose_name="类型")
