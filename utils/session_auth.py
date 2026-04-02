from django.shortcuts import redirect
from django.urls import reverse

from ninja.security.session import SessionAuth


class CustomSessionAuth(SessionAuth):
    
    def authenticate(self, request, key):
        user = super().authenticate(request, key)
        if user is None:
            return redirect(reverse("api-1.0.0:user_unauthorized_page"))
        return user
