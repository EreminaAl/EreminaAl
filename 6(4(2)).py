s_input = input("Введите целые числа через пробел: ")
numbers = list(map(int, s_input.split()))
x = []
for number in numbers:
    if number % 2 != 0: 
        x.append(number) 
if x:
    x.sort(reverse=True)
    print("Нечетные числа в порядке убывания:", x)
else:
    print("Нечетных чисел нет.")
