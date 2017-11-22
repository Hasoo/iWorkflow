from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.WorkflowListView.as_view(), name='workflow-list'),
    url(r'^workflow/(?P<pk>[0-9]+)/$', views.WorkflowDetailView.as_view(), name='workflow-detail'),
    url(r'^workflow/create/$', views.WorkflowCreate.as_view(), name='workflow-create'),
]