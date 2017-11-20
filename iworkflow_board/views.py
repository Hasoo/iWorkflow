from django.shortcuts import render

def iw_list(request):
    return render(request, 'board/iw_page.html')