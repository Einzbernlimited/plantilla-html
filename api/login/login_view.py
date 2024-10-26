from django.shortcuts import render, redirect

def login_view(request):
    template_name ="auth-login.html"

    return render(request,template_name)
