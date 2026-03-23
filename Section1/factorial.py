def factorial(num: int) -> int:
    fact = 1
    for i in range(2, num + 1):
        fact *= i

    return fact


def factorial_rec(num: int) -> int:
    if num <= 1:
        return 1

    return num * factorial_rec(num - 1)


print(factorial_rec(50))
