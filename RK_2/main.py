"""Основная программа для демонстрации работы системы"""
from models import Department, StudentGroup, GroupDepartment
from data_service import DataService

def create_test_data():
    """
    Создание тестовых данных
    
    Returns:
        Кортеж (departments, student_groups, group_departments)
    """
    # Создаем кафедры
    departments = [
        Department(1, "Алгебры и геометрии"),
        Department(2, "Высшей математики"),
        Department(3, "Аналитической химии"),
        Department(4, "Физики"),
        Department(5, "Английского языка"),
        Department(6, "Астрономии")
    ]
    
    # Создаем студенческие группы
    student_groups = [
        StudentGroup(1, "МАТ-101", 25, 1),
        StudentGroup(2, "МАТ-102", 30, 1),
        StudentGroup(3, "ВМ-201", 28, 2),
        StudentGroup(4, "ХИМ-301", 22, 3),
        StudentGroup(5, "АНГ-501", 35, 5),
        StudentGroup(6, "АНГ-502", 32, 5),
        StudentGroup(7, "АСТ-601", 18, 6)
    ]
    
    # Создаем связи многие-ко-многим
    group_departments = [
        GroupDepartment(1, 1),  # МАТ-101 - Алгебры и геометрии
        GroupDepartment(2, 1),  # МАТ-102 - Алгебры и геометрии
        GroupDepartment(3, 2),  # ВМ-201 - Высшей математики
        GroupDepartment(4, 3),  # ХИМ-301 - Аналитической химии
        GroupDepartment(5, 5),  # АНГ-501 - Английского языка
        GroupDepartment(6, 5),  # АНГ-502 - Английского языка
        GroupDepartment(7, 6),  # АСТ-601 - Астрономии
        # Дополнительные связи для демонстрации многие-ко-многим
        GroupDepartment(1, 2),  # МАТ-101 также относится к Высшей математики
        GroupDepartment(3, 1),  # ВМ-201 также относится к Алгебры и геометрии
        GroupDepartment(5, 1),  # АНГ-501 также относится к Алгебры и геометрии
    ]
    
    return departments, student_groups, group_departments

def print_test_data(departments, student_groups, group_departments):
    """Вывод тестовых данных"""
    print("=" * 80)
    print("ТЕСТОВЫЕ ДАННЫЕ")
    print("=" * 80)
    
    print("\nКафедры:")
    for dept in departments:
        print(f"  {dept}")
    
    print("\nСтуденческие группы:")
    for group in student_groups:
        print(f"  {group}")
    
    print("\nСвязи группы-кафедры:")
    for gd in group_departments:
        print(f"  {gd}")

def print_query_1(service):
    """Выполнение и вывод результатов запроса №1"""
    print("\n" + "=" * 80)
    print("ЗАПРОС №1")
    print("=" * 80)
    print("Список всех кафедр, у которых название начинается с буквы «А», ")
    print("и список студенческих групп, относящихся к ним:")
    
    departments_with_a = service.get_departments_starting_with('А')
    
    for dept in departments_with_a:
        dept_groups = service.get_groups_by_department_id(dept.id)
        print(f"\nКафедра: {dept.name}")
        if dept_groups:
            for group in dept_groups:
                print(f"  - Группа {group.group_name} ({group.student_count} студентов)")
        else:
            print("  Нет студенческих групп")

def print_query_2(service):
    """Выполнение и вывод результатов запроса №2"""
    print("\n" + "=" * 80)
    print("ЗАПРОС №2")
    print("=" * 80)
    print("Список кафедр с максимальным количеством студентов в группах")
    print("в каждой кафедре, отсортированный по максимальному количеству студентов:")
    
    department_max_students = service.get_departments_with_max_students()
    
    for dept_name, max_students in department_max_students:
        print(f"Кафедра '{dept_name}': максимальное количество студентов = {max_students}")

def print_query_3(service):
    """Выполнение и вывод результатов запроса №3"""
    print("\n" + "=" * 80)
    print("ЗАПРОС №3")
    print("=" * 80)
    print("Список всех связанных студенческих групп и кафедр (многие-ко-многим),")
    print("отсортированный по кафедрам, сортировка по группам произвольная:")
    
    connections = service.get_group_department_connections()
    
    for department, department_groups in connections.items():
        print(f"\nКафедра: {department.name}")
        for group in department_groups:
            print(f"  - Группа {group.group_name} ({group.student_count} студентов)")

def main():
    """Основная функция программы"""
    # Создание тестовых данных
    departments, student_groups, group_departments = create_test_data()
    
    # Вывод тестовых данных
    print_test_data(departments, student_groups, group_departments)
    
    # Создание сервиса данных
    service = DataService(departments, student_groups, group_departments)
    
    # Выполнение и вывод результатов запросов
    print_query_1(service)
    print_query_2(service)
    print_query_3(service)

if __name__ == "__main__":
    main()