
# Запуск
# uwsgi --http :8000 --wsgi-file main.py

from wavy import render
from models import TrainingSite
from logger import Logger, debug
from wavy.cbv import CreateView

site = TrainingSite()
logger = Logger('main')


@debug
def main_view(request):
    logger.log('Главная страница')
    secret = request.get('secret_key', None)
    # Используем шаблонизатор
    courses = site.courses
    categories = site.categories
    students = site.students
    return '200 OK', render('index.html', categories=categories, courses=courses, students=students)


@debug
def create_category(request):
    logger.log('Создание категории')
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        category_id = data.get('category_id')
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))
        new_category = site.create_category(name, category)
        site.categories.append(new_category)
        return '200 OK', render('create_category.html')
    else:
        categories = site.categories
        return '200 OK', render('create_category.html', categories=categories)


# def about_view(request):
#     # Просто возвращаем текст
#     return '200 OK', "About"
@debug
def create_course(request):
    logger.log('Создание курса')
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        category_id = data.get('category_id')
        if category_id:
            category = site.find_category_by_id(int(category_id))
            course = site.create_course('record', name, category)
            site.courses.append(course)
        return '200 OK', render('create_course.html')
    else:
        categories = site.categories
        return '200 OK', render('create_course.html', categories=categories)


@debug
def contact_view(request):
    logger.log('Страница контактов')
    # Проверка метода запроса
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
        return '200 OK', render('contact.html')
    else:
        return '200 OK', render('contact.html')


class StudentCreateView(CreateView):
    template_name = 'create_student.html'

    def create_obj(self, data: dict):
        name = data['name']
        new_obj = site.create_user('student', name)
        site.students.append(new_obj)


class AddStudentByCourseCreateView(CreateView):
    template_name = 'add_student.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = site.courses
        context['students'] = site.students
        return context

    def create_obj(self, data: dict):
        # breakpoint()
        course_name = data['course_name']
        course = site.get_course(course_name)
        student_name = data['student_name']
        student = site.get_student(student_name)
        course.add_student(student)
