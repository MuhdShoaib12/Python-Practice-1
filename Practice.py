# 1. WAPP to initialize two integers (10 and 25) to a variable and print the result after addition, subtraction, multiplication and division
a = 10
b = 25
print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)

print("-" * 100)
# 2. WAPP to print computed kinetic energy by the formula: KE = (1/2) * m * v^2 (Where m = 5kg, v = 10m/s).
m = 5  # mass in kg
v = 10 # velocity in m/s
KE = (1/2) * m * v**2
print("Kinetic Energy: ", KE)

print("-" * 100)
# 3. WAPP to print "Hello" 20 times. DO NOT USE print() 20 TIMES. BE SMART.
print("Hello\t" * 20)

print("-" * 100)
# 4. WAPP to print this statement:(It's Raining and I have an "Umbrella".)
print("It's Raining and I have an \"Umbrella\".")

print("-" * 100)
# 5. WAPP to find and print Area of a EquilateralTriangle
# 1. Equilateral Triangle Area. area = (3 ** (1/2) / 4) * (side ** 2)
side = 5 
Area = (3 ** (1/2) / 4) * (side ** 2)
print("Area of Equilateral Triangle: ", Area)
# 2. Isosceles Triangle Area: area = (b/4) * ((4*a**2) - b**2)**(1/2) 
a = 5 # Length of equal sides
b = 6 # Base length
Area = (b/4) * ((4*a**2) - b**2)**(1/2)
print("Area of Isosceles Triangle: ", Area)
# 3. Scalene Triangle Area: area = (s*(s-a)*(s-b)*(s-c))**1/2 where s = (a+b+c)/2
c = 3
s = (a+b+c)/2
Area = (s*(s-a)*(s-b)*(s-c))**1/2
print("Area of Scalene: " ,Area)

print("-" * 100)
# 6.WAPP to find the area, perimeter and diagonal of a rectangle. Take Length as 12 and breadth as 5
# Area of Rectangle : l * b
# Perimeter of Rectangle : 2(l + b)
# Diagonal of Rectangle : ((l**2) + (b**2))**1/2
l = 12
b = 12
print("Area of Rectangle: ", l * b)
print("Perimeter of Rectangle: ", 2*(l + b))
print("Diagonal of Rectangle: ", ((l**2) + (b**2))**1/2)

print("-" * 100)
# 7. WAPP to find the area and circumference of a circular ring whose outer and inner radii are 14 and 7.
# Area of Circle : 3.14 * ((R**2) - (r**2))
# Circumference : 2 * 3.14 * (R + r)
R = 14
r = 7
print("Area of Circle: ", 3.14 * ((R**2) - (r**2)))
print("Circumference: ", 2 * 3.14 * (R + r))

print("-" * 100)
# 8.WAPP to find the difference between Simple Interest and Compound Interest when Principle is ₹1000, Rate is 10% and Time is 5 years.
# Simple Interest : (P*R*T)/100
# Compound Interest : P*(((1 + (R/100))**T) - 1)
P = 1000
R = 10
T = 5
print("SI: ", (P*R*T)/100)
print("CI:", P*((1 + (R/100))**T - 1) )

print("-" * 100)
# 9. WAPP to find and print profit percent where selling price is ₹ 341 and Cost Price is ₹ 300.
# Profit Percentage Formula: (sp - cp) / cp  * 100
sp = 341
cp = 300
print("Profit: ", (sp - cp) / cp  * 100)

print("-" * 100)
# 10. WAPP to find and print displacement by using given formula where initial velocity is 20 m/s, time is 10s, and acceleration is 5 m/s**2
# s = (u*t) + (1/2 * a * t ** 2)
u = 20
t = 10
a = 5
print("Displacement: ", (u*t) + (1/2 * a * t ** 2))

print("-" * 100)
# 11. WAPP to display 3488 sec as hours, minutes and seconds in this format (hh:mm:ss)
s = 3488
h = s // 3600
s %= 3600
m = s // 60
s %= 60 
print(f"{h}:{m}:{s}")

print("-" * 100)
# 12. WAPP to input your name and age and print it in following format:
#I am [NAME] and my age is [AGE].
name = 'Shoaib'
age = 22
print(f"Name is {name} and Age is {age}")

