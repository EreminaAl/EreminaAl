N = int(input("Введите размер матрицы N: "))

A = []

print("Введите элементы матрицы:")
for i in range(N):
    row = []
    for j in range(N):
        element = float(input(f"A[{i+1}][{j+1}] = "))
        row.append(element)
    A.append(row)

sum_positive = 0
count_positive = 0

for i in range(N):
    for j in range(i+1, N):
        if A[i][j] > 0:
            sum_positive += A[i][j]
            count_positive += 1

print(f"Сумма положительных элементов над главной диагональю: {sum_positive}")
print(f"Количество положительных элементов над главной диагональю: {count_positive}")
