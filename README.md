README for Assignment_2
All programs are implemented as separate modules using def() functions in Assignment_2.py.
input_functions file is for repeated functions and inputs, which is used in Assignemnt_2.py.

These modules are imported and executed from main.py, where you can choose which program to run and test.

while true - is used to repeat the programs and to select the choice until user stop.

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

Formula for converting between temperature units:
    - C = (F - 32) / 1.8
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







