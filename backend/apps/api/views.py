from .api import api
from . import schemas, models


# todo: ninja 能否用类进行模块化？类似 django 的 View 类

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@api.get("/hello")
def hello_get(request, name: str = "world"):
    return f"Hello {name}"


@api.post("/hello")
def hello_post(request, data: schemas.Hello):
    return f"Hello {data.name}"


@api.get("/math")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}


@api.get("/me", response={200: schemas.User, 403: schemas.Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user


@api.post("/employees", description="employee")
def create_employee(request, payload: schemas.EmployeeIn):
    employee = models.Employee.objects.create(**payload.dict())
    return {"id": employee.id}
