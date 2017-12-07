from django.shortcuts import render
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from iwrestful.models import Workflow


class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = ('seq', 'title')

class workflow_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Workflow.objects.filter(status=1)
    serializer_class = WorkflowSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)