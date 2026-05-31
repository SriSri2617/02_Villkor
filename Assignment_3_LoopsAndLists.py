# 1a -  Complete the code and the answer should be 55

print(" Program 1")
answer = 0
for i in range(1, 11):
    answer += i
print("The sum of numbers 1 to 11 is : " + str(answer) + "\n")

#____________________________________________________________________________________________

#1b. Calculate the sum of all numbers between 1 and 100. (including 1 and 100, the correct answer should be 5050)

total = 0
for i in range(1, 101):
    total += i
print("The sum of all numbers from 1 to 100 : " + str(total) + "\n")

#____________________________________________________________________________________________

# 1c.Rewrite 1b so that it uses a while loop.
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print("The sum of all numbers from 1 to 100 : " + str(total) + "\n\n")

#____________________________________________________________________________________________

# 2. Calculate the sum of all elements in the list:[1, -2, 3, -2, 4, -3]

print("Program 2 - List")
list = [1, -2, 3, -2, 4, -3]
total = sum(list)
print("The sum is : " + str(total) + "\n\n")

#____________________________________________________________________________________________

# 3a. Create a list with the names of four movies. The names should be strings. Print the entire list using the print function.

print("Program 3 - Movie names")

movie_names = ["The Lion King", "Toy Story", "Shrek ", "Finding Nemo"]
print(movie_names, "\n")

# 3b. Add "Fellowship of the ring" to the last of the list.
movie_names.append("Fellowship of the ring")
print(movie_names, "\n")

#3c. Add "The two towers" to the first place in the list. (index zero)
movie_names.insert(0, "The two towers")
print(movie_names, "\n")

#3d Find out what position (index) "Fellowship of the ring" now has.
position = movie_names.index("Fellowship of the ring")
print("The position of the movie - Fellowship of the ring is : ", str(position), "\n")

#3e Remove another of the movies. Has the Fellowship movie changed index?
movie_names.remove("The two towers")
print(movie_names, "\n")

# Checking again the index of Fellowship of the ring
current_position = movie_names.index("Fellowship of the ring")
print("The current position of the movie - Fellowship of the ring is : ", str(current_position), "\n")

#3f. Find out how long the list is. (only)
print("The length of the list is : ", len(movie_names), "\n")

#3g Turn the list backwards.
movie_names.reverse()
print("The reverse list is : ", movie_names,  "\n")

#3h Sort the list in ascending alphabetical order.
movie_names.sort()
print("The alphabetical order of - movie names : ", movie_names, "\n\n")

#____________________________________________________________________________________________

# 4a. Write a program that repeatedly asks the user to enter a number. When the user enters the string "quit" or "end", the program should calculate the sum of the numbers

def receipt_calculator():
    print("Program 4 \n")
    print("Welcome to kvittokompis!  Quit by typing: quit \n")
    total_amt = 0
    amt = ""
    while amt != "quit":
        amt = input("Enter the amount : ")
        if amt == "quit":
            print("It's " + str(total_amt) + " sek in total. Welcome back! \n")
            break
        amt_int = float(amt)
        total_amt += amt_int


    # Version 2: the program should ask how many people there are, and tell how much each person in the party should pay.

    while True:
        no_of_persons = input("Enter the number of persons: ")
        try:
            persons_int = int(no_of_persons)
            if persons_int <= 0:
                print("No of persons atleast 1 \n")
                continue
            break
        except ValueError:
            print("Enter a valid integer")

    amt_sharing = total_amt // persons_int
    print("It's " + str(total_amt) + " sek in total, or " + str(amt_sharing) + " sek per person. Welcome back! \n")


    # Version 3: the program should ask how many percentage tips to add. If the user does not type anything (empty string), the program should use 10% as the default.

    percentage = input("Enter tip percentage (press enter for 10%) : ")

    if percentage == "":
        tip_percentage = 10
        print("Tip is 10%")
    else:
        tip_percentage = float(percentage)

    tip_amt = total_amt * (tip_percentage / 100)
    print("The tip amount : " + str(tip_amt) + " sek \n")

receipt_calculator()

#____________________________________________________________________________________________


