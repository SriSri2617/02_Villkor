from Assignment_2 import discount_program, height_program, championship_league, temp_conversion

#Choose which program to run
print("1. Discount Program")
print("2. Height check to ride")
print("3. Championship League")
print("4. Temperature Conversion")
program_to_run = input("Choose a program to run (1/2/3/4) : ")
if program_to_run == "1":
    discount_program()
elif program_to_run == "2":
    height_program()
elif program_to_run == "3":
    championship_league()
elif program_to_run == "4":
    temp_conversion()
else:
    print("Invalid input")