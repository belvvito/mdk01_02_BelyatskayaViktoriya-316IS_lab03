import math

def raznostorini_triangle(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('треугольника не существует, введите другие значения')
    elif a != b != c:
        print('разносторонний треугольник')
    else:
        print('это не разносторонний треугольник, введите другие значения')
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return round(s, 2)
print(raznostorini_triangle(5, 4, 7))

def ravnobedreni_triangle(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('треугольника не существует, введите другие значения')
    elif a == b or a == c or b == c:
        print('равнобедренный треугольник')
    else:
        print('это не равнобедренный треугольник, введите другие значения')
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return round(s, 2)
print(ravnobedreni_triangle(6, 6, 7))

def ravnostoroni_triangle(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('треугольника не существует, введите другие значения')
    elif a == b == c:
        print('равносторонний треугольник')
    else:
        print('это не равносторонний треугольник, введите другие значения')
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return round(s, 2)
print(ravnostoroni_triangle(5, 5, 5))