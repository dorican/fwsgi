from views import IndexView, AboutView, OtherView, ContactView, PostView

routes = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/other/': OtherView(),
    '/contacts/': ContactView(),
}

post_routes = {
    '/contacts/': PostView(),
}

