from ninja import Schema

class LoginUserSchema(Schema):
    username: str
    password: str
    remember: bool = False
