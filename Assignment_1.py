import math
from datetime import date, timedelta



# Assignment 1 - To check print function

Name = "World"
print(f"Hello {Name}") # \n adds a blank line right after this text

#Runtime input verification
Name = "Mathumitha"
print(f"This program was made by {Name} \n")


# Assignment 3 - Ticket price calculation
TicketPrice = 100
MoneyInHand = 200

#Balance calculation
Balance = MoneyInHand - TicketPrice
print(f"There is {Balance} Kr left")

#Return Amt calculation
ReturnAmt = Balance / 2
print(f"Each person gets {ReturnAmt}Kr \n")


# Assignment 4 - 1a
#Number stored in variable
Enter_Number = input("Enter number1: ")

#Variable into integer
Number1 = int(Enter_Number)

# Assignment 4 - 1b
Number2 = int(input("Enter number2: "))
SumOfNumbers = Number1 + Number2
print(f"Total : {SumOfNumbers} \n")

# Assignment 4 - 2a (Fixed percentage)
Price = 2000
print(f"WinterJacketPrice  : {Price} kr")

#Fixed discount
Sale_Percentage = 75.0
Sale_Discount = 100 - Sale_Percentage
print(f"Sale_Percent : {Sale_Discount:.0f}%")
Discount = (Price * Sale_Discount) / 100
Final_Price = Price - Discount
print(f"Final price is : {Final_Price} kr \n")

#Assignment 4 - 2b (Percentage as input)
Percentage = int(input("Enter your discount (%) :  "))
Discount1 = (Price * Percentage) / 100
Final_Price1 = Price - Discount1
print(f"Final price is : {Final_Price1} kr \n")


# Assignment 5 - 1a
Distance_Km = 470

# Ask the user speed
Speed_Kmh = int(input("Enter your speed in km/h: "))

Total_Hrs = int(Distance_Km // Speed_Kmh)
print(f"Total hrs : {Total_Hrs:.2f} hrs")

#Assignment 5 - 1b
# Hours into minutes
Minutes = Total_Hrs * 60
print(f"Total minutes : {Minutes:.0f} minutes") # (0 decimal digits after number and round of the floating point no to integer)

#Assignment 5 - 1c - Extract whole hrs using int
Hours = int(Distance_Km // Speed_Kmh)  # // gives the whole number

#Extract minutes
Minutes1 = int(Total_Hrs % 60)  # % gives reminder

print(f"It will take {Hours} hours and {Minutes1} minutes to drive \n")

# Comparison of the hrs using ==
print("The comparison of two answers is same : " , int(Total_Hrs) == int(Hours) , "´\n")


# Calculate the length of the hypotenuse of a right triangle
#Formula used c = sqrt{a^2 + b^2}
def calculate_hypotenuse():
    try:
        Side_A = float(input("Length of a =  ")) #with decimal value
        Side_B = float(input("Length of b =  "))

# Calculate c^2
        Length_of_c_sqrt = (Side_A ** 2 + Side_B ** 2)
        print(f"c^2 = {Length_of_c_sqrt:.2f}")

# Calculate c
        Side_C = float(Length_of_c_sqrt) ** 0.5
        print(f"Length of c = {Side_C:.2f} - calculated without math.sqrt \n")


#Calculate c length with math.sqrt
        c = math.sqrt(Side_A**2 + Side_B**2)
        print(f"Length of hypotenuse  = {c:.2f} - calculated with sqrt function \n")

# Comparison of two values
        print("The comparison of two type answers is same : " , float(Side_C) == float(c) , "\n")

    except ValueError:
        print(" Enter a valid number \n")

calculate_hypotenuse()


# Current Date
today = date.today()
print(f"Today's date : {today}")
#after 7 days date
future_Date = today + timedelta(days=7)
print(f"Future date : {future_Date} \n")

#to avoid terminal closing
input("All programs finished! Press Enter to close this window...")






