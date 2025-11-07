def field(items, *args):
    assert len(args) > 0
    
    if len(args) == 1:
        # Передан один аргумент- возвращаем только значения
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]
    else:
        # Передано несколько аргументов - возвращаем словари
        for item in items:
            result = {}
            has_valid_fields = False
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
                    has_valid_fields = True
            
            if has_valid_fields:
                yield result


if __name__ == '__main__':
    # Тестовые данные
    goods = [
        {'title': 'Радиоприёмник', 'price': 3500, 'color': 'black'},
        {'title': 'Гитара акустическая', 'color': 'red'},
        {'title': None, 'price': 5000},
        {'color': 'blue'}
    ]
    
    print("Тест 1 - один аргумент:")
    for title in field(goods, 'title'):
        print(title)
    
    print("\nТест 2 - несколько аргументов:")
    for item in field(goods, 'title', 'price'):
        print(item)