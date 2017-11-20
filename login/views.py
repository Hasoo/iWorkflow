from django.shortcuts import render
from login.forms import LoginForm
from login.models import LoginAdmin

def login(request):
    return render(request, 'login/login.html', {"loginRet": 1})

def loginCheck(request):
    username = ""
    userpass = ""

    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['user_id']
            userpass = MyLoginForm.cleaned_data['user_pass']

        loginAdmin = LoginAdmin.objects.filter(user_id__exact=username).values_list('user_id', 'user_pass')
        if 0 != len(loginAdmin):
            if userpass == loginAdmin[0][1]:
                request.session['member_id'] = username
                return render(request, 'board/iw_page.html', {"username": username})
                #return render(request, 'login/loggedin.html', {"username": username})

        return render(request, 'login/login.html', {"loginRet": 0})
    else:
        MyLoginForm = LoginForm()

    return render(request, 'login/login.html', {"loginRet": 1})

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass

    return render(request, 'login/login.html', {"loginRet": 0})