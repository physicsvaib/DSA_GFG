def count_digits(num: int) -> int:
    count = 0

    while num > 0:
        num //= 10
        count += 1

    return count


print(count_digits(20542152))
