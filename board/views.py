from django.shortcuts import render
from django.views.generic.list import ListView
from board.models import Workflow

def iw_list(request):
    return render(request, 'board/iw_page.html')

class WorkflowListView(ListView):

    model = Workflow

    def get_context_data(self, **kwargs):
        context = super(WorkflowListView, self).get_context_data(**kwargs)
        return context