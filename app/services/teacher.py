from ..repositories.teacher import (
    add_teacher,
    get_teachers,
    get_teacher,
    update_teacher as _update_teacher,
    delete_teacher as _delete_teacher,
)


def create_teacher(name, age, email, department, employee_id):
    add_teacher(name, age, email, department, employee_id)


def get_all_teachers():
    return get_teachers()


def get_teacher_by_id(teacher_id):
    return get_teacher(teacher_id)


def update_teacher(teacher_id, name, age, email, department, employee_id):
    _update_teacher(teacher_id, name, age, email, department, employee_id)


def delete_teacher(teacher_id):
    _delete_teacher(teacher_id)
