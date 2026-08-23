# 1. WAPP to enter and check if the number is EVEn or ODD
#n = int(input("Enter your number: "))
#if n % 2  == 0 :
 #   print(n,"is EVEN")
#else:
 #   print(n, "is ODD")

# 2. WAPP to check the number is POSITIVE , NEGATIVE , or ZERO
#Number = int(input("Enter the number: "))
#if Number > 0:
#    print(Number,"number is POSITIVE")
#elif Number < 0:
#    print(Number,"number is NEGATIVE")
#else:
#    print(Number,"number is ZERO")        

# 4. WAPP to input total marks out of 100 and print "PASS" if the marks in the subject is above 40. If marks is less than 40 then print "FAIL".
#marks = int(input("Enter the marks: "))
#if marks >= 40:
#    print("PASS")
#else:
#    print("FAIL")   

# 5. WAPP to print Square if the number is EVEN else print Square Root if the number is ODD.
#n = int(input("Enter a number: "))
#if n % 2 == 0:
#    print(n**2," EVEN number")
#else:
#    print(n**0.5," ODD number")    

# 6. WAPP to calculate BMI of a persom and classif the person as "Overweight","Underweight" and "Normal".
# BMI = Weight(kg)/Height(m)
#weight = float(input("Enter your weight: "))
#Height = float(input("Enter your height: "))
#BMI = weight/Height
#print(f"Your BMI is {BMI}")
#if BMI < 18.5 :
#    print("Underweight")
#elif (18.5 <= BMI < 24.9):
#    print("Normal")
#else:
#    print("Overweight")        

# 7. WAPP to enter angle of a triangle and print if the angle are acute, obtused or right angled.
a = int(input("Enter the first angle of triangle: "))
b = int(input("Enter the second angle of triangle: "))
c = int(input("Enter the third angle od triangle: "))

if (a + b + c == 180):
    if a > 90 or b > 90 or c > 90:
        print("OBTUSHED ANGLE")
    elif a == 90 or b == 90 or c == 90:
        print("RIGHT ANGLE")
    else:
        print("ACUTE ANGLE")
else:
    print("Invaild angles")                

