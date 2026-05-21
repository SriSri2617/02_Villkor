# 1 - Shopping program
def discount_program():
    is_member = False
    level1 = 100
    level2 = 200
    discount = 0

    price = input("Välkommen, köp något dyrt: ")
    price = float(price)
    if price > level1:
        print("Grattis! Du har avancerat till nivå 1 och får 10% rebat.")
        discount = discount + 10

    if price >= level2:
        print("Grattis! Du har avancerat till nivå 2 och får 25% rebat.")
        discount = discount + 25

    if is_member:
        print("Som medlem får du extra 5% rabatt.")
        discount = discount + 5



    final_price = price * (100 - discount) / 100
    print(f"Efter rebatter blir priset... {final_price:.2f} kr \n\n")


#-------------------------------------------------------------

# 2 - To ride Balder at Liseberg you must be 130 cm tall. Write a program that can tell you if you can ride!

def height_program():
    is_member = False
    level1 = 100
    level2 = 200
    person_height = float(input("Enter you height in cm : "))

#Checking the condition with if statement
    if person_height >= 130:
        print("Your are allowed to ride")
    else:
        print("Your are not allowed to ride \n\n")


#-------------------------------------------------------------

# 3 -  program that asks the user how many goals each team scored, and tells which team won.

def championship_league():
    print(" Tottenham & Liverpool - championship League")
    print("Lets find out the winner based on their goals")

    tottenham = int(input("Tottenham goals in total :  "))
    liverpool = int(input("Liverpool goals in total :  "))

#calculate won by how many goals
    # abs is used for absolute value of number - it removes the (-) sign and only gives + number
    goals_ahead = abs(tottenham - liverpool)

#comparison of goals with if - to find who won, or it's draw

    if tottenham > liverpool:
        print("Tottenham won the match")
        print(f"Tottenham won by {goals_ahead} goals")

    elif tottenham == liverpool:
        print("It's draw / tie match")
        print(f"Both the team has {tottenham} goals")

    else:
        print("Liverpool won the match")
        print(f"Liverpool won by {goals_ahead} goals")


#-------------------------------------------------------------

#  4 - Write a program that can convert a temperature in degrees Celsius to degrees Fahrenheit.
##########################################################################
#Reusable module - Formula for temperature conversion

#Celsius Conversion
def celsius_Conversion(F_fahrenheit):
    return (F_fahrenheit - 32) / 1.8

#Fahrenheit conversion
def fahrenheit_conversion(C_celsius):
    return 1.8 * C_celsius + 32

def get_celsius():
    return float(input("Enter a temperature in Celsius : "))

def get_fahrenheit():
    return float(input("Enter a temperature in Fahrenheit : "))

###########################################################################

#Conversion
def temp_conversion():

#Celsius to Fahrenheit
    celsius = get_celsius()
    fahrenheit = fahrenheit_conversion(celsius)
    print(f"It is {fahrenheit:.3f} Fahrenheit \n")

# Fahrenheit to Celsius
    fahrenheit = get_fahrenheit()
    celsius = celsius_Conversion(fahrenheit)
    print(f"It is {celsius:.3f} Celsius \n")

# User choice of entering the temperature
    temp_choice = input("You want to enter the temperature in Fahrenheit or Celsius (Enter F or C) : ").upper()

    if temp_choice == "F":
        F = get_fahrenheit()
        celsius_C = celsius_Conversion(F)
        print(f"It is {celsius_C:.3f} Celsius\n")

    elif temp_choice == "C":
            C = get_celsius()
            fahrenheit_F1 = fahrenheit_conversion(C)
            print(f"It is {fahrenheit_F1:.3f} Fahrenheit\n")

# Checking the converted temperature is below 10 degree Celsius
    if temp_choice == "C" and C <= 10:
        print("It's cold outside and don't forget to wear jacket")
    elif temp_choice == "F" and celsius_C <= 10:
        print("It's cold outside and don't forget to wear jacket")






















































"""
#Choose which program to run
program_to_run = input("Choose a program to run (1/2) : ")
if program_to_run == "1":
    discount_program()
elif program_to_run == "2":
    height_program()
"""
