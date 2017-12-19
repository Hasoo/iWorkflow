from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from board.models import Workflow
from fcm.utils import get_device_model

class WorkflowListView(ListView):

    model = Workflow
    paginate_by = 3
    ordering = ['-seq']

    def dispatch(self, *args, **kwargs):
        if None == self.request.session.get('member_id'):
            return HttpResponse('401 Unauthorized', status=401)
            #return redirect('login')
        return super(WorkflowListView, self).dispatch(*args, **kwargs)

class WorkflowDetailView(DetailView):

    model = Workflow

    def dispatch(self, *args, **kwargs):
        if None == self.request.session.get('member_id'):
            return HttpResponse('401 Unauthorized', status=401)
            #return redirect('login')
        return super(WorkflowDetailView, self).dispatch(*args, **kwargs)

class WorkflowCreate(CreateView):

    model = Workflow
    success_url = reverse_lazy('workflow-list')
    fields = ['status', 'title', 'desc', 'attach', 'secret_key']

    def dispatch(self, *args, **kwargs):
        if None == self.request.session.get('member_id'):
            return HttpResponse('401 Unauthorized', status=401)
            #return redirect('login')
        return super(WorkflowCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.worker = self.request.session['member_id']
        response = super(WorkflowCreate, self).form_valid(form)
        Device = get_device_model()
        Device.objects.all().send_message({'message':form.cleaned_data['title']})
        return response
    """
    def form_valid(self, form):
        form.instance.worker = self.request.session['member_id']
        return super(WorkflowCreate, self).form_valid(form)
    """

class WorkflowUpdate(UpdateView):

    model = Workflow
    fields = ['status', 'title', 'desc', 'attach', 'secret_key']

    def dispatch(self, *args, **kwargs):
        if None == self.request.session.get('member_id'):
            return HttpResponse('401 Unauthorized', status=401)
            #return redirect('login')
        return super(WorkflowUpdate, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('workflow-detail', args=(self.object.pk,))