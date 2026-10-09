def is_prime(num):
    if num < 2:
        return False

    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1

    return True

n = int(input("Enter a number: "))
print(is_prime(n))