
#  4 - Write a program that can convert a temperature in degrees Celsius to degrees Fahrenheit.

#Reusable module - Formula for temperature conversion

#Celsius Conversion
def celsius_Conversion(F_fahrenheit):
    return (F_fahrenheit - 32) / 1.8

#Fahrenheit conversion
def fahrenheit_conversion(C_celsius):
    return 1.8 * C_celsius + 32

# input for Celsius
def get_celsius():
    return float(input("Enter a temperature in Celsius : "))

# input for Fahrenheit
def get_fahrenheit():
    return float(input("Enter a temperature in Fahrenheit : "))

#-------------------------------------------------------------------------------------------------------

# 5 - Calculators
# input for getting 3 nos
def get_number1():
    return int(input("Enter a number_1: "))
def get_number2():
    return int(input("Enter a number_2: "))
def get_number3():
    return int(input("Enter a number_3: "))


