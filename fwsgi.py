from cbv import View
from routes import routes, post_routes


def parse_input_data(data: str):
    result = {}
    if data:
        # делим параметры через &
        params = data.split('&')
        for item in params:
            # делим ключ и значение через =
            k, v = item.split('=')
            result[k] = v
    return result


def get_wsgi_input_data(env) -> bytes:
    # получаем длину тела
    content_length_data = env.get('CONTENT_LENGTH')
    print(f'content_length_data - {content_length_data}')
    # приводим к int
    content_length = int(content_length_data) if content_length_data else 0
    # считываем данные если они есть
    data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
    return data


def parse_wsgi_input_data(data: bytes) -> dict:
    result = {}
    if data:
        # декодируем данные
        data_str = data.decode(encoding='utf-8')
        # собираем их в словарь
        result = parse_input_data(data_str)
    return result


class Application:
    def __init__(self, routes, post_routes):
        self.routes = routes
        self.post_routes = post_routes

    def __call__(self, environ, start_response):
        method = environ['REQUEST_METHOD']
        print(f'method - {method}')
        path = self.add_slash(environ['PATH_INFO'])
        request = {}
        if method == 'GET':
            if path in self.routes:
                view = self.routes[path]
            else:
                view = NotFoundView()
            query_string = environ['QUERY_STRING']
            request = parse_input_data(query_string)
            print(request)
        elif method == 'POST':
            data = get_wsgi_input_data(environ)
            data = parse_wsgi_input_data(data)
            print(f'data - {data}')
            if path in self.routes:
                view = self.post_routes[path]
            else:
                view = NotFoundView()
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body

    def add_slash(self, path):
        return path + '/' if not path[-1] == '/' else path


class NotFoundView(View):
    template = 'templates/404.html'
    context = '404 Page not found'


application = Application(routes, post_routes)
