from input_functions import fahrenheit_conversion, get_celsius, get_fahrenheit, celsius_Conversion, get_number1, \
    get_number2, get_number3


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


#------------------------------------------------------------------------------------------------

# 2 - Balder - To ride Balder at Liseberg you must be 130 cm tall. Write a program that can tell you if you can ride!

def height_program():
    #getting the person height in cm
    person_height = float(input("Enter you height in cm : "))

#Checking the condition with if statement
    if person_height >= 130:
        print("Your are allowed to ride")
    else:
        print("Your are not allowed to ride \n\n")


#-------------------------------------------------------------------------------------------

# 3 - Sports Results-  program that asks the user how many goals each team scored, and tells which team won.

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


#------------------------------------------------------------------------------------------------

#  4 - Temperature Conversion - Write a program that can convert a temperature in degrees Celsius to degrees Fahrenheit.

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

#------------------------------------------------------------------------------------------------

# 5 - Calculators
#5.1 - Sum of 3 nos
def calculator():
    number_1 = get_number1()
    number_2 = get_number2()
    number_3 = get_number3()

    total = number_1 + number_2 + number_3
    print(f"Sum of 3 numbers are : {total} \n")

# 5.2 - finding largest number
     # number_1 is biggest and same
    if number_1 >= number_2 and number_1 >= number_3:
        print(f"number_1 {number_1} is the largest \n")
    elif number_2 >= number_3 and number_2 >= number_1:
        print(f"number_2 {number_2} is the largest \n")
    else:
        print(f"number_3 {number_3} is the largest \n")

    # 5.3 - finding the same number
    if number_1 == number_2 and number_1 != number_3:
        print(f"number_1 and number_2 are same : {number_1, number_2} \n")
    elif number_1 == number_3 and number_1 != number_2:
         print(f"number_1 and number_3 are same : {number_1, number_3} \n")
    elif number_2 == number_3 and number_2 != number_1:
        print(f"number_2 and number_3 are same : {number_2, number_3} \n")

    #5.4 Finding the middle number
    if number_1 == number_2 or number_2 == number_3:
        print("First or last 2 numbers are same, so no middle number \n")
    else:
        #using len function finding the no of items entered(list in total)
        number_entered = [number_1, number_2, number_3]
        nos_in_total = len(number_entered)

        # // leaves the decimal
        middle_position = nos_in_total // 2

        #getting the middle no value
        middle_number = number_entered[middle_position]
        print(f"Middle number is : {middle_number} \n")
