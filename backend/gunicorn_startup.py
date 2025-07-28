"""
# Gunicorn（仅支持 Linux 和 macOS）

Gunicorn（Green Unicorn）是一个用于 Python WSGI 应用程序的高性能、轻量级 HTTP 服务器。
它能够将 Python 应用程序部署在生产环境中，特别适合与 Flask、Django 等 Web 框架配合使用。
它基于 pre-fork worker 模式，能够处理高并发，简单且易于扩展。

## Gunicorn 与 Django 应用整合

```bash
# 一般 django 项目结构：{project_name}/{project_name}/wsgi.py，其中第一个 {project_name} 是项目 Sources Root，application 是 WSGI 应用的入口。
gunicorn {project_name}.wsgi:application

# 指定 worker 数量和监听端口
gunicorn -w 3 -b 127.0.0.1:9999 {project_name}.wsgi:application
```

## Gunicorn 的配置
1. 指定工作进程数量

```bash
gunicorn -w 4 app:app
```

-w 参数设置 worker 进程的数量。通常，建议的 worker 数量为 CPU 核心数的 2 倍加 1。

2. 指定绑定的 IP 和端口

```bash
gunicorn -b 0.0.0.0:8000 app:app
```

-b 参数指定 Gunicorn 监听的 IP 地址和端口。

3. 使用配置文件

你可以将配置项写入一个配置文件中，比如 gunicorn.conf.py，然后通过命令加载它：

```bash
gunicorn -c gunicorn.conf.py app:app
```

示例 gunicorn.conf.py 文件内容：

```python
workers = 4
bind = '0.0.0.0:8000'
loglevel = 'debug'
```

## [Gunicorn 的替代品](https://deepinout.com/python/python-qa/509_python_does_gunicorn_run_on_windows.html)

如果您不想使用 WSL 或希望在 Windows 上运行纯粹的 Python Web 服务器，您可以考虑使用 Gunicorn 的某些替代品。

### 使用 WSL（Windows Subsystem for Linux）

```bash
wsl --install / wsl --install -d Ubuntu
```

详细内容还得仔细研究...



### Waitress 服务器

Waitress 是一个纯 Python 编写的 WSGI 服务器，它可以在 Windows 上运行，并且与 Gunicorn 几乎相同的性能。

```bash
pip install waitress

waitress-serve --call app:app

waitress-serve --port=8000 {project_name}.wsgi:application
```

### 其他替代品

除了 Waitress 服务器之外，还有其他一些纯 Python 编写的 WSGI 服务器可以在 Windows 上运行，例如 Bjoern、gevent 等。
这些替代品都有自己的优点和适用场景，您可以根据自己的需求进行选择。

## 参考资料

1. https://buffaloboyhlh.github.io/it-handbooks/%E6%9C%8D%E5%8A%A1%E5%99%A8/gunicorn/basic/
2. https://docs.gunicorn.org/en/stable/

"""