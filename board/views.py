from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy, reverse
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
    fields = ['status', 'title', 'desc', 'attach', 'secret_key']

    def form_valid(self, form):
        form.instance.worker = self.request.session['member_id']
        return super(WorkflowCreate, self).form_valid(form)

class WorkflowUpdate(UpdateView):

    model = Workflow
    fields = ['status', 'title', 'desc', 'attach', 'secret_key']

    def get_success_url(self):
        return reverse('workflow-detail', args=(self.object.pk,))