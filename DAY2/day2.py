# a = int(input("Enter a number: "))
# if a < 0:
#     print("Number is negative")
# elif a > 0:
#     print("Number is positive")
# else : 
#     print("Number is Zero")

# if a % 2 == 0:
#     print("number is even")
# else:
#     print("Number is odd")

# if a % 3 == 0 and a % 5 == 0:
#     print("Number is divisible by both 3 and 5")
# else : 
#     print(" Not divisible by 3 and 5")

# b = int(input("Enter second number "))
# c = int(input("Enter third number: "))

# if a>b and a>c:
#     print(f"{a} is greater")
# elif b>a and b>c :
#     print(f"{b} is greater")
# else :
#     print(f"{c} is greater")


# value = str(input("Enter a string: "))

# if value == 'a'or 'e' or 'i'or 'o'or 'u'or 'A'or 'E' or 'I' or 'O' or'U':
#     print(f"{value} is vowel")
# else :
#     print(f"{value} is consonant")

# attendance = int(input("Enter attendance in percentage:"))

# if attendance == 75:
#     print("Depends on the management whether you are eligible or not")
# elif attendance > 75:
#     print("You are eligible for placements")
# else:
#     print("You are not eligible for placements")


# a = int(input("Enter a number:"))
# if a>=10 and a<=99:
#     print("number is two digit")
# else:
#     print("number is not two digit")

# year = int(input("Enter a year: "))
# if year%4==0 and year%100 != 0:
#     print(f"{year} is a leap year")
# elif year % 400 ==0:
#     print(f"{year} is a leap year")
# else :
#     print(f"{year} is not a leap year")

# temp = int(input("Enter temperature value:"))
# if temp <= 15:
#     print("Temperature is cold")
# elif temp>15 and temp <= 30:
#     print("Temperature is moderate")
# else:
#     print("Temperature is hot")


# user = str(input("Enter username: "))
# password = str(input("Enter password: "))

# if user == 'admin' and password == 'password':
#     print("Login successful")
# else: 
#     print("Invalid credentials")

# side1 = int(input("Enter value of side1: "))
# side2 = int(input("Enter value of side2: "))
# side3 = int(input("Enter value of side3: "))

# if side1 + side2 >= side3:
#     print("Here is your triangle")
# elif side2 + side3 >= side1:
#     print("Here is your triangle")
# elif side1 + side3 >= side2:
#     print("Here is your triangle")
# else: 
#     print("Invalid values")

# if side3^2 == side1^2 + side2^2 or side1^2 == side2^2 + side3^2 or side2^2 == side1^2 + side3^2 :
#     print("It's a right angled triangle")
# else: 
#     print("It's not a right angled triangle")


a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")

else:
    if a == b == c:
        print("Equilateral Triangle")

    elif a == b or b == c or a == c:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")


