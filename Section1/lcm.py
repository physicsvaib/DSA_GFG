def lcm_basic(a: int, b: int) -> int:
    larger_num = a if a > b else b

    mul = a * b

    for i in range(larger_num, mul + 1):
        if i % a == 0 and i % b == 0:
            return i

    return mul


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    # a*b = gcd(a,b) * lcm(a,b)
    return (a * b) // gcd(a, b)


print(lcm(4, 6))
print(lcm(8, 2))
print(lcm(12, 21))
