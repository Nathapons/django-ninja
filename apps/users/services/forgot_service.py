from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def render_forgot_password_page_service(request):
    return render(request, 'forgot_password.html')


def forgot_password_service(request, username):
    user = User.objects.filter(username=username).first()
    if not user:
        return HttpResponse("""
            <div class="flex items-center gap-3 p-4 rounded-lg bg-red-50 border border-red-200 text-red-800 text-sm font-medium">
                <span class="material-symbols-outlined text-red-600 text-xl">error</span>
                <span>Username not found.</span>
            </div>
        """, status=400)
    else:
        return HttpResponse("""
            <div class="flex items-center gap-3 p-4 rounded-lg bg-green-50 border border-green-200 text-green-800 text-sm font-medium">
                <span class="material-symbols-outlined text-green-600 text-xl">check_circle</span>
                <span>Username found.</span>
            </div>
        """)
    