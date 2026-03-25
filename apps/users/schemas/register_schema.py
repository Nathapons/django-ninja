from ninja import Schema
from pydantic import root_validator
from django.contrib.auth.models import User


class RegisterUserSchema(Schema):
    first_name: str
    last_name: str
    username: str
    password: str
    confirm_password: str

    @root_validator
    def check_passwords_match(cls, values):
        if values.get('password') != values.get('confirm_password'):
            raise ValueError('Passwords do not match')

        if User.objects.filter(username=values.get('username')).exists():
            raise ValueError('Username already exists')
        
        return values