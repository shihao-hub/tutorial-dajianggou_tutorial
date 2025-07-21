"""
# Django 实战：使用通用类视图开发任务管理 CRUD 小应用

## 1 需求分析

### 1.1 功能梳理

#### 1.1.1 基础功能

- 创建页面，创建成功预期跳转至列表页面 -> CreateView
- 删除功能，删除成功预期跳转至列表页面 -> DeleteView -> UpdateView
- 更新页面，点击更新按钮跳转至更新页面，更新成功后预期跳转至详情页面
- 详情页面，查看指定 id 数据项的详情 -> DetailView

#### 1.1.2 高级功能



### 1.2 核心业务流程


### 1.3 需求优先级

## 2 库表设计

### 2.1 任务表

#### 2.1.1 核心设计

sqlite sql 如下：
```sql
-- sqlite data type: null, integer, real, text, blob
create table if not exists tasks (
    id integer primary key,
    name text not null, -- 任务名
    status text not null, -- 任务状态
    content text not null, -- 任务内容

    created_time real not null, -- 创建时间
    updated_time real not null, -- 更新时间
    is_deleted integer default false, -- 是否删除
);

create index if not exists idx_name on tasks(name);

```

#### 2.1.2 扩展设计


"""

from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import generic

from . import models, forms


class TestView(generic.View):
    def get(self, request: HttpRequest):
        return HttpResponse(f"method: {request.method} path: {request.path}".encode())

    # def post(self, request: HttpRequest):
    #     return HttpResponse(f"method: {request.method} path: {request.path}".encode())

    def put(self, request: HttpRequest):
        return HttpResponse(f"method: {request.method} path: {request.path}".encode())

    def patch(self, request: HttpRequest):
        return HttpResponse(f"method: {request.method} path: {request.path}".encode())

    def delete(self, request: HttpRequest):
        return HttpResponse(f"method: {request.method} path: {request.path}".encode())


class TaskListView(generic.ListView):
    model = models.Task
    context_object_name = "tasks"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class TaskCreateView(generic.CreateView):
    model = models.Task
    form_class = forms.TaskForm
    success_url = reverse_lazy("tasks:task_list")  # 创建成功后，预期跳转至列表页面

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TaskDeleteView(generic.DeleteView):
    model = models.Task
    success_url = reverse_lazy("tasks:task_list")  # 删除成功后，预期跳转至列表页面

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class TaskUpdateView(generic.UpdateView):
    model = models.Task
    form_class = forms.TaskForm
    success_url = reverse_lazy("tasks:task_list")  # 更新成功后，预期跳转至列表页面

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TaskDetailView(generic.DetailView):
    model = models.Task

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
