__### Week One Python CODE CYSE 250__ 


## chapter 1

## _ExO 1_ 

```# Write your code here

name = "Isaac"
address = "Harrisonburg va"
phone = "(540 551 xxxx)"

print (name)
print (address)
print (phone)
```


## _ExO 2_

```# Write the code here
width = float(input ("Enter the width: "))
height = float(input("Enter the height: "))
area = width * height
print ("The Area is", area, "square units.")
```
## _Ex0 3_

```# Write your code here
width = float(input ("Enter the width: "))
height = float(input("Enter the height: "))
area = width * height
print ("The area of a this triangle is", area * .5, "square units.")
```
## _Ex0 4_

 ```# Write your code here

radius = float (input("Input Circle Radius: "))
currentrad = int(radius)
area = 3.14 * radius ** 2
print ("the area of a circle with a radius of",currentrad, "is", area, "square units")
```
## _Ex0 5_

```# Write your program here
width = float(input ("Enter the width: "))
height = float(input("Enter the height: "))
depth = float(input("Enter the depth: "))
volume = width * height * depth
print ("The Area is", volume, "cubic units.")
```

## _ex2-1_

Rounding formula to get an output to an exat decimal place


```
Roundnum = round(number to be rounded, to what dcimal place)
```
### example
`rounded_number = round(3.14159, 2)
print(rounded_number)`


## _ex2-2_

### Write code that will calculate the surface area of a cube

```# Write your program here
edge = float(input("Input Edge length"))

cubearea = ( (edge * edge) * 6)

print ("cube surface area is", cubearea , "square units")
```

_ex2-3_

~~~
# Write your program here
newbie = float(input("Enter new video count: "))
oldie = float (input ("Enter old video count: "))

tnewbie = (3.00 * newbie)
toldie = (2.00 * oldie)
# this section  (${:.2f}",format) rounds the output to two decimal points and adds a dollar sign
print ("${:.2f}".format(tnewbie + toldie))
~~~
### Note*
This section of code is what formats the output to round to two decimal places and adds a dollar sign to the front of the output.

`"${:.2f}".format`

Also you can round a variable to any amount of decimal places with this below code. the number is the amount decimal places

`rounded_variable = round(variable_to_round, 2)`


## **_ex2-4_**

```
# Write your program here

radius = float(input("Enter sphere radius: "))

diameter = (2 * radius)

circumference = (2 * 3.141592653589793 * radius)

surface_area = (4 * 3.141592653589793 * radius ** 2)

volume = ( 4/3 * 3.141592653589793 * radius ** 3)

#left these rounded values for future reference if round values are needed for these formulas
diameter2 = round(diameter, 2)

circumference2 = round(circumference, 2)

surface_area2 = round(surface_area, 2)

volume2 = round(volume, 2)

print (diameter)
print (circumference)
print (surface_area)
print (volume)
```

## **_ex2-5_**

### Simple code for calculating momentum

```
# Write your program here
mass = float(input("Enter Object's Mass: "))
velocity = float(input("Enter Object's Velocity: "))

Momentum = (mass * velocity)

print ("The" , mass ," kilogram Object is traveling at a Velocity of: ", velocity , "meters per seceond, which would give its Momentum to be: ", Momentum)
```

## **_ex2-6_**

### Incorporates code from ex2-5

```
# Write your program here
mass = float(input("Enter Object's Mass: "))
velocity = float(input("Enter Object's Velocity: "))

Momentum = (mass * velocity)

print ("The" , mass ," kilogram Object is traveling at a Velocity of: ", velocity , "meters per seceond, which would give its Momentum to be: ", Momentum)

KE = ( 1/2 * mass * velocity ** 2)

print ("The numerical representation of Kinetic Energy of the Object is: " , KE )
```


## **_ex-2-7_**

This excercise had issues where i needed to convert a float to an integer to not get an 0.0 error in python

```
# Write your program here
years = float(input("Enter how many years: "))


# this next line of code converts float to interger. 
# The round funtion without any switches will round to the nearest integer
yearsrnd = int(round(years))

minperyr = 525600

minperyrrnd = round(minperyr,0)

minelapsed = (minperyrrnd * yearsrnd)

print ("minutes elapased in time frame is:", minelapsed)
```

## **_ex2-8_**
Add this command to your code to get it to output intergers. it will prevent output like this `4.7304e+16`

>`print (int(variable))`

```
# Write your program here
years = float(input("Enter Years: "))

lyt = ((3e8) * (31536000))

lyty= (lyt * years)

print ("Distance traveled: ",(int(lyty))) 
print
```

## **_ex2-9_**

```
# Write your program here
# Nautical miles for this is calculated by the blow code
nm = ((60 * 90) /10000 )


kilo= float(input("Enter Kilometers: "))

anm= kilo * .54

print ("Nautical Miles:" , (round(anm, 2)))
```

## **_ex2-10_**

```
# Write your program here
hourwage = float(input("Enter hourly wage: "))

reghours = float (input("Enter regular hours: "))

OT = float(input("Enter overtime hours: "))

finalwage = (OT * 1.5) * hourwage + (hourwage * reghours)

print ("Weekly pay: $",(round(finalwage, 2)))
```
 ## Chapter 2 Debugging Exercise

 The code had a few errors with the math and was missing a variable

 ```
 purchasePrice = float(input("Enter the purchase price as $: "))
taxRate = int(input("Enter the tax rate as %: "))
tax = purchasePrice * ((taxRate / 100) + 1)
taxtotal= tax - purchasePrice
totalOwed = tax
print("Purchase price: ", round(purchasePrice, 2))
print("Tax:            ", round(taxtotal, 2))
print("Total owed:     ", totalOwed)
```
## **_ex3-1_**

```
# Write your program here
side1= int(input("Enter first side:"))

side2= int(input("Enter second side: "))

side3 = int(input("Enter third side: "))

if side1 == side2 and side1 == side3:
    print ("The triangle is equilateral")
else:
    print ("triangle is not equilateral")
```

## **_ex3-2_**

```
side1 = int(input("Enter the first side: "))

side2 = int(input("Enter the second side: "))

side3 = int(input("Enter the third side: "))

if ((side1**2)+(side2**2)) == (side3**2):
    print ("The triangle is a right triangle")
else:
    print ("The triangle is not a right triangle")
```

## **_ex3-3_**

```
# Get the smaller and larger numbers from the user
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

# Initialize count and bounds
count = 0
low = smaller
high = larger

# The computer now tries to guess the number
while low <= high:
    guess = (low + high) // 2  # Guess the middle of the current range
    count += 1
    print(f"{low} {high}")
    print(f"Your number is {guess}")

    user_input = input("Enter =, <, or >: ")  # Get feedback from the user

    if user_input == "=":
        print(f"Hooray, I've got it in {count} tries!")
        break
    elif user_input == "<":
        high = guess - 1  # Adjust the upper bound
    elif user_input == ">":
        low = guess + 1  # Adjust the lower bound

# If the loop ends without finding the number, print cheating message
if low > high:
    print("I'm out of guesses, and you cheated!")
```

Certainly! Here’s a Markdown-friendly guide for your code. You can copy and paste it directly into VS Code, and it will format nicely.

```markdown
# Code Breakdown: Number Guessing Game

This guide explains a Python program where the computer tries to guess a number based on user input. Let's break down the code step by step.

## 1. Getting User Input

The program starts by asking the user to provide two numbers: a smaller and a larger number.

```python
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
```

- `smaller`: The lower bound of the range.
- `larger`: The upper bound of the range.

## 2. Initializing Variables

Next, the program initializes three variables:

```python
count = 0  # Keeps track of how many guesses have been made
low = smaller  # The current lower bound
high = larger  # The current upper bound
```

- `count`: Tracks the number of guesses.
- `low`: Initially set to the smaller number.
- `high`: Initially set to the larger number.

## 3. Binary Search Loop

The core of the program is a **while loop**, which implements a binary search to guess the user's number.

```python
while low <= high:
    guess = (low + high) // 2  # Guess the middle of the current range
    count += 1
    print(f"{low} {high}")
    print(f"Your number is {guess}")
```

- **Binary Search**: The computer guesses the number by calculating the midpoint between `low` and `high`.
- The program prints the current bounds (`low` and `high`) and the current guess.

## 4. Getting User Feedback

After making a guess, the program asks for feedback from the user:

```python
user_input = input("Enter =, <, or >: ")
```

- `=`: The guess is correct.
- `<`: The guess is too high, so the computer will narrow the range by adjusting the upper bound.
- `>`: The guess is too low, so the computer will adjust the lower bound.

## 5. Adjusting the Range Based on Feedback

The program adjusts the bounds depending on the user's feedback:

```python
if user_input == "=":
    print(f"Hooray, I've got it in {count} tries!")
    break
elif user_input == "<":
    high = guess - 1  # Narrow the upper bound
elif user_input == ">":
    low = guess + 1  # Narrow the lower bound
```

- If the user enters `"="`, the program announces that it guessed the number and exits the loop.
- If the user enters `"<"`, the upper bound is set to one less than the guess.
- If the user enters `">"`, the lower bound is set to one more than the guess.

## 6. Cheating Check

If the loop exits and the bounds (`low > high`) are invalid, it means the user provided inconsistent feedback, and the program concludes they cheated:

```python
if low > high:
    print("I'm out of guesses, and you cheated!")
```

This handles the scenario where the user's feedback is impossible, i.e., the number can't be guessed within the provided bounds.

## Summary

This program uses a binary search approach to guess the number the user is thinking of. It adjusts the range based on the user's feedback (`=`, `<`, or `>`) until it guesses the correct number or determines the user is cheating.

### Key Concepts:
- **Binary Search**: Efficiently guessing numbers by halving the search range each time.
- **User Feedback**: Input-driven adjustments to the guessing logic.
```

You can paste this into your Markdown file in VS Code, and it should render nicely. Let me know if you'd like any further adjustments!
```

## **_ex3-4_**

```
inittheight= float(input("Enter the height from which the ball is dropped: "))

initbounce= float(input("bounciness index of the ball: "))

allowbounce= int(input("Enter the number of times the ball is allowed to continue bouncing: "))

tdistance = inittheight

for i in range(allowbounce):
    
    inittheight *= initbounce
    
    tdistance += inittheight * 2

if allowbounce > 0:

    tdistance -= inittheight
    
    print(f"Total distance traveled by the ball: {tdistance:.6f}")
```

## **_ex3-5_**

```
init = (float(input("Enter the initial number of organisms: ")))

rgro = (float(input("Enter the rate of growth [a real number > 1]: ")))

hours = (float(input("Enter the number of hours to achieve the rate of growth: ")))

tours = (float(input("Enter the total hours of growth: ")))

import math

tpop = math.floor(init * (rgro**(tours / hours)))

print (f"After {tours} hours, The total population is : {tpop}")
```


## **_ex3-6_**

```
iters = int(input("Enter the number of iterations: "))

rpie = 0

for n in range(iters):

    rpie += ((-1) ** n) / (2 * n + 1)

rpie *= 4

print(f"The approximation of pi is : {rpie}")
```

## **_ex3-7_**

```
start = float(input("Enter the starting salary : "))

incr = int(input("Enter the annual % increase : "))

years = int(input("Enter the number of years : "))

pincr= incr / 100

rsal= start

for n in range(1, years + 1):

    print(f"Year {n}: Salary: {rsal:.2f}")

    rsal += rsal * pincr
```

## **_ex3-8_**
```
small = int(input("Enter the smaller number : "))

large = int(input("Enter the larger number : "))

def gcd(small, large):
    while large != 0:
        small, large = large, small % large
    return small

print(f"The greatest common divisor is {gcd(small, large):.0f}")
```

## **_ex3-9_**

```
total = 0

count = 0

while True:

    usernum = (input("Enter a number or press Enter to quit: "))

    if usernum == "":

        break

    nu1 = float(usernum)

    total += nu1

    count += 1

average = total/count

print("The sum is " , total)

print("The average is " , average)
```

## **_ex3-10_**
```
def tidbit_credit_plan(purchase_price):
    # Credit plan details
    down_payment_rate = 10  # 10% down payment
    annual_interest_rate = 12  # 12% annual interest rate
    monthly_payment_rate = 5  # 5% of the listed purchase price

    # Calculate initial values
    balance = purchase_price * (1 - down_payment_rate / 100)
    monthly_payment = purchase_price * (monthly_payment_rate / 100)

    # Print header for table
    print("{:<5} {:<20} {:<20} {:<20} {:<15} {:<20}".format(
        "Month", "Starting Balance", "Interest to Pay", "Principal to Pay", "Payment", "Ending Balance"
    ))

    # Calculate and display details for each month
    month = 1
    while balance > 0:
        interest = balance * (annual_interest_rate / 100) / 12
        principal = monthly_payment - interest
        payment = min(monthly_payment, balance)
        ending_balance = balance - payment

        # Print the details for the month
        print("{:<5} {:<20.2f} {:<20.2f} {:<20.2f} {:<15.2f} {:<20.2f}".format(
            month, balance, interest, principal, payment, ending_balance
        ))

        # Update balance and month
        balance = ending_balance
        month += 1

# This will run provide the table now
purchase_price = float(input("Enter the purchase price: "))
tidbit_credit_plan(purchase_price)
```
## **_ex3-11_**

```
import random

def lucky_sevens(starting_amount):
    pot = starting_amount
    rolls = 0
    max_pot = pot
    max_roll = 0

    while pot > 0:
        rolls += 1
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == 7:
            pot += 4
        else:
            pot -= 1.0

        if pot > max_pot:
            max_pot = pot
            max_roll = rolls

    print(f"You are broke after {rolls} rolls.")
    print(f"You should have quit after {max_roll} rolls when you had ${max_pot}.")


starting_amount = float(input("How many dollars do you have? "))
lucky_sevens(starting_amount)
```

## **_Chapter 3 Debugging Exercise_**

```
count = 1
total = 0
while count <= 10:
    score = int(input("Enter test score number " + str(count) + ": "))
    total = total + score
    count = count + 1
average = total / 10
print("The average test score is", average)
```
