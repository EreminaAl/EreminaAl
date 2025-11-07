import math
def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

cathet1_a = float(input("Введите катет a первого треугольника: "))
cathet1_b = float(input("Введите катет b первого треугольника: "))

cathet2_a = float(input("Введите катет a второго треугольника: "))
cathet2_b = float(input("Введите катет b второго треугольника: "))

hypotenuse1 = calculate_hypotenuse(cathet1_a, cathet1_b)
hypotenuse2 = calculate_hypotenuse(cathet2_a, cathet2_b)

if hypotenuse1 > hypotenuse2:
    print("Гипотенуза первого треугольника больше.")
elif hypotenuse1 < hypotenuse2:
    print("Гипотенуза второго треугольника больше.")
else:
    print("Гипотенузы равны.")
