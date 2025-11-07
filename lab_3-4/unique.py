class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()
    
    def __next__(self):
        while True:
            item = next(self.items)
            
            # Для сравнения учитываем регистр в зависимости от ignore_case
            if self.ignore_case and isinstance(item, str):
                check_item = item.lower()
            else:
                check_item = item
            
            if check_item not in self.seen:
                self.seen.add(check_item)
                return item
    
    def __iter__(self):
        return self


if __name__ == '__main__':
    print("Тест 1 - числа:")
    data1 = [1, 1, 2, 3, 1, 2, 4, 1, 3, 2, 5]
    for item in Unique(data1):
        print(item)
    
    print("\nТест 2 - строки без ignore_case:")
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data2):
        print(item)
    
    print("\nТест 3 - строки с ignore_case=True:")
    for item in Unique(data2, ignore_case=True):
        print(item)