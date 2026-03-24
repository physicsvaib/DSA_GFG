def prime_factors(a: int) -> list[int]:
    factors = []

    count = 2
    while a > 0 and count <= a:
        if a % count == 0:
            factors.append(count)
            a //= count
        else:
            count += 1

    return factors


print(prime_factors(315))
