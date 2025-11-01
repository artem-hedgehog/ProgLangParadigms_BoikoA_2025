import sys
import math

class BiquadraticEquation:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []
        self.discriminant = None
    
    def validate_coefficients(self):
        if self.a == 0:
            raise ValueError("Коэффициент A не может быть равен 0")
    
    def calculate_discriminant(self):
        self.discriminant = self.b**2 - 4*self.a*self.c
        return self.discriminant
    
    def solve(self):
        """Решение биквадратного уравнения"""
        self.validate_coefficients()
        self.calculate_discriminant()
        
        if self.discriminant < 0:
            return []
        
        t1 = (-self.b + math.sqrt(self.discriminant)) / (2*self.a)
        t2 = (-self.b - math.sqrt(self.discriminant)) / (2*self.a)
        
        real_roots = []
        
        if t1 >= 0:
            root1 = math.sqrt(t1)
            root2 = -math.sqrt(t1)
            real_roots.extend([root1, root2])
        
        if t2 >= 0 and abs(t2 - t1) > 1e-10:
            root3 = math.sqrt(t2)
            root4 = -math.sqrt(t2)
            real_roots.extend([root3, root4])
        
        self.roots = real_roots
        return self.roots
    
    def display_solution(self):
        print(f"\nРешение уравнения: {self.a}x⁴ + {self.b}x² + {self.c} = 0")
        print(f"Дискриминант D = {self.b}² - 4*{self.a}*{self.c} = {self.discriminant}")
        
        if self.discriminant < 0:
            print("Дискриминант отрицательный. Действительных корней нет.")
        elif not self.roots:
            print("Нет действительных корней.")
        else:
            print(f"Действительные корни уравнения: {sorted(self.roots)}")

class InputHandler:
    
    @staticmethod
    def get_valid_coefficient(prompt):
        while True:
            try:
                value = input(prompt)
                return float(value)
            except ValueError:
                print("Ошибка! Введите действительное число.")
    
    @staticmethod
    def parse_command_line_args():
        coefficients = []

        for i in range(3):
            if i + 1 < len(sys.argv):
                try:
                    coefficients.append(float(sys.argv[i + 1]))
                except ValueError:
                    coefficients.append(None)
            else:
                coefficients.append(None)
        return coefficients

def main_oo():
    print("Решение биквадратного уравнения вида: Ax⁴ + Bx² + C = 0")
    
    # Обработка параметров командной строки
    coefficients = InputHandler.parse_command_line_args()
    
    # Получение коэффициентов
    a = coefficients[0] if coefficients[0] is not None else InputHandler.get_valid_coefficient("Введите коэффициент A: ")
    b = coefficients[1] if coefficients[1] is not None else InputHandler.get_valid_coefficient("Введите коэффициент B: ")
    c = coefficients[2] if coefficients[2] is not None else InputHandler.get_valid_coefficient("Введите коэффициент C: ")
    
    try:
        # Создание и решение уравнения
        equation = BiquadraticEquation(a, b, c)
        equation.solve()
        equation.display_solution()
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main_oo()