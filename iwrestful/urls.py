from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.WorkflowListAPI.as_view()),
    url(r'^update/(?P<pk>[0-9]+)$', views.WorkflowUpdateAPI.as_view()),
]