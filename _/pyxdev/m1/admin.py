from django.contrib import admin

# Register your models here.
from m1.models import Addr


# 手动编程版
# 1.default admin form
# admin.site.register(Addr) # 默认显示所有字段

# 2.customize admin form
# class AddrAdmin(admin.ModelAdmin):
#     list_display = ("id", "m1", "m2", "sex", "ctime", "utime")
#     ordering = []
#     actions = []
# admin.site.register(Addr, AddrAdmin)


# 注解方式
@admin.register(Addr)
class AddrAdmin(admin.ModelAdmin):
    # add or change form field of detail page,choose one method
    # fields = () # form提交时包含的字段,可以组装合并字段
    # exclude = () # form提交时排除的字段
    # fieldsets =() # form 加强版
    list_display = ("id", "m1", "m2", "sex", "ctime", "utime")  # 不能合并字段
    list_filter = ("sex",)
    search_fields = ['id', 'm1', 'm2']
    ordering = ['-utime']
    actions = []
