from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from board.models import Workflow

class WorkflowListView(ListView):

    model = Workflow
    paginate_by = 3
    ordering = ['-seq']

class WorkflowDetailView(DetailView):

    model = Workflow

class WorkflowCreate(CreateView):

    model = Workflow
    success_url = reverse_lazy('workflow-list')
    fields = ['title', 'desc', 'secret_key']
