from django.conf.urls import url

from . import views

# app_name = {namespace}

urlpatterns = [
    # name 给后端处理行为取别名，起到桥接作用
    # 在templates，models，views中使用name，即时网址变更也不用改代码
    # 如果要使用name，最好再加一个命名空间 app_name={namespace},避免冲突 => namespace:index
    #
    # function
    url(r"^$", views.index, name="index"),  # reverse("name",args=()) 执行方法调用
    url(r"^path/(\w+)/$", views.path_variable),  # 参数以位置参数的方式传递
    # url(r"^path/(?P<k1>\w+)/$", views.path), # 参数以命名分组的方式传递
    # class
    # as_view : transfer class to function implement
    url(r"^vindex/(\w+)/?$", views.Index2View.as_view()),

]
