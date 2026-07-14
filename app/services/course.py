from ..repositories.course import (
    add_course,
    get_courses,
    get_course,
    update_course as _update_course,
    delete_course as _delete_course,
)


def create_course(title, description, credits, teacher_id, course_code):
    add_course(title, description, credits, teacher_id, course_code)


def get_all_courses():
    return get_courses()


def get_course_by_id(course_id):
    return get_course(course_id)


def update_course(course_id, title, description, credits, teacher_id, course_code):
    _update_course(course_id, title, description, credits, teacher_id, course_code)


def delete_course(course_id):
    _delete_course(course_id)
