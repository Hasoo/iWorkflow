from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from board.models import Workflow

class WorkflowListView(ListView):

    model = Workflow

class WorkflowDetailView(DetailView):

    model = Workflow