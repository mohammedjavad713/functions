n = int(input("Enter a number: "))
def factorial(num):
    fact = 1
    while num > 0:
        fact = fact * num
        num = num - 1
    return fact


print("Factorial:", factorial(n))