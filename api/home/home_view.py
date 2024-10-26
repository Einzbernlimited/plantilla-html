from django.shortcuts import render
#crear vista

def home_view(request):
    template_name ="index.html"

    return render(request,template_name)