from ninja import ModelSchema
from django.contrib.auth.models import User


class LoginUserModelSchema(ModelSchema):
    remember: bool = False

    class Meta:
        model = User
        fields = ['username', 'password']