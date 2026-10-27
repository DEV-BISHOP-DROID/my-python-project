#The main types of operators
#arithmetic operators - simple calculations


x = 90
y =5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) #Modulus-divides the values and returns the remainder as the value
print(x % y)

#Comparison Operators - compare values and return boolean
num1 = 45
num2 = 20
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2) #equal to
print(num1 != num2) # not equal to

#Assignment Operators - Store values in variables
number = 80

#Operator Precedence
number %= 2
print(number)

#Logical Operators - and, or, not. used in scenario where more than one condition is required to determine n answer/output
print(100==50 and 60 < 80) #and if all the condition is true
print(100==50 or 60 < 80) # or if one of the condition is true
print( not(100==50 and 60 < 80)) #gives the opposite