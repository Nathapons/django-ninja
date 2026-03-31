from ninja import Router
from apps.dashboard.services.dashboard_service import render_dashboard_page_service


dashboard_router = Router()


@dashboard_router.get("dashboard/", url_name="get_dashboard_page")
def dashboard(request):
    return render_dashboard_page_service(request)