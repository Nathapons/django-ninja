from ninja import NinjaAPI

from apps.users.api import user_router
from apps.dashboard.api import dashboard_router
from utils.session_auth import CustomSessionAuth


api = NinjaAPI(
    title="Plastic Surgery Clinic Management System", 
    version="1.0.0",
    description="Plastic Surgery Clinic Management System",
    docs_url=None,
)

api.add_router("", user_router)
api.add_router("", dashboard_router, auth=CustomSessionAuth())
