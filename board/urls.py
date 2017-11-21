from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.WorkflowListView.as_view(), name='workflow-list'),
]