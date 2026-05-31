Assignment_2 <br />

All programs are implemented as separate modules using def() functions in Assignment_2.py.
input_functions file is for repeated functions and inputs, which is used in Assignemnt_2.py.

#1 - error program
```python
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

final_price = price * (100 - discount) / 100
print("Efter rebatter blir priset... " + final_price)
```

1. In the above code is_memeber = false not used
2. else..also missing
3.  print("Efter rebatter blir priset... " + final_price) - wrong syntax

---------------------------------------------------------------------

#2 - To ride Balder at Liseberg you must be 130 cm tall. Write a program that can tell you if you can ride!

reason to test Test_Cases with 3 different values - Boundary Value Analysis testing

    - **121 cm**  → Below the boundary
        Result: You can't go  
        Explanation: 121 < 130, so the condition is false.

    - **130 cm**  → At the boundary
        Result: You can go  
        Explanation: 130 >= 130, so the condition is true.

    - **155 cm**  → Above the boundary
        Result: You can go  
        Explanation: 155 >= 130, so the condition is true. 

Boundary value analysis

| Test Value | Meaning         | BVA Category   | Expected Result |
|----------- |-----------------|----------------|-----------------|
| 121 cm     | Below the limit | Below boundary | You can't go    |
| 130 cm     | Exact limit     | On boundary    | You can go      |
| 155 cm     | Above the limit | Above boundary | You can go      |

This confirms that the condition `height >= 130` works correctly for all boundary cases

--------------------------------------------------------------------- 

#3 -  program that asks the user how many goals each team scored, and tells which team won.

3 different cases tested

    - Tottenham - goal more than Liverpool 
    - Liverpool - goal more then Tottenham
    - Both team has equal goals

And the program will tell you how many more goals the team won by using 
    
    goals_ahead = abs(tottenham - liverpool) 
- abs is used for absolute value of number - it removes the - sign and only gives + number

--------------------------------------------------------------------- 
 
#4 - Write a program that can convert a temperature in degrees Celsius to degrees Fahrenheit.

Formula for converting between temperature units: <br />
    - C = (F - 32) / 1.8 <br />
    - F = 1.8 * C + 32

Values tested with

| Celsius  | Fahrenheit |
|----------|------------|
|      0   | 32         |
|  -17.777 | 0          |
|   37.777 | 100        |
|    100   | 212        |

~~~python
    temp_choice = input("You want to enter the temperature in Fahrenheit or Celsius (Enter F or C) : ").upper()
~~~
    - upper() - is used to remove the case sensitive. It handles the lowercase automatically.

--------------------------------------------------------------------- 

#5 Calculators
if elif is used to find the largest and same numbers.

    - For finding the middle number - len() function is used -  this will count list of numbers entered.
    - // is used to leave the decimal point, list/2 is - finding the middle position


Tested with values

| number_1 | number_2 | number_3 | Biggest no | same numbers | Middle number |
|:--------:|----------|----------|:----------:|:------------:|:-------------:|
|    3     |    4     |    3     |     4      |     yes      |       4       |
|    56    |    0     |    5     |     56     |      No      |       0       |
|    5     |    6     |    6     |     6      |     yes      | no middle no  |

------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------
Assignment_3 <br />

1. While code loop test

~~~python

    limit = 15              - maximum value
    index = 5               - Starting number
    while index <= limit:   - repeat while index <= 15
        print(index)        
        index = index + 2   - increase by 2 each loop itreation      

~~~~

This loop starts at 5 and keeps adding 2 each time until it reaches 15.
It prints all odd numbers from 5 to 15.(5,7,9,11,13 & 15)

--------------------------------------------------------------------- 

2. for loop code test
~~~python
    
    print("for loop test")
    for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
        i = i + 1
~~~~        
It prints the numbers from 0 to 9 and instead of 5 it prints space. 
i range is 10, so it will print 10 numbers(0 to 9)
i == 5, then print empty line. So the result will be 0,1,2,3,4, 6,7,8,9

--------------------------------------------------------------------- 

3. What will be the sum?

~~~python

    counter = 0         - starts with value 0
    for i in range(6):  - loops through numbers 0 to 5 (range = 6), 6 numbers
        counter += i    - 0+1+2+3+4+5+6
    print(counter)      - 15
~~~

--------------------------------------------------------------------- 

6.

~~~python
   
    for and in range(1, 7):     - and is a keyword, it cannot be used a variable name 
    s = ""
    for x in range(1, 9):
        if x == and:            - and should be replace with variable name
            s += "#"
        else:
            s += "."
    print(s)

~~~~

--------------------------------------------------------------------- 

Assignment_LoopssAndLists_3 <br />

1a. Complete the code example and The answer should be 55

~~~~python

    answer = 0
    for i in ????????????:      - for i in range(1, 11):
    answer += i
    print("The sum of the numbers 1 to 10 is: " + str(answer))
~~~~

--------------------------------------------------------------------- 

1b.  Calculate the sum of all numbers between 1 and 100. (including 1 and 100, the correct answer should be 5050)

~~~~python

    for i in range(1, 101):    - in this loop run till 100 and exit and the sum will be 5050. 
~~~~

if for i in range(1, 100): - the loop will run till 99 and the sum will be 4950

--------------------------------------------------------------------- 

1c.  Rewrite 1b so that it uses a while loop

~~~~python
    
    while i <= 100:
    sum += i
    i += 1
~~~~
--------------------------------------------------------------------- 

3a. Create a list with the names of four movies. The names should be strings. Print the entire list using the print function.
    - print function 

3b.  Add "Fellowship of the ring" to the last of the list
    - append() function

3c. Add "The two towers" to the first place in the list. (index zero)
    - insert() function

3d. Find out what position (index) "Fellowship of the ring" now has.
    - index() function

3e. Remove another of the movies. Has the Fellowship movie changed index?
    - remove() function

3f. Find out how long the list is. (only)
    - len() function

3g. Turn the list backwards.
    - reverse() function

3h. Sort the list in ascending alphabetical order.
    - sort() function

--------------------------------------------------------------------- 

3 . Receipt calculator <br />
version 1 <br /> 
    - Uses a while‑loop to repeatedly ask the user for amounts.
    - Each input is first read as a string, then converted to an integer/float before being added to the total.
    - Typing "quit" stops the loop and prints the total sum.

version 2 <br />
The program first calculates the total amount from Version 1.
Then it uses a validation loop to ensure the user enters a valid integer for the number of people.
If the number is valid and at least 1, the program divides the total and prints how much each person should pay.

Key concepts <br />

    - while loop for repeated input
    - int conversion
    - input validation

version 2 <br />
After splitting the bill, the program asks for a tip percentage.
If the user presses Enter (empty input), the program automatically applies a 10% default tip.
If the user enters a number, it is converted to a float and used to calculate the tip amount.

Key concepts <br />

    - empty‑string check
    - float conversion
    - percentage calculation

--------------------------------------------------------------------- 



