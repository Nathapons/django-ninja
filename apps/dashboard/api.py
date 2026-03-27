from django.shortcuts import render
from ninja import Router, Form
from django.http import HttpResponse


dashboard_router = Router()


@dashboard_router.get("dashboard/", url_name="get_dashboard_page")
def dashboard(request):
    return HttpResponse("<h1>Dashboard</h1>")