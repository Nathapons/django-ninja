from ninja import Router, Form

from apps.users.services.login_service import render_user_page_service, \
    user_login_service, render_unauthorized_page_service
from apps.users.services.register_service import render_register_page_service, \
    user_register_service
from apps.users.services.forgot_service import render_forgot_password_page_service, \
    forgot_password_service
from apps.users.services.logout_service import user_logout_service
from apps.users.schemas.login_schema import LoginUserSchema
from apps.users.schemas.forgot_password_schema import ForgotPasswordSchema
from apps.users.schemas.register_schema import RegisterUserSchema


user_router = Router()

@user_router.get('/', url_name='user_login_page')
def user_login_view(request):
    return render_user_page_service(request)

@user_router.get('/unauthorized', url_name='user_unauthorized_page')
def user_unauthorized_view(request):
    return render_unauthorized_page_service(request)

@user_router.post('/login', url_name='user_login')
def user_login(request, data: LoginUserSchema = Form()):
    return user_login_service(request, data.username, data.password, data.remember)

@user_router.get('/register', url_name='user_register_page')
def register_page_view(request):
    return render_register_page_service(request)

@user_router.post('/register', url_name='user_register')
def register_view(request, data: RegisterUserSchema = Form()):
    return user_register_service(
        data.username, data.password, data.confirm_password, data.first_name, data.last_name
    )

@user_router.get('/forgot-password', url_name='user_forgot_password_page')
def user_forgot_password_view(request):
    return render_forgot_password_page_service(request)

@user_router.post('/forgot-password', url_name='user_forgot_password')
def user_forgot_password(request, data: ForgotPasswordSchema = Form()):
    return forgot_password_service(data.email)

@user_router.get('/logout', url_name='user_logout')
def user_logout(request):
    return user_logout_service(request)