def is_prime(n, divisor=2):
    if divisor == n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)

N = int(input("Введите натуральное число n > 1: "))

if is_prime(N):
    print("YES")
else:
    print("NO")
