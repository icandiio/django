# from django.contrib import admin
# from djcelery.models import TaskMeta
#
#
# # Register your models here.
#
# # 非本地App中的admin.ModelAdmin
#
# @admin.register(TaskMeta)
# class TaskMetaAdmin(admin.ModelAdmin):
#     readonly_fields = ('id', 'result', 'meta',)
#     search_fields = ('id', 'task_id',)
#     list_filter = ('status',)
#
#     # def get_queryset(self, request):
#     #     qs = super().get_queryset(request)
#     #     return qs.filter(result__isnull=False)
