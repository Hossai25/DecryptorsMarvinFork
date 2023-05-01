from TAScheduler.models import Course as CourseModel
from classes import account


def create_course(name: str):
    if get_course_model(name) is None:
        new_course_model = CourseModel.objects.create(course_name=name)
        return Course(new_course_model)
    else:
        return None


def delete_course(primary_key):
    pass


def get_course_model(name_attempt):
    try:
        course_model = CourseModel.objects.get(course_name=name_attempt)
        return course_model
    except CourseModel.DoesNotExist:
        return None


def get_course(name_attempt):
    try:
        course_model = CourseModel.objects.get(course_name=name_attempt)
        course = Course(course_model)
        return course
    except CourseModel.DoesNotExist:
        return None


def get_course_by_id(course_id):
    try:
        course_model = CourseModel.objects.get(id=course_id)
        course = Course(course_model)
        return course
    except CourseModel.DoesNotExist:
        return None


def course_list():
    courses = CourseModel.objects.all()
    course_objects = [Course(course_model) for course_model in courses]
    return course_objects


class Course:
    def __init__(self, course_model: CourseModel):
        self.course_model = course_model

    def get_course_name(self):
        return self.course_model.course_name

    def set_course_name(self, new_course_name: str):
        self.course_model.course_name = new_course_name
        self.course_model.save()

    def get_instructor(self):
        instructor_id = self.course_model.instructor_id
        instructor = account.get_account_by_id(instructor_id)
        return instructor

    def set_instructor(self, instructor: type[account.Account]):
        self.course_model.instructor_id = instructor
        self.course_model.save()

    def get_primary_key(self):
        return self.course_model.pk
