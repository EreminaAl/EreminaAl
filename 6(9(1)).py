s= input("Введите вещественные числа через пробел: ")
numbers = list(map(float, s.split()))
min_x_value = x(numbers[0])
min_element = numbers[0]
for number in numbers:
    x_value= x(number)
    if x_value < min_x_value:
        min_x_value = x_value
        min_element = number 
print("Минимальный по модулю элемент:", min_element)
reversed_numbers = numbers[::-1]
print("Массив в обратном порядке:", reversed_numbers)
