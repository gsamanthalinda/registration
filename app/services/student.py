from ..repositories.student import (
    add_student,
    get_students,
    get_student,
    update_student as _update_student,
    delete_student as _delete_student,
)


def register_student(name, age, email, country, id_number):
    add_student(name, age, email, country, id_number)


def get_all_students():
    return get_students()


def get_student_by_id(student_id):
    return get_student(student_id)


def update_student(student_id, name, age, email, country, id_number):
    _update_student(student_id, name, age, email, country, id_number)


def delete_student(student_id):
    _delete_student(student_id)
