"""Сервис для работы с данными и выполнения запросов"""
from collections import defaultdict

class DataService:
    """Сервис для работы с данными кафедр и студенческих групп"""
    
    def __init__(self, departments, student_groups, group_departments):
        """
        Инициализация сервиса с данными
        
        Args:
            departments: список кафедр
            student_groups: список студенческих групп
            group_departments: список связей многие-ко-многим
        """
        self.departments = departments
        self.student_groups = student_groups
        self.group_departments = group_departments
        
        # Создаем словари для быстрого доступа
        self.group_dict = {group.id: group for group in student_groups}
        self.department_dict = {dept.id: dept for dept in departments}
    
    def get_departments_starting_with(self, letter):
        """
        Получить кафедры, название которых начинается с заданной буквы
        
        Args:
            letter: буква для поиска
            
        Returns:
            Список кафедр, удовлетворяющих условию
        """
        return [dept for dept in self.departments if dept.name.startswith(letter)]
    
    def get_groups_by_department_id(self, department_id):
        """
        Получить студенческие группы по ID кафедры
        
        Args:
            department_id: ID кафедры
            
        Returns:
            Список студенческих групп, относящихся к кафедре
        """
        return [group for group in self.student_groups if group.department_id == department_id]
    
    def get_departments_with_max_students(self):
        """
        Получить кафедры с максимальным количеством студентов в группах
        
        Returns:
            Список кортежей (название_кафедры, максимальное_количество_студентов),
            отсортированный по убыванию количества студентов
        """
        # Группируем студенческие группы по кафедрам
        groups_by_department = defaultdict(list)
        for group in self.student_groups:
            groups_by_department[group.department_id].append(group)
        
        # Находим максимальное количество студентов для каждой кафедры
        department_max_students = []
        for dept_id, dept_groups in groups_by_department.items():
            if dept_groups:
                max_students = max(group.student_count for group in dept_groups)
                dept_name = next(dept.name for dept in self.departments if dept.id == dept_id)
                department_max_students.append((dept_name, max_students))
        
        # Сортируем по максимальному количеству студентов (по убыванию)
        department_max_students.sort(key=lambda x: x[1], reverse=True)
        
        return department_max_students
    
    def get_group_department_connections(self):
        """
        Получить все связи группы-кафедры, отсортированные по кафедрам
        
        Returns:
            Словарь, где ключ - кафедра, значение - список связанных групп
        """
        connections_by_department = defaultdict(list)
        
        for gd in self.group_departments:
            group = self.group_dict.get(gd.group_id)
            department = self.department_dict.get(gd.department_id)
            if group and department:
                connections_by_department[department].append(group)
        
        # Сортируем кафедры по названию
        sorted_connections = {}
        for department in sorted(connections_by_department.keys(), key=lambda x: x.name):
            sorted_connections[department] = connections_by_department[department]
        
        return sorted_connections