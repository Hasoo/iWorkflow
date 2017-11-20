from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^board/', views.iw_list, name='iw_list'),
]