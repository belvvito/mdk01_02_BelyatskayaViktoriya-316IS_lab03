import math

def ostrougolni_triangle(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('треугольника не существует, введите другие значения')
    elif c**2 < a**2 + b**2:
        print('остроугольный треугольник')
    else:
        print('это не остроугольный треугольник, введите другие значения')
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return round(s, 2)

def tupougolni_triangle(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('треугольника не существует, введите другие значения')
    elif c**2 > a**2 + b**2:
        print('тупоугольный треугольник')
    else:
        print('это не тупоугольный треугольник, введите другие значения')
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return round(s, 2)

def pryamougolni_triangle(a, b, c):
    if (a or b or c <= 0) and (a + b < c or a + c < b or b + c < a):
        print('треугольника не существует, введите другие значения')
    elif c ** 2 == a ** 2 + b ** 2:
        print('прямоугольный треугольник')
    else:
        print('это не прямоугольный треугольник, введите другие значения')
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return round(s, 2)



print(ostrougolni_triangle(5,5,3))
print(tupougolni_triangle(6,5,9))
print(pryamougolni_triangle(4,3, 5))