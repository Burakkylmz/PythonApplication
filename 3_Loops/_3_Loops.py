
#############
#While Loops#
#############

print("1.Example")
i = 0
while i < 6:
    print(i)
    i += 1

print("--------------")

print("2.Example")
number = [1,2,3,4,5]
index = 0
while (index < len(number)):
    print(number[index])
    index++


"""
in operator : The 'in' operator is used to check if a value exists in a sequence or not. Evaluates to true if it finds a variable in the specified sequence and false otherwise.

'not in' operator- Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
"""
#For example

5 in [1,2,3,4] #output is False because our list don't contain 5

2 in [1,2,3] #output is True

"t" in "Tesla"

"elo" in "elon musk"

not 4 in (1,2,3) # true

"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
"""
print("-----------------------")

#Printing numbers in a list

print("printing numbers in a list")
listOfNumber = [0,1,2,3,4,5,6,7,8,9]
for item in listOfNumber:
    print(item)

print("-----------------------")

#Calculating the sum of all elements of an array

print("calculating the sum of all elements of an array")
sum = 0
listOfNumber = [0,1,2,3,4,5,6,7,8,9]
for item in listOfNumber:
    sum = sum + item
print(sum)

print("------------------------------------")

#Adding numbers between two numbers by a given step amount
#Note: using start, stop, and step arguments in Python range() function

print("Adding numbers between two numbers by a given step amount")
print("using start, stop, and step arguments in Python range() function")
initialValue = int(input("Please type the initial value: "))
endValue = int(input("Please type the end value: "))
stepValue= int(input("Please type step value: "))
sum = 0
for i in range(initialValue, endValue, stepValue):
    sum += i;
print(sum)

print("------------------------------------")

#Calculating a given exponent strength
baseValue = int(input("Type the  base value: "))
exponentValue = int(input("Type the exponent value: "))
result = 1
for i in range(1, exponentValue):
    result *= baseValue
print(result)

print("------------------------------------")





