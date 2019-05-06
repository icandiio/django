# coding:utf-8

from django.db import models

from django_common.db.models import AbsTimeModel

# Create your models here.

SEX_CHOICES = (("0", "未知"), ("1", "男"), ("2", "女"),)


class Addr(AbsTimeModel):  # 只能单继承
    m1 = models.CharField(max_length=256, null=True)
    m2 = models.CharField(max_length=256, null=True)

    sex = models.CharField(max_length=2, null=False, default=0, choices=SEX_CHOICES, verbose_name="性别")

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return str(self.id)
