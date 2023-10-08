import math
def square(side):
    if isinstance(side, int):
        area = side * side
    else:
        area = math.ceil(side * side)   
    return area
side = float(input("Введите сторону квадрата: "))
result = square(side)
print(f"Площадь квадрата: {result}")
