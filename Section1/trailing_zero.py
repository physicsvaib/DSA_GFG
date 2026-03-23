def trailing_zeros(num: int) -> int:
    count = 0
    divisor = 5

    while True:
        val = num // divisor

        if val == 0:
            break

        count += val
        divisor *= 5

    return int(count)


print(trailing_zeros(500000000000))
