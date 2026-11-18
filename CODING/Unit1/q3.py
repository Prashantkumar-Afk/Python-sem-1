# Create a temperature converter between Celsius, Fahrenheit and Kelvin.
temp = float(input("Enter temperature: "))
scale = input("Enter scale (C/F/K): ")

if scale == "C":
    print("Fahrenheit:", temp * 9/5 + 32)
    print("Kelvin:", temp + 273.15)
elif scale == "F":
    print("Celsius:", (temp - 32) * 5/9)
    print("Kelvin:", (temp - 32) * 5/9 + 273.15)
elif scale == "K":
    print("Celsius:", temp - 273.15)
    print("Fahrenheit:", (temp - 273.15) * 9/5 + 32)
else:
    print("Invalid scale!")