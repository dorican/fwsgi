from views import *
from routes import routes


def add_slash(path):
    return path + '/' if not path[-1] == '/' else path


class Application:
    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        path = add_slash(environ['PATH_INFO'])
        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFoundView()
        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return body


application = Application(routes)
