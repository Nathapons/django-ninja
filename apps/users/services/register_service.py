from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def render_register_page_service(request):
    return render(request, 'register.html')

def user_register_service(username, password, confirm_password, first_name, last_name):
    if password != confirm_password:
        return HttpResponse("""
            <div class="flex items-center gap-3 p-4 rounded-lg bg-red-50 border border-red-200 text-red-800 text-sm font-medium">
                <span class="material-symbols-outlined text-red-600 text-xl">error</span>
                <span>Passwords do not match.</span>
            </div>
        """, status=400)

    if User.objects.filter(username=username).exists():
        return HttpResponse("""
            <div class="flex items-center gap-3 p-4 rounded-lg bg-red-50 border border-red-200 text-red-800 text-sm font-medium">
                <span class="material-symbols-outlined text-red-600 text-xl">error</span>
                <span>Username already exists.</span>
            </div>
        """, status=400)

    try:
        User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_active=False,
        )
        success_html = """
        <div class="flex items-center gap-3 p-4 rounded-lg bg-green-50 border border-green-200 text-green-800 text-sm font-medium">
            <span class="material-symbols-outlined text-green-600 text-xl">check_circle</span>
            <span>Registration successful! Redirecting to login...</span>
        </div>
        <script>setTimeout(() => { window.location.href = '/'; }, 1500);</script>
        """
        return HttpResponse(success_html)
    except Exception:
        return HttpResponse("""
            <div class="flex items-center gap-3 p-4 rounded-lg bg-red-50 border border-red-200 text-red-800 text-sm font-medium">
                <span class="material-symbols-outlined text-red-600 text-xl">error</span>
                <span>An error occurred. Please try again.</span>
            </div>
        """, status=500)