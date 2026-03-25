from django.http import HttpResponse
from django.shortcuts import render
from ninja import Router, Form

from apps.users.services.login_service import render_user_page_service, \
    user_login_service
from apps.users.schemas.login_schema import LoginUserSchema
from apps.users.schemas.forgot_password_schema import ForgotPasswordSchema
from apps.users.services.forgot_service import render_forgot_password_page_service, \
    forgot_password_service


user_router = Router()

@user_router.get('/', url_name='user_login_page')
def user_login_view(request):
    return render_user_page_service(request)

@user_router.post('/login', url_name='user_login')
def user_login(request, data: LoginUserSchema = Form()):
    return user_login_service(request, data.username, data.password, data.remember)

@user_router.api_operation(['GET', 'POST'], '/register')
def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    
    # HTMX POST logic
    from django.contrib.auth.models import User
    
    first_name = request.POST.get('first_name', '').strip()
    last_name = request.POST.get('last_name', '').strip()
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '').strip()
    confirm_password = request.POST.get('confirm_password', '').strip()
    
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
        user = User.objects.create_user(
            username=username, 
            password=password, 
            first_name=first_name, 
            last_name=last_name,
            is_active=False,
            is_superuser=False,
        )
        user.set_password(password)
        user.save()
        # Success fragment
        success_html = """
        <div class="flex items-center gap-3 p-4 rounded-lg bg-green-50 border border-green-200 text-green-800 text-sm font-medium">
            <span class="material-symbols-outlined text-green-600 text-xl">check_circle</span>
            <span>Registration successful! Redirecting to login...</span>
        </div>
        <script>setTimeout(() => { window.location.href = '/'; }, 1500);</script>
        """
        return HttpResponse(success_html)
    except Exception as e:
        return HttpResponse(f"""
            <div class="flex items-center gap-3 p-4 rounded-lg bg-red-50 border border-red-200 text-red-800 text-sm font-medium">
                <span class="material-symbols-outlined text-red-600 text-xl">error</span>
                <span>An error occurred: {str(e)}</span>
            </div>
        """, status=500)


@user_router.get('/forgot-password', url_name='user_forgot_password_page')
def user_forgot_password_view(request):
    return render_forgot_password_page_service(request)

@user_router.post('/forgot-password', url_name='user_forgot_password')
def user_forgot_password(request, data: ForgotPasswordSchema = Form()):
    return forgot_password_service(request, data.email)