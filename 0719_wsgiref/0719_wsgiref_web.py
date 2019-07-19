# wsgiref 和 apache Nginx 一樣的web服務器
import os, time
from wsgiref.simple_server import make_server


def index(req):
    with open(os.path.dirname(__file__) + "/index.html", "rb") as f:
        data = f.read()
    return data


def login(req):
    with open(os.path.dirname(__file__) + "/login.html", "rb") as f:
        data = f.read()
    return data


def login_to(req):
    print(req["QUERY_STRING"])
    return b'welcome'


def show_time(req):
    timea = time.ctime()
    with open(os.path.dirname(__file__) + "/show_timea.html", "rb") as f:
        data = f.read()
    data = data.decode()
    data = data.replace("{{time}}", str(timea))  # 自己寫一個 模板渲染 是非常low的
    return data.encode("utf8")


def sign(req):
    return b'hello'


def router(req):  # 控制器
    url_patterns = [
        ("/login", login),
        ("/login_to", login_to),
        ("/sign", sign),
        ("/index", index),
        ("/show_time", show_time),

    ]
    return url_patterns


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']
    url_patterns = router(environ)
    print(path)
    func = None
    for item in url_patterns:
        if path in item:
            func = item[1]
            break
    if func:
        return [func(environ)]
    else:
        return [b'<h1>my 404</h1>']


httpd = make_server('', 8080, application)

print('server HTTP on 8080')

httpd.serve_forever()
