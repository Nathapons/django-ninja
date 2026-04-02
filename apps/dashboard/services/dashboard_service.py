from django.shortcuts import render, redirect
from django.urls import reverse


def render_dashboard_page_service(request):
    if not request.user.is_authenticated:
        return redirect(reverse("api-1.0.0:user_unauthorized_page"))
    return render(request, "dashboard.html")
