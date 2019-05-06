from django.db import models


class AbsTimeModel(models.Model):
    """
       auto_now just for model.save(),QuerySet.update() not exec udpated,
       auto_now_add just for create, will override if manual set value
       if True, cause the field to have editable=False and blank=True set
       """
    ctime = models.DateTimeField(db_index=True, null=True, auto_now_add=True, verbose_name="创建时间")

    utime = models.DateTimeField(db_index=True, null=True, auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True
