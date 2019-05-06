from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", 'username', "mobile", "email", "state", "tp", "ctime", "utime")  # 不能合并字段
    list_filter = ("state", "tp")
    search_fields = ('id', 'username', 'mobile')
    ordering = ['-utime']
    actions = []
