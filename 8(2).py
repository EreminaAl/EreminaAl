N = int(input("Введите число строк N: "))
B = int(input("Введите число столбцов B: "))

A = []

print("Введите элементы матрицы:")
for i in range(N):
    row = []
    for j in range(B):
        element = float(input('элемент'+str(j)+':'))
        row.append(element)
    A.append(row)
for i in range(N):
    row = A[i]
    max_index = row.index(max(row))
    min_index = row.index(min(row))
    row[0], row[max_index] = row[max_index], row[0]
    row[-1], row[min_index] = row[min_index], row[-1]
    A[i] = row

print("Измененная матрица:")
for row in A:
    print(row)
