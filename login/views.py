from django.shortcuts import render
from login.forms import LoginForm
from login.models import LoginAdmin

def login(request):
    return render(request, 'login/login.html', {"loginRet": 1})

def loginCheck(request):
    username = "not logged in"
    userpass = "not logged in"

    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['user_id']
            userpass = MyLoginForm.cleaned_data['user_pass']

        loginAdmin = LoginAdmin.objects.filter(user_id__exact=username).values_list('user_id', 'user_pass')
        if 0 != len(loginAdmin):
            if userpass == loginAdmin[0][1]:
                return render(request, 'login/loggedin.html', {"username": username})
    else:
        MyLoginForm = LoginForm()

    return render(request, 'login/login.html', {"loginRet": 0})