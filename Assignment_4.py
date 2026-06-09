# 1a - test will be printed as string "Hello" is passed into t and the func() executes print(test).
import numbers


def foo(t):
    print("test")

foo("Hello")

#-----------------------------------------------------------------------------------------

# 1b - it prints  X , Y - then result will be 3, 5

def fun1(x, y):
    return x * y

print(3, 5)

#-----------------------------------------------------------------------------------------

# 1c - result will be 15. It calls the fun1() and it returns x * y

def fun1(x, y):
    return x * y

print(fun1(3, 5))

#-----------------------------------------------------------------------------------------

# 1d -

def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

#-----------------------------------------------------------------------------------------

# 1e - 7 is the answer. a = 5 is a global variable and a += 1 is local variable. local variable is not used.
# Only global variable is added with 2 & printed.

a = 5
def for3(a):
    a += 1

a += 2
print(a)

#-----------------------------------------------------------------------------------------

# 1f - answer is 18.
# 1. goo(foo , 3) - x is foo and y is 3, return x(y), so it is foo(3)
# 2. Now foo fun() passes 3 as i, 2 * 3 * 3 = 18

def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);    # semicolon allowed in python.
print(a)

#-----------------------------------------------------------------------------------------

# 1g - is_number() checks whether the input x is either an integer or a float.
# If it is either of int or float it returns True else False.
# Code can be simplified to one fun make it looks more clear and simple

def is_number(x):

    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))


#simpler version of 1g.

def is_number(x):
    return isinstance(x, (int, float))

print(is_number(5.5))
print(is_number(42))

#-----------------------------------------------------------------------------------------

# 1h - avarage_words() checks the words length, and it checks the words greater than 4 and less than 8.
# Words which pass the condition appended and stored in found.
# the ans is ["how's", "going", "coding"].

def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])


#-----------------------------------------------------------------------------------------

# 1i - to find the smallest number in the list
# It try to find the smallest number by looping through the list in a variable called counter

def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])      # answer is -11
find_min([])                    # answer is 0 as counter = 0
find_min([100])                 #  answer is 0 as (100 < 0 - no)

#-----------------------------------------------------------------------------------------

# new way

def find_min1(numbers):

    # Handling empty list

    if not numbers:
        print("List is empty")
        return None

    #initializing the input as smallest number
    smallest = numbers[0]
    for item in numbers:
        if item < smallest:
            smallest = item

    print(f"The smallest number is: {smallest}")
    return smallest

find_min([10, 3, -4, -11])          # answer is -11
find_min([])                        # answer is "List is empty"
find_min([100])                     # answer is 100 (if 100 < 100)


#-----------------------------------------------------------------------------------------

