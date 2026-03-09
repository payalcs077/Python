# x = 12
# y = x
# z = 13867556433422554432
# print(id(x))
# print(id(z))
# AGE = 18
# AGE = 23
# print(AGE)
# 1name = "Error"


# calculator
a = int(input())
b = int(input())

print(a+b)
print(a - b)
print( a * b)
print( a / b)
print( a // b)
print( a ** b)

# km to meter converter
km = float(input("Enter distance in kilometers: "))
meter = km * 1000
cm = meter * 100
print("Value in meter : ", meter)
print("Value in centimeter:", cm)

# celsius to farenheit
celsius = int(input("Value of temperature in celsius :"))
farenheit = celsius * (9/5) + 32
print("Value in farenheit:",farenheit)

# GB to MB to KB converter
gb = int(input("Enter val in GB:"))
mb = gb * 1024
print("Value in mb:", mb)
kb = mb * 1024
print("Value in kb:", kb)

# area of triangle

base = int(input("Enter base value:"))
height = int(input("Enter height value:"))
area = (1/2) * base * height
print(area)

# area of circle
radius = int(input("Enter radius value: "))
area = 2 * 3.14 * radius * radius
print("Area of circle : ", area)

# area of square
side = int(input("Enter value of side: "))
area = side * side
print("Area of square: ",area)
