
#Simple Math

x = 1
y=3
z=5

x+y+z
x-y
x*y
x/z

print("-------------------------------------------")


#Calculate the Circumcircle of a triangle given the three sides

sideA = 3 # define a variable name is "sideA" than assigned into it a value of 3
sideB = 4 #In Python, the data type of a variable can be dynamically updated. In this case our sideB variable type is integer
sideC = 5

result = sideA+sideB+sideC #we calculated the circumference of the triangle and assigned it to the result variable

print(result) # "print" function in Python is a function that outputs

print("-------------------------------------------")

#Basic Math Operations

a = int(input("Please type a number: ")) #we asked the user to enter a value and assigned the value to the variable "a" of the integer type
b = int(input("Please type a number: ")) 

print("{} + {} = {}".format(a,b,a+b)) 
print("{} - {} = {}".format(a,b,a-b))
print("{} x {} = {}".format(a,b,a*b))
print("{} / {} = {}".format(a,b,a/b))

print("-------------------------------------------")

#Calcualte the Area of Retangle

smallEdge = int(input("Please type a length: "))
longEdge = int(input("Please type a length: "))

area= smallEdge * longEdge


print("Area of Retangle: ", area)

print("-------------------------------------------")


#Exponent Calculator

print(2**4)

base = int(input("Please type a number: "))
exponent = int(input("Please type a number: "))

result = base**exponent

print(result)

print("-------------------------------------------")

#Switch the value of two variables

a=3
b=4

a,b=b,a

print(a)
print(b)

print("-------------------------------------------")









