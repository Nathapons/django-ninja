from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail


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
        if user.email:
            email_detail = render_to_string('forgot_password_email.html', {'user': user})
            send_mail(
                subject='Password Reset',
                message='Please enable HTML to view this email.',
                from_email=None,
                recipient_list=[user.email],
                html_message=email_detail,
                fail_silently=True,
            )
            
        return HttpResponse("""
            <div class="flex items-center gap-3 p-4 rounded-lg bg-green-50 border border-green-200 text-green-800 text-sm font-medium">
                <span class="material-symbols-outlined text-green-600 text-xl">check_circle</span>
                <span>Password reset link has been sent to your email.</span>
            </div>
        """)    