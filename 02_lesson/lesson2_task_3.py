import math

def square():

    side = float(input("Введите сторону квадрата: "))
    if side <= 0:
        raise ValueError("Сторона квадрата должна быть положительной")
    result = side ** 2
    if not isinstance(side, int):
        result = math.ceil(result)
    print(f"Площадь квадрата со стороной {side}: {result}")

# Вызов функции
square()

