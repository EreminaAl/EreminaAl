def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)

N = int(input("Введите натуральное число N: "))

result = sum_digits(N)

print(f"Сумма цифр числа {N} равна {result}")
