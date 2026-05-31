# 1 - What is printed
print("While loop test")
limit = 15
index = 5
while index <= limit:
    print(index)
    index = index +2
print("")

#-------------------------------------------------------------------------------------------------#

# 2 - What is printed
print("for loop test")
for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
        i = i + 1
print("")

#---------------------------------------------------------------------------------------------------#

# 3 - What will be the sum
print("Program 3")
counter = 0
for i in range(6):
     counter += i
print(counter)
print("")

#-------------------------------------------------------------------------------------------------#

# 4 - What is printed
print("Program 4")
x = 0
y = 1
while x < 10:
    if y % 2 == 0:
        x -= y
    else:
        x += y * y
    y += 1
print("")

#-------------------------------------------------------------------------------------------------#

# 5 - what is printed
print("Program 5")
message = "Its_time_to_get_coding"
print(message[3:7], "\n")

#-------------------------------------------------------------------------------------------------#

# 6 - what is printed
print("Program 6")
for pos in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == pos:
            s += "#"
        else:
            s += "."
    print(s)





