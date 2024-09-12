number = int(input("enter grade number:"))
if number >= 90 and number <= 100:
    grade = "A"
elif number >= 80 and number <= 89:
    grade = "B"
elif number >= 70 and number <= 79:
    grade = "C"
elif number > 100 or number < 0:
    grade = "Error: Grade must be between 100 and 0"
else:
    grade= "F"
    
print ("The letter grade is:", grade)

thesum= 0
for count in range (1,10):
    thesum += count
    print (thesum)

thesum = 0
count = 1
while count <=10:
    thesum += count
    count += 1
    print (thesum)