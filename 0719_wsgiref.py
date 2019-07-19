# wsgiref 和 apache Nginx 一樣的web服務器

from wsgiref.simple_server import make_server


def foo():
    with open("0719_index.html", "rb") as f:
        data = f.read()
    return data


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    text1 = environ['PATH_INFO'].replace('/', '')
    if text1 == 'alex':
        return [foo()]


httpd = make_server('', 8080, application)

print('server HTTP on 8080')

httpd.serve_forever()
