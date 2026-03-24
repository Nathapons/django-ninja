from django.shortcuts import render
from ninja import Router


user_router = Router()

@user_router.get('/view')
def user_view(request):
    return render(request, 'login.html')

@user_router.post('/login')
def user_login(request):
    return render(request, 'login.html')

@user_router.api_operation(['GET', 'POST'], '/register')
def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        return render(request, 'register.html')