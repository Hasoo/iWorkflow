from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/', views.loginCheck, name='loginCheck'),
    url(r'^logout/', views.logout, name='logout'),
]