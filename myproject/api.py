from ninja import NinjaAPI

from apps.users.api import router as user_router


api = NinjaAPI(
    title="Hospital Management System", 
    version="1.0.0",
    description="Hospital Management System Web Application",
    docs_url=None,
)

api.add_router("/", user_router)
