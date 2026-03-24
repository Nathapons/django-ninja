from django.shortcuts import render

def get_login_page(request):
    return render(request, 'login.html')