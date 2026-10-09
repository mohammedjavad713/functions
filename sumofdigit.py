n = int(input("Enter a number: "))
def summ(num):
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10
    return total

print("Sum of digits:", summ(n))
