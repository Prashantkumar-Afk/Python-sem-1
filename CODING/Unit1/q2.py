# Write a program to swap two numbers without using a third variable.
Num1 = int(input("Enter no 1: "))
Num2 = int(input("Enter no 2: "))

print("Before swapping:")
print("No 1:", Num1)
print("No 2:", Num2)

Num1 = Num1 + Num2
Num2 = Num1 - Num2
Num1 = Num1 - Num2

print("After swapping:")
print("No 1:", Num1)
print("No 2:", Num2)