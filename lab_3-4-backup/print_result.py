def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        print(func.__name__)
        
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        
        return result
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'Hello! I am a student from IU5-36B group.'


@print_result
def test_3():
    return {'a': 2, 'b': 45}


@print_result
def test_4():
    return [3, 7]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()