from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse


def render_user_page_service(request):
    return render(request, 'login.html')

def user_login_service(request, username, password, remember):
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        if remember:
            # Remember in 8 hrs
            request.session.set_expiry(8 * 60 * 60)
        else:
            # Session expires when browser is closed
            request.session.set_expiry(0)

        success_html = f"""
        <div class="flex items-center gap-3 p-4 rounded-lg bg-green-50 border border-green-200 text-green-800 text-sm font-medium">
            <span class="material-symbols-outlined text-green-600 text-xl">check_circle</span>
            <span>Login successful! Redirecting…</span>
        </div>
        <script>setTimeout(() => {{ window.location.href = '{reverse("api-1.0.0:get_dashboard_page")}'; }}, 1000);</script>
        """
        response = HttpResponse(success_html)
        return response
    else:
        error_html = """
        <div class="flex items-center gap-3 p-4 rounded-lg bg-red-50 border border-red-200 text-red-800 text-sm font-medium">
            <span class="material-symbols-outlined text-red-600 text-xl">error</span>
            <span>Invalid username or password. Please try again.</span>
        </div>
        """
        return HttpResponse(error_html, status=401)
