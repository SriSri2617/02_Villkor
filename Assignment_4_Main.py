import Assignment_4_Modules
import Assignment_4_TheGame21

# 1 . func() that takes string as a parameter

print("program # 1")
Assignment_4_Modules.my_name("Mathumitha")

#---------------------------------------------------------------------------------

# 2a . func() that print the string twice

print("program # 2a")
Assignment_4_Modules.echo("Python")

#---------------------------------------------------------------------------------

# 2b . adding a parameter "count" to decide the no.of times to print the string

print("program # 2b")
Assignment_4_Modules.echo_times("Python", 4)

#---------------------------------------------------------------------------------

# 3. loop should stop at 5 iterations

print("program # 3")
Assignment_4_Modules.loop_times()

#---------------------------------------------------------------------------------
# 4 . Function name last() - takes list as a parameter and return the last number in the list

# user enter the list
print("program # 4")
list_of_numbers = input("Enter numbers with commas (2,3,..): ")

print(f"The list is : {list_of_numbers}")

# changing the list into real python list
list1 = list_of_numbers.split(",")

#pass the list into fun last()
last_number = Assignment_4_Modules.last(list_of_numbers)

if last_number == "There is only one number":
    print("The list has only one number \n")

else:
    print(f"The last number  : {last_number} \n")


#---------------------------------------------------------------------------------

# 5. fun cut_edges() - parameter is list, and it removes the first and last elements in the list

print("program # 5")
# input
list_of_numbers1 = input("Enter input with commas: ")

print(f"The list is : {list_of_numbers1}")

# changing the list into real python list
list2 = list_of_numbers1.split(",")

# pass the list into fun last()
cut_edges = Assignment_4_Modules.cut_edges(list2)

if cut_edges == "The list too short to cut the edges":
    print("The list has only two numbers \n")

else:
    print(f"List after the removal of first & last numbers  : {cut_edges} \n")


#---------------------------------------------------------------------------------

# 6. resolve the error

print("program # 6")
print(Assignment_4_Modules.increase(1), "\n")


#---------------------------------------------------------------------------------#

# 7. fun average returns the average of 2 numbers

print("program # 7")
x = input("Enter a x: ")
y = input("Enter a y: ")
print("Average of x & y :", Assignment_4_Modules.average(x, y), "\n")

#---------------------------------------------------------------------------------

# 8. pretty print function

print("program # 8")
user_list = input("Enter a list separated by commas (2,3,..): ")

# check if the user input is empty
if user_list == "":
    my_list = []

else:

    my_list = user_list.split(",")

print("")
Assignment_4_Modules.pretty_print(my_list)

#---------------------------------------------------------------------------------

# Game 21 - version 1

print("")

numbers, total = Assignment_4_TheGame21.game21()

# Print the full expression like: 1 + 2 + 3 + 4 + 5 + 6 = 21
print("+".join(str(x) for x in numbers), "=", total, "\n")


# Game 21 - version 2 random nos

numbers, total = Assignment_4_TheGame21.game21_random()
print("cards : ", numbers)
print("total : ", total, "\n")













