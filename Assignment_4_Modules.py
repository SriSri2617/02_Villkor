# 1. func() that takes string as a parameter

def my_name(name):
    print(f"{name} learning python \n")

#---------------------------------------------------------------------------------

# 2a. func() that print the string twice

def echo(echo):
    print(echo * 2, "\n")

#---------------------------------------------------------------------------------

# 2b. adding a parameter "count" to decide the no.of times to print the string

def echo_times(echo1, count):
    for i in range(count):
        print(echo1, "\n")

#---------------------------------------------------------------------------------

# 3. loop should stop at 5 iterations

def loop_times():

    end = 5     # end value
    y = 1

    for x in range(1, 100):
        y *= 2
        print(f" Loop number : {x} and value is : {y} \n")

    # end the loop with an if statement here
        if x == end:        # check if the loop number x matches the end value
            break

    print(f"Final value of loop number : {x} is : {y} \n")


#---------------------------------------------------------------------------------

# 4. Function name last() - takes list as a parameter and return the last number in the list

def last(list_of_numbers):

    # check if the list has more than 1 element
    if len(list_of_numbers) >= 2:
        return list_of_numbers[-1]
    else:
        return "There is only one number"


#---------------------------------------------------------------------------------

# 5. fun cut_edges() - parameter is list, and it removes the first and last elements in the list

def cut_edges(list):

    # check if the list has more than 2 elements
    if len(list) > 2:
        return list[1 : -1]
    else:
        return "The list too short to cut the edges"

#---------------------------------------------------------------------------------

# 6. Resolve the error - the error is logical error and often called "unreachable code"
    #   def increase(x):
        #     return x
        #     x += 1
    # print(increase(1))
# "x += 1" - above the return
# any code inside the fun after return will never run

def increase(x):
    x += 1
    return x

#---------------------------------------------------------------------------------

# 7. fun average returns the average of 2 numbers

def average(x , y):

    # checking the user input is only number
    try:
        no1 = int(x)
        no2 = int(y)
        total = no1 + no2
        z = total / 2
        return z
    except ValueError:
        print("Enter numbers  only \n")
        return None

#---------------------------------------------------------------------------------

# 8. pretty print function

def pretty_print(user_list):

    # check the list is empty
    if len(user_list) == 0:
        print("The list is empty \n")
    else:
        print(f"The list has : {len(user_list)} elements\n")

        # enumerate keeps track of both the counting number (index) and the actual value (item).
        # start=1 ensures the list numbers print out as 1, 2, 3 instead of starting at 0.
        for index, item in enumerate(user_list , start=1):
            print(f"{index}. {item}")

#---------------------------------------------------------------------------------
