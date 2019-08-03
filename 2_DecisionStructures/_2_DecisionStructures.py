
#Application to find out whether the number entered on the keyboard is odd or even

number = int(input("Please type a number: "))

if (number % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")

print("---------------------------------------")

#Comparing two entered numbers (greater or smaller or equality)

numberOne = int(input("Please type a number: "))
numberTwo = int(input("Please type a number: "))

if (numberOne > numberTwo):
    print("{} > {}".format(numberOne,numberTwo))
elif (numberOne < numberTwo):
    print("{} < {}".format(numberOne,numberTwo))
else:
    print("{} = {}".format(numberOne,numberTwo))

print("---------------------------------------")

#Simple note calculation

note = float(input("Please type a note: "))

if (note >=90):
    print("AA")
elif (note >= 80):
    print("BB")
elif (note >= 70):
    print("CC")
elif (note >= d0):
    print("DD")
else:
    print("FF")

print("---------------");


#Simple calculator 

print("--Operation Menu---")
print("Addition       --> 1")
print("Extraction     --> 2")
print("Multiplication --> 3")
print("Division       --> 4")
print("--------------------")

choice = input("Please select an action from the menu: ")

a = int(input("Please type a number: "))
b = int(input("Please type a number: "))


if (choice == "1"):
    print("{} + {} = {}".format(a,b,a+b))
elif (choice == "2"):
    print("{} - {} = {}".format(a,b,a-b))
elif (choice == "3"):
    print("{} x {} = {}".format(a,b,a*b))
elif (choice == "4"):
    print("{} / {} = {}".format(a,b,a/b))
else:
    print("Please select an action from the menu..!")

print("--------------------------------------------")

#Calculate Second Order Linear Equations

a = int(input("Type the first coefficient value  (a): "))
b = int(input("Type the second coefficient value (b): "))
c = int(input("Type the third coefficient value  (c): "))

delta = b ** 2 - 4 * a * c
x1 = (-b - delta ** 0.5 / (2 * a))
x2 = (-b + delta ** 0.5 / (2 * a))

print("First root: {}\nSecond root: {}\n".format(x1,x2))
