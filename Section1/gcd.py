def gcd_basic(num1: int, num2: int) -> int:
    value = 1

    smaller_num = num1 if num1 < num2 else num2

    if num1 % smaller_num == 0 and num2 % smaller_num == 0:
        return smaller_num

    for i in range(2, smaller_num // 2 + 1):
        if num1 % i == 0 and num2 % i == 0:
            value = i

    return value


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(4, 6))
print(gcd(100, 200))
print(gcd(7, 10))
print(gcd(15, 10))
print(gcd(70, 10))
