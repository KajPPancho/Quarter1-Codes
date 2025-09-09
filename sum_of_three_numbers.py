num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

rnum1 = round(num1, 2)
rnum2 = round(num2, 2)
rnum3 = round(num3, 2)

sum = rnum1 + rnum2 + rnum3

print("first number is" ,rnum1)
print("second number is" ,rnum2)
print("third number is" ,rnum3)
print("Sum of three numbers is", round(sum, 2))