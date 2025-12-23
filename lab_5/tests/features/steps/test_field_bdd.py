import sys
import os

# Правильный путь к src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

try:
    from behave import given, when, then
    from src.field import field, process_data
except ImportError:
    # Установите behave если его нет
    print("Установите behave: pip install behave")
    # Альтернативный импорт
    sys.path.append('.')
    from src.field import field, process_data


# Контекст для хранения состояния между шагами
def before_scenario(context, scenario):
    context.test_data = []
    context.result = []


@given('список словарей с товарами')
def step_given_list_of_dicts(context):
    """Подготовка тестовых данных"""
    context.test_data = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': None, 'price': 5000},
        {'color': 'blue'},
        {'title': 'Стул', 'price': None, 'color': 'white'},
    ]


@given('список содержит словари с None значениями')
def step_given_list_with_none_values(context):
    """Подготовка данных с None значениями"""
    context.test_data = [
        {'title': 'Товар1', 'price': 1000},
        {'title': None, 'price': 2000},
        {'title': 'Товар3', 'price': None},
    ]


@when('я извлекаю поле "{field_name}"')
def step_when_extract_single_field(context, field_name):
    """Извлечение одного поля"""
    context.result = list(field(context.test_data, field_name))


@when('я извлекаю поля "{field1}" и "{field2}"')
def step_when_extract_multiple_fields(context, field1, field2):
    """Извлечение нескольких полей"""
    context.result = list(field(context.test_data, field1, field2))


@when('я обрабатываю данные с полями "{fields}"')
def step_when_process_data_with_fields(context, fields):
    """Обработка данных с указанными полями"""
    field_list = [f.strip() for f in fields.split(',')]
    context.result = process_data(context.test_data, *field_list)


@then('я получаю значения "{expected_values}"')
def step_then_get_expected_values(context, expected_values):
    """Проверка ожидаемых значений"""
    expected = [v.strip() for v in expected_values.split(',')]
    # Преобразуем числовые значения
    processed_expected = []
    for val in expected:
        if val.isdigit():
            processed_expected.append(int(val))
        elif val == 'None':
            processed_expected.append(None)
        else:
            processed_expected.append(val)
    
    assert context.result == processed_expected


@then('я получаю список словарей')
def step_then_get_list_of_dicts(context):
    """Проверка что результат - список словарей"""
    assert isinstance(context.result, list)
    if context.result:  # Если список не пустой
        assert all(isinstance(item, dict) for item in context.result)


@then('результат содержит {count:d} элементов')
def step_then_result_contains_count(context, count):
    """Проверка количества элементов"""
    assert len(context.result) == count


@then('результат пуст')
def step_then_result_is_empty(context):
    """Проверка что результат пуст"""
    assert context.result == []


@then('каждый словарь содержит хотя бы одно из полей "{fields}"')
def step_then_each_dict_contains_at_least_one_field(context, fields):
    field_list = [f.strip() for f in fields.split(',')]
    for i, item in enumerate(context.result):
        has_any = any(field in item for field in field_list)
        assert has_any, f"Элемент {i} {item} не содержит ни одного из полей {field_list}"


# Файлы функций для BDD (tests/features/field.feature)
"""
Feature: Field Generator
  As a developer
  I want to use field generator to extract data from dictionaries
  So that I can process structured data efficiently

  Scenario: Extract single field from valid data
    Given список словарей с товарами
    When я извлекаю поле "title"
    Then я получаю значения "Ковер, Диван для отдыха, Стул"
    And результат содержит 3 элементов

  Scenario: Extract multiple fields from valid data
    Given список словарей с товарами
    When я извлекаю поля "title" и "price"
    Then я получаю список словарей
    And каждый словарь содержит поля "title, price"
    And результат содержит 3 элементов

  Scenario: Handle None values correctly
    Given список содержит словари с None значениями
    When я извлекаю поле "title"
    Then я получаю значения "Товар1, Товар3"
    And результат содержит 2 элементов

  Scenario: Process non-existent field
    Given список словарей с товарами
    When я извлекаю поле "non_existent"
    Then результат пуст

  Scenario: Use process_data helper function
    Given список словарей с товарами
    When я обрабатываю данные с полями "color"
    Then я получаю значения "green, black, blue, white"
    And результат содержит 4 элементов
"""