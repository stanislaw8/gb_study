"""
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
равнобедренным или равносторонним.
"""
a = int(input('Введите длину первого отрезка: '))
b = int(input('Введите длину второго отрезка: '))
c = int(input('Введите длину третьего отрезка: '))

if a + b > c and b + c > a and a + c > b:
    if a == b or a == c or b == c:
        if a == b and a == c:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольника с такими сторонами не существует')