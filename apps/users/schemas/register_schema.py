from ninja import Schema


class RegisterUserSchema(Schema):
    first_name: str
    last_name: str
    username: str
    password: str
    confirm_password: str
