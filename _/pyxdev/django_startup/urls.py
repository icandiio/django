"""pydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

urlpatterns = [
    url(r"^/?$", RedirectView.as_view(url=r"/static/index.html")),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'/static/media/favicon.ico')),
    url(r'^robots.txt$', RedirectView.as_view(url=r'/static/media/robots.txt')),
    # admin
    url(r'^admin/', admin.site.urls),
    # auth
    url(r'^m1auth/', include('m1auth.urls')),
    # app
    url(r'^m1/', include("m1.urls")),
]

# !!! staticfiles 路径特殊处理，gunicorn 管理时如果没有此行，静态文件是没有办法访问的
urlpatterns += staticfiles_urlpatterns()
