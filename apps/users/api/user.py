from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from ninja import Router


user_router = Router()


@user_router.api_operation(['GET', 'POST'], '/login')
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

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
    elif request.method == 'POST':
        return render(request, 'register.html')