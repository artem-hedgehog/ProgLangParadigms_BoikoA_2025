import unittest
import sys
import os

# Правильный путь к src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

try:
    from src.field import field, process_data
except ImportError:
    # Альтернативный вариант - импорт напрямую если файл в той же директории
    import sys
    sys.path.append('.')
    from src.field import field, process_data


class TestFieldGeneratorTDD(unittest.TestCase):
    """TDD тесты для генератора field"""
    
    def setUp(self):
        """Подготовка тестовых данных"""
        self.test_data = [
            {'title': 'Ковер', 'price': 2000, 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
            {'title': None, 'price': 5000},
            {'color': 'blue'},
            {'title': 'Стул', 'price': None, 'color': 'white'},
            'invalid_item',  # Не словарь для тестирования обработки ошибок
        ]
    
    def test_single_field_extraction(self):
        """Тест извлечения одного поля"""
        result = list(field(self.test_data, 'title'))
        expected = ['Ковер', 'Диван для отдыха', 'Стул']
        self.assertEqual(result, expected)
    
    def test_multiple_fields_extraction(self):
        """Тест извлечения нескольких полей"""
        result = list(field(self.test_data, 'title', 'price'))
        expected = [
            {'title': 'Ковер', 'price': 2000},
            {'title': 'Диван для отдыха', 'price': 5300},
            {'price': 5000},  # title is None, so only price is included
            {'title': 'Стул'}  # price is None, so only title is included
        ]
        self.assertEqual(result, expected)
    
    def test_none_values_handling(self):
        """Тест обработки None значений"""
        result = list(field(self.test_data, 'price'))
        expected = [2000, 5300, 5000]
        self.assertEqual(result, expected)
    
    def test_empty_result(self):
        """Тест случая когда нет подходящих данных"""
        result = list(field(self.test_data, 'non_existent_field'))
        self.assertEqual(result, [])
    
    def test_process_data_function(self):
        """Тест вспомогательной функции process_data"""
        result = process_data(self.test_data, 'color')
        expected = ['green', 'black', 'blue', 'white']
        self.assertEqual(result, expected)
    
    def test_invalid_input_handling(self):
        """Тест обработки некорректного ввода"""
        # Тест с пустым списком
        result = list(field([], 'title'))
        self.assertEqual(result, [])
        
        # Тест с не-словарями в списке
        mixed_data = [{'a': 1}, 'string', 123, {'b': 2}]
        result = list(field(mixed_data, 'a'))
        self.assertEqual(result, [1])


if __name__ == '__main__':
    unittest.main()