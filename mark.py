def calculate_total(m1, m2, m3):
    return m1 + m2 + m3

def calculate_average(total):
    return total / 3

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

# Main program
name = input("Enter student name: ")

m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))

total = calculate_total(m1, m2, m3)
average = calculate_average(total)
grade = calculate_grade(average)

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", round(average, 2))
print("Grade:", grade)