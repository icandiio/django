from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^(\w*)$", views.AuthView.as_view()),
]
