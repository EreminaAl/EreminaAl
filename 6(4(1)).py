s_input = input("Введите целые числа через пробел: ")
numbers = list(map(int, s_input.split()))
max_number = numbers[0]
max_index = 0
for index in range(1, len(numbers)):
    if numbers[index] > max_number:
        max_number = numbers[index]
        max_index = index
print(f"Максимальный элемент: {max_number}")
print(f"Порядковый номер максимального элемента: {max_index + 1}")  
