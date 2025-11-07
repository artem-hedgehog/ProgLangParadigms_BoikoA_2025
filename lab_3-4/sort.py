data = [26, -72, 155, -37, 103, 1, 0, -1, 43]

if __name__ == '__main__':
    # Без lambda-функции
    result = sorted(data, key=abs, reverse=True)
    print("Без lambda:", result)
    
    # С lambda-функцией
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print("С lambda:", result_with_lambda)