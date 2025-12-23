"""Модульные тесты для сервиса данных"""
import unittest
from models import Department, StudentGroup, GroupDepartment
from data_service import DataService

class TestDataService(unittest.TestCase):
    """Класс тестов для DataService"""
    
    def setUp(self):
        """Настройка тестовых данных перед каждым тестом"""
        # Создаем тестовые данные (ТОЛЬКО для тестов, без лишних данных из main.py)
        self.departments = [
            Department(1, "Алгебры и геометрии"),
            Department(2, "Высшей математики"),
            Department(3, "Аналитической химии"),
            Department(4, "Физики"),
            Department(5, "Английского языка"),
        ]
        
        self.student_groups = [
            StudentGroup(1, "МАТ-101", 25, 1),
            StudentGroup(2, "МАТ-102", 30, 1),
            StudentGroup(3, "ВМ-201", 28, 2),
            StudentGroup(4, "ХИМ-301", 22, 3),
            StudentGroup(5, "АНГ-501", 35, 5),
        ]
        
        self.group_departments = [
            GroupDepartment(1, 1),
            GroupDepartment(2, 1),
            GroupDepartment(3, 2),
            GroupDepartment(4, 3),
            GroupDepartment(5, 5),
            GroupDepartment(1, 2),  # Дополнительная связь
        ]
        
        # Создаем экземпляр сервиса
        self.service = DataService(
            self.departments, 
            self.student_groups, 
            self.group_departments
        )
    
    def test_get_departments_starting_with(self):
        """Тест для метода get_departments_starting_with"""
        # Тест 1: Поиск кафедр, начинающихся на 'А'
        result = self.service.get_departments_starting_with('А')
        self.assertEqual(len(result), 3)  # Исправлено: должно быть 3 кафедры
        # Проверяем конкретные кафедры
        dept_names = [dept.name for dept in result]
        expected_names = ["Алгебры и геометрии", "Аналитической химии", "Английского языка"]
        self.assertCountEqual(dept_names, expected_names)  # Проверяем содержимое без учета порядка
        
        # Тест 2: Поиск кафедр, начинающихся на 'В'
        result = self.service.get_departments_starting_with('В')
        self.assertEqual(len(result), 1)  # Должна быть 1 кафедра
        self.assertEqual(result[0].name, "Высшей математики")
        
        # Тест 3: Поиск кафедр, начинающихся на 'Ф'
        result = self.service.get_departments_starting_with('Ф')
        self.assertEqual(len(result), 1)  # Должна быть 1 кафедра
        self.assertEqual(result[0].name, "Физики")
        
        # Тест 4: Поиск кафедр, начинающихся на 'X' (нет таких)
        result = self.service.get_departments_starting_with('X')
        self.assertEqual(len(result), 0)  # Не должно быть кафедр
    
    def test_get_groups_by_department_id(self):
        """Тест для метода get_groups_by_department_id"""
        # Тест 1: Группы кафедры с ID=1
        result = self.service.get_groups_by_department_id(1)
        self.assertEqual(len(result), 2)  # Должно быть 2 группы
        group_names = [group.group_name for group in result]
        self.assertCountEqual(group_names, ["МАТ-101", "МАТ-102"])
        
        # Тест 2: Группы кафедры с ID=2
        result = self.service.get_groups_by_department_id(2)
        self.assertEqual(len(result), 1)  # Должна быть 1 группа
        self.assertEqual(result[0].group_name, "ВМ-201")
        
        # Тест 3: Группы кафедры с ID=5
        result = self.service.get_groups_by_department_id(5)
        self.assertEqual(len(result), 1)  # Должна быть 1 группа
        self.assertEqual(result[0].group_name, "АНГ-501")
        
        # Тест 4: Группы кафедры с ID=999 (не существует)
        result = self.service.get_groups_by_department_id(999)
        self.assertEqual(len(result), 0)  # Не должно быть групп
    
    def test_get_departments_with_max_students(self):
        """Тест для метода get_departments_with_max_students"""
        result = self.service.get_departments_with_max_students()
        
        # Проверяем количество результатов
        self.assertEqual(len(result), 4)  # Должно быть 4 кафедры (у кафедры 4 нет групп)
        
        # Проверяем правильность сортировки (по убыванию количества студентов)
        self.assertEqual(result[0][1], 35)  # Максимум у кафедры английского
        self.assertEqual(result[1][1], 30)  # Затем у алгебры
        self.assertEqual(result[2][1], 28)  # Затем у высшей математики
        self.assertEqual(result[3][1], 22)  # Затем у химии
        
        # Проверяем названия кафедр
        self.assertEqual(result[0][0], "Английского языка")
        self.assertEqual(result[1][0], "Алгебры и геометрии")
        self.assertEqual(result[2][0], "Высшей математики")
        self.assertEqual(result[3][0], "Аналитической химии")
        
        # Проверяем структуру результата
        for dept_name, max_students in result:
            self.assertIsInstance(dept_name, str)
            self.assertIsInstance(max_students, int)
            self.assertGreater(max_students, 0)
    
    def test_get_group_department_connections(self):
        """Тест для метода get_group_department_connections"""
        result = self.service.get_group_department_connections()
        
        # Проверяем количество кафедр в результате
        self.assertEqual(len(result), 4)  # Должно быть 4 кафедры (у кафедры 4 нет связей)
        
        # Проверяем сортировку по названиям кафедр
        departments = list(result.keys())
        dept_names = [dept.name for dept in departments]
        expected_names = ["Алгебры и геометрии", "Аналитической химии", 
                         "Английского языка", "Высшей математики"]
        self.assertEqual(dept_names, expected_names)
        
        # Проверяем связи для кафедры "Алгебры и геометрии"
        algebra_groups = result[departments[0]]
        self.assertEqual(len(algebra_groups), 2)  # Исправлено: 2 группы связаны с этой кафедрой
        group_names = sorted([g.group_name for g in algebra_groups])
        self.assertEqual(group_names, ["МАТ-101", "МАТ-102"])  # Только эти 2 группы
        
        # Проверяем связи для кафедры "Высшей математики"
        math_groups = result[departments[3]]
        self.assertEqual(len(math_groups), 2)  # 2 группы: ВМ-201 и МАТ-101 (через дополнительную связь)
        group_names = sorted([g.group_name for g in math_groups])
        self.assertEqual(group_names, ["ВМ-201", "МАТ-101"])

if __name__ == '__main__':
    # Запуск тестов с детальным выводом
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDataService)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)