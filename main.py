# Запуск
# uwsgi --http :8000 --wsgi-file main.py

from wavy import Application
import views
from views import StudentCreateView, AddStudentByCourseCreateView, IndexListView

urlpatterns = {
    '/': IndexListView(),
    '/create-category/': views.create_category,
    '/create-student/': StudentCreateView(),
    '/add-student/': AddStudentByCourseCreateView(),
    '/create-course/': views.create_course,
    '/contact/': views.contact_view
}


def secret_controller(request):
    # пример Front Controller
    request['secret_key'] = 'SECRET'


front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)
