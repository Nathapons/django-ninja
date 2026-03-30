from ninja.security.session import SessionAuth


class CustomSessionAuth(SessionAuth):
    
    def authenticate(self, request, key):
        user = super().authenticate(request, key)
        if user is None:
            return None
        return user
