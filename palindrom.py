def is_palindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return original == rev

n = int(input("Enter a number: "))
print(is_palindrome(n))