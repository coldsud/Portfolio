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