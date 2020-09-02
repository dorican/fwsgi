from cbv import View


class IndexView(View):
    template = 'templates/index.html'
    context = 'IndexView is working'


# class NotFoundView(View):
#     template = 'templates/404.html'
#     context = '404 Page not found'


class AboutView(View):
    template = 'templates/about.html'
    context = 'AboutView is working'


class OtherView(View):
    template = 'templates/other.html'
    context = 'OtherView is working'


class ContactView(View):
    template = 'templates/contacts.html'
    context = 'ContactView is working'


class PostView(View):
    template = 'templates/contacts.html'
    context = 'PostView is working'