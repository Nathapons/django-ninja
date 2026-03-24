from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from ninja import Router


user_router = Router()

@user_router.api_operation(['GET'], '/')
def user_login_view(request):
    return render(request, 'login.html')

@user_router.api_operation(['POST'], '/login')
def user_login(request):
    # HTMX POST — authenticate and return an HTML fragment
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '').strip()

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Success fragment: HTMX will inject this into #login-response
        # You can also add hx-redirect here if you want a full page redirect
        success_html = """
        <div class="flex items-center gap-3 p-4 rounded-lg bg-green-50 border border-green-200 text-green-800 text-sm font-medium">
            <span class="material-symbols-outlined text-green-600 text-xl">check_circle</span>
            <span>Login successful! Redirecting…</span>
        </div>
        <script>setTimeout(() => { window.location.href = '/'; }, 1000);</script>
        """
        response = HttpResponse(success_html)
        return response
    else:
        # Error fragment: HTMX will inject this into #login-response
        error_html = """
        <div class="flex items-center gap-3 p-4 rounded-lg bg-red-50 border border-red-200 text-red-800 text-sm font-medium">
            <span class="material-symbols-outlined text-red-600 text-xl">error</span>
            <span>Invalid username or password. Please try again.</span>
        </div>
        """
        return HttpResponse(error_html, status=401)

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
            last_name=last_name
        )
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