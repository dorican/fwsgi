from views import IndexView, AboutView, OtherView

routes = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/other/': OtherView(),
}
