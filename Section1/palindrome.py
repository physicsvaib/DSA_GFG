def is_palindrome(inp: int) -> bool:
    og_num = inp
    flipped_num = 0

    while inp > 0:
        flipped_num *= 10
        flipped_num += inp % 10
        inp //= 10

    return flipped_num == og_num


print(is_palindrome(121))
print(is_palindrome(1212))
print(is_palindrome(1123123))
print(is_palindrome(1155225511))
