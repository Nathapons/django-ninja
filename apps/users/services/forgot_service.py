from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def render_forgot_password_page_service(request):
    return render(request, 'forgot_password.html')


_FORGOT_SUCCESS_HTML = """
    <div class="flex items-center gap-3 p-4 rounded-lg bg-green-50 border border-green-200 text-green-800 text-sm font-medium">
        <span class="material-symbols-outlined text-green-600 text-xl">check_circle</span>
        <span>If this email is registered, a password reset link has been sent.</span>
    </div>
"""


def forgot_password_service(email):
    user = User.objects.filter(email=email).first()
    if user:
        email_detail = render_to_string('forgot_password_email.html', {'user': user})
        send_mail(
            subject='Password Reset',
            message='Please enable HTML to view this email.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            html_message=email_detail,
            fail_silently=True,
        )
    return HttpResponse(_FORGOT_SUCCESS_HTML)    