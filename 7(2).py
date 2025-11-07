def d(a,b):
    d = a*b
    return d
A = []
for i in range(3):
    print('введите стороны', i, '- го прямоугольника:')
    a = int(input('сторона a:'))
    b = int(input('сторона b:'))
    A.append(d(a,b))
for i in range(3):
    print('площадь', i, '- го прямоугольника:', A[i])
