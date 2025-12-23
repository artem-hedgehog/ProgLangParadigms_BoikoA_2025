def field(items, *args):
    """
    Генератор для извлечения полей из словарей.
    
    Args:
        items: Список словарей
        *args: Ключи для извлечения
    
    Yields:
        Если передан один аргумент - значения поля
        Если несколько аргументов - словари с указанными полями
    """
    assert len(args) > 0, "Должен быть передан хотя бы один аргумент"
    
    if len(args) == 1:
        # Если передан один аргумент, возвращаем только значения
        key = args[0]
        for item in items:
            if isinstance(item, dict) and key in item and item[key] is not None:
                yield item[key]
    else:
        # Если передано несколько аргументов, возвращаем словари
        for item in items:
            if not isinstance(item, dict):
                continue
                
            result = {}
            has_valid_fields = False
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
                    has_valid_fields = True
            
            if has_valid_fields:
                yield result


def process_data(data, *fields):
    """
    Функция для обработки данных с использованием field генератора.
    Возвращает список результатов для удобства тестирования.
    """
    return list(field(data, *fields))