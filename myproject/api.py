from ninja import NinjaAPI
from ninja.security import django_auth

from apps.users.api import user_router
from apps.dashboard.api import dashboard_router


api = NinjaAPI(
    title="Hospital Management System", 
    version="1.0.0",
    description="Hospital Management System Web Application",
    docs_url=None,
)

api.add_router("", user_router)
api.add_router("", dashboard_router, auth=django_auth)
