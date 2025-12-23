# features/field.feature
# encoding: utf-8

Feature: Field Generator
  As a developer
  I want to use field generator to extract data from dictionaries
  So that I can process structured data efficiently

  Scenario: Извлечение одного поля из валидных данных
    Given список словарей с товарами
    When я извлекаю поле "title"
    Then я получаю значения "Ковер, Диван для отдыха, Стул"
    And результат содержит 3 элементов

  Scenario: Извлечение нескольких полей из валидных данных
    Given список словарей с товарами
    When я извлекаю поля "title" и "price"
    Then я получаю список словарей
    And каждый словарь содержит хотя бы одно из полей "title, price"
    And результат содержит 4 элементов

  Scenario: Обработка None значений корректно
    Given список содержит словари с None значениями
    When я извлекаю поле "title"
    Then я получаю значения "Товар1, Товар3"
    And результат содержит 2 элементов

  Scenario: Обработка несуществующего поля
    Given список словарей с товарами
    When я извлекаю поле "non_existent"
    Then результат пуст

  Scenario: Использование вспомогательной функции process_data
    Given список словарей с товарами
    When я обрабатываю данные с полями "color"
    Then я получаю значения "green, black, blue, white"
    And результат содержит 4 элементов