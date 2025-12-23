"""Модели данных для системы кафедр и студенческих групп"""

class Department:
    """Класс Кафедра"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return f"Department(id={self.id}, name='{self.name}')"

class StudentGroup:
    """Класс Студенческая группа"""
    def __init__(self, id, group_name, student_count, department_id):
        self.id = id
        self.group_name = group_name
        self.student_count = student_count
        self.department_id = department_id
    
    def __repr__(self):
        return f"StudentGroup(id={self.id}, group_name='{self.group_name}', student_count={self.student_count}, department_id={self.department_id})"

class GroupDepartment:
    """Класс для связи многие-ко-многим между Студенческой группой и Кафедрой"""
    def __init__(self, group_id, department_id):
        self.group_id = group_id
        self.department_id = department_id
    
    def __repr__(self):
        return f"GroupDepartment(group_id={self.group_id}, department_id={self.department_id})"