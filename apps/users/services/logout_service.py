from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse


def user_logout_service(request):
    logout(request)
    return redirect(reverse("api-1.0.0:user_login_page"))