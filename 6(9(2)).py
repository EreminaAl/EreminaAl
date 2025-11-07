import random
A = [random.randint(1, 100) for _ in range(10)]
B = [random.randint(1, 100) for _ in range(10)]
print("Исходный массив A:", A)
print("Исходный массив B:", B)
A, B = B, A
print("Преобразованный массив A:", A)
print("Преобразованный массив B:", B)
