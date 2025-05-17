# Topic 2: Basic Data Types and Operators - Combined Tasks

# ----------------------------
# Task 1: Area and Perimeter of a Rectangle
# ----------------------------
length = 10
breadth = 5
area = length * breadth
perimeter = 2 * (length + breadth)
print("\nTask 1: Area and Perimeter of Rectangle")
print("Length:", length, "| Breadth:", breadth)
print("Area:", area)
print("Perimeter:", perimeter)

# ----------------------------
# Task 2: Compare Two Numbers
# ----------------------------
print("\nTask 2: Compare Two Numbers")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print("First number is greater than the second.")
elif a < b:
    print("First number is less than the second.")
else:
    print("Both numbers are equal.")

# ----------------------------
# Task 3: Leap Year Checker
# ----------------------------
print("\nTask 3: Leap Year Checker")
year = int(input("Enter a year to check if it's a leap year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# ----------------------------
# Task 4: Experiment with Operators
# ----------------------------
print("\nTask 4: Operator Experiments")
print("Arithmetic: 10 + 3 =", 10 + 3)
print("Floor Division: 10 // 3 =", 10 // 3)
print("Modulus: 10 % 3 =", 10 % 3)
print("Exponentiation: 2 ** 3 =", 2 ** 3)

print("Comparison: 5 == 5:", 5 == 5)
print("Comparison: 5 != 3:", 5 != 3)

print("Logical AND: True and False =", True and False)
print("Logical OR: True or False =", True or False)
print("Logical NOT: not True =", not True)

# ----------------------------
# Task 5: String Concatenation
# ----------------------------
print("\nTask 5: String Concatenation")
first_name = "sailu"
last_name = "bandi"
full_name = first_name + " " + last_name
print("Full name:", full_name)
