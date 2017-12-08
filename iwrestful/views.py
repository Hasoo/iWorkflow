from django.shortcuts import render
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView, UpdateAPIView

from iwrestful.models import Workflow


class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = "__all__"
        #fields = ('seq', 'title')

class WorkflowListAPI(GenericAPIView, mixins.ListModelMixin):
    queryset = Workflow.objects.filter(status=1)
    serializer_class = WorkflowSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class WorkflowUpdateAPI(UpdateAPIView):
    partial=True
    queryset = Workflow.objects.all()    
    serializer_class = WorkflowSerializer
