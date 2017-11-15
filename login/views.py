from django.shortcuts import render
from login.forms import LoginForm

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
    else:
        MyLoginForm = LoginForm()

    if username == "admin" and userpass == "admin":
        return render(request, 'login/loggedin.html', {"username": username})
    else:
        return render(request, 'login/login.html', {"loginRet": 0})
