from datetime import date

from ninja import Schema


class Error(Schema):
    message: str


class Hello(Schema):
    name: str = "world"


class User(Schema):
    username: str
    is_authenticated: bool
    # 未经过身份验证的用户没有以下字段，因此提供默认值。
    email: str = None
    first_name: str = None
    last_name: str = None


class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None
