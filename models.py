from orm.unitofwork import DomainObject
from reusepatterns.prototypes import PrototypeMixin


class User:
    def __init__(self, name):
        self.name = name


class Teacher(User):
    pass


class Student(User, DomainObject):

    def __init__(self, name):
        self.courses = []
        super().__init__(name)


class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher
    }

    @classmethod
    def create(cls, type_, name):
        return cls.types[type_](name)


class Course(PrototypeMixin):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)
        student.courses.append(self)


class InteractiveCourse(Course):
    pass


class RecordCourse(Course):
    pass


class CourseFactory:
    types = {
        'interactive': InteractiveCourse,
        'record': RecordCourse
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class Category(DomainObject):
    # реестр
    # auto_id = 0

    def __init__(self, name):
        # self.id = Category.auto_id
        # Category.auto_id += 1
        self.name = name
        # self.category = category
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result

    @classmethod
    def create(cls, name):
        return cls.__class__(name)


class TrainingSite:
    # Интерфейс
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    def create_user(self, type_, name):
        return UserFactory.create(type_, name)

    def create_category(self, type_, name):
        # print(self, name)
        # return Category(name)
        return Category(name)

    def find_category_by_id(self, id):
        for item in self.categories:
            print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'Нет категории с id = {id}')

    def create_course(self, type_, name, category):
        return CourseFactory.create(type_, name, category)

    def get_course(self, name) -> Course:
        for item in self.courses:
            if item.name == name:
                return item

    def get_student(self, name) -> Student:
        for item in self.students:
            if item.name == name:
                return item