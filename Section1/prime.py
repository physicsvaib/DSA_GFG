from math import floor, sqrt


def is_prime(a: int) -> bool:
    if a % 2 == 0:
        return False
    for i in range(3, floor(sqrt(a) + 1), 2):
        if a % i == 0:
            return False

    return True


print(is_prime(50))
print(is_prime(51))
print(is_prime(57))
print(is_prime(83))
print(is_prime(97))
print(is_prime(7))
print(is_prime(13))
