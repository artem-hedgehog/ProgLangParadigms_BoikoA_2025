import sys
import math

def get_valid_coefficient(prompt):
    
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Ошибка! Введите действительное число.")

def solve_biquadratic(a, b, c):
    
    print(f"\nРешение уравнения: {a}x⁴ + {b}x² + {c} = 0")
    
    if a == 0:
        print("Ошибка: коэффициент A не может быть равен 0 для биквадратного уравнения")
        return []
    
    D = b**2 - 4*a*c
    print(f"Дискриминант D = {b}² - 4*{a}*{c} = {D}")
    
    real_roots = []
    
    if D < 0:
        print("Дискриминант отрицательный. Действительных корней нет.")
    else:

        t1 = (-b + math.sqrt(D)) / (2*a)
        t2 = (-b - math.sqrt(D)) / (2*a)
        
        print(f"Корни для t = x²: t1 = {t1:.4f}, t2 = {t2:.4f}")
        
        # Находим действительные корни x
        if t1 >= 0:
            root1 = math.sqrt(t1)
            root2 = -math.sqrt(t1)
            real_roots.extend([root1, root2])
            print(f"Из t1 = {t1:.4f} получаем корни: x = ±{root1:.4f}")
        
        if t2 >= 0 and abs(t2 - t1) > 1e-10:  # Чтобы избежать дублирования
            root3 = math.sqrt(t2)
            root4 = -math.sqrt(t2)
            real_roots.extend([root3, root4])
            print(f"Из t2 = {t2:.4f} получаем корни: x = ±{root3:.4f}")
        
        if not real_roots:
            print("Нет действительных корней (t1 и t2 отрицательные)")
    
    return real_roots

def main():
    print("Решение биквадратного уравнения вида: Ax⁴ + Bx² + C = 0")
    
    coefficients = []
    for i in range(3): 
        if i < len(sys.argv) - 1:
            try:
                coefficients.append(float(sys.argv[i + 1]))
            except (ValueError, IndexError):
                coefficients.append(None)
        else:
            coefficients.append(None)
    
    a = coefficients[0] if coefficients[0] is not None else get_valid_coefficient("Введите коэффициент A: ")
    b = coefficients[1] if coefficients[1] is not None else get_valid_coefficient("Введите коэффициент B: ")
    c = coefficients[2] if coefficients[2] is not None else get_valid_coefficient("Введите коэффициент C: ")
    
    roots = solve_biquadratic(a, b, c)
    
    if roots:
        print(f"\nДействительные корни уравнения: {sorted(roots)}")
    else:
        print("\nУравнение не имеет действительных корней.")

if __name__ == "__main__":
    main()