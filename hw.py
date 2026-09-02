# User se 2 numbers input lo aur print karo:

# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Remainder
# Power
 
# a=float(input("enter number1: "))
# b=float(input("enter number2: "))
# print("the addition is ",a+b)
# print("the subtraction is ",a-b)
# print("the multiplication is ",a*b)
# print("the division  is ",a/b)
# print("the Floor Division is ",a//b)
# print("the remainder of a  is ",a%b)
# print("the power of a   is ",a**b)



# User se ek integer input lo aur check karo ki number even hai ya odd.


# a=float(input("enter number: "))
# if a%2==0:
#     print("even")
# else:
#     print("odd")    


# Q3 — Positive, Negative or Zero

# a=int(input("enter number: "))
# if a>0:
#     print("this is positive number")
# elif a<0:
#      print("this is negative number")
# else:
#      print("this is zero ")     

# Q4 — Largest of Three

# a=int(input("enter number1: "))
# b=int(input("enter number2: "))
# c=int(input("enter number3: "))

# if a>=b and a>=c:
#     print("a is greater")
# elif b>=a and b>=c:
#     print("b is greater")
# elif c>=a and c>=b:
#     print("c is greater")
# else:
#     print("all are same numbers")            


# Q7 — String Analysis

# User se ek string input lo aur print karo:

# String ki length
# First character
# Last character
# String uppercase mein
# String lowercase mein


# str=str(input("Enter string"))
# print(len(str))
# print(str[0])
# print(str[-1])
# print(str.lower())
# print(str.upper())

# Q8 — Vowels Count

# User se ek string input lo aur usme total vowels (a, e, i, o, u) count karo.

# str=str(input("Enter string"))
# print(str.count())


# Q9 — List Operations

# Given:

# numbers = [10, 20, 30, 40, 50]

# Program likho jo:

# List mein 60 add kare
# 20 remove kare
# List ko reverse kare
# List ka largest element find kare
# List ka smallest element find kare

# numbers = [10, 20, 30, 40, 50]
# print(numbers.append(60))
# print(numbers)
# print(numbers.remove(20))
# print(numbers)
# print(numbers.reverse())
# print(numbers)
# print(min(numbers))
# print(max(numbers))



# Q10 — List + Loop
# User se 5 numbers input lekar ek list mein store karo.

# Phir print karo:

# Complete list
# Even numbers
# Odd numbers
# Sum of all numbers


# a=int(input("enter number1: "))
# b=int(input("enter number2: "))
# c=int(input("enter number3: "))
# d=int(input("enter number4: "))
# e=int(input("enter number5: "))

# list=[a,b,c,d,e]
# print(list)
# if a%2==0 :
#     print("even",a)
# else:
#     print("odd")
    
# if b%2==0 :
#     print("even",b)
# else:
#     print("odd")


# if c%2==0 :
#     print("even",c)
# else:
#     print("odd")


# if d%2==0 :
#     print("even",d)
# else:
#     print("odd")


# if e%2==0 :
#     print("even",e)
# else:
#     print("odd")


# sum=a+b+c+d+e
# print("sum of all numbers", sum)    



#     Q11 — Tuple

# Given:

# data = (10, 20, 30, 20, 40, 20, 50)

# Find karo:

# 20 kitni baar present hai
# 30 ka index kya hai
# Tuple ki length

# data = (10, 20, 30, 20, 40, 20, 50)
# print(data.count(20))
# print(data.index(30))
# print(len(data))


# Q12 — Dictionary

# Given:

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "BCA",
#     "marks": 85
# }

# Program likho jo:

# Student ka name print kare
# Marks update karke 90 kare
# "city": "Delhi" add kare
# Age remove kare
# Final dictionary print kare

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "BCA",
#     "marks": 85
# }
# print(student["name"])
# # print(student.update["marks":"90"])
# print(student.update({"city":"delhi"}))
# student.update({"marks":90})
# student.pop("age")
# print(student)


# Q13 — Dictionary + Condition

# Ek dictionary mein students ke marks store karo:

# students = {
#     "Rahul": 85,
#     "Aman": 42,
#     "Priya": 91,
#     "Rohit": 35,
#     "Neha": 76
# }

# Program likho jo har student ke liye print kare:

# Rahul - Pass
# Aman - Pass
# Priya - Pass
# Rohit - Fail
# Neha - Pass

# Passing marks = 40

# rahul_marks=int(input("enter rahul's marks"))
# aman_marks=int(input("enter aman marks"))
# rohit_marks=int(input("enter rohit marks"))
# priya_marks=int(input("enter priya marks"))
# neha_marks=int(input("enter neha marks"))
# students = {
#     "Rahul": 85,
#     "Aman": 42,
#     "Priya": 91,
#     "Rohit": 35,
#     "Neha": 76
# }
# if rahul_marks>40:
#     print(" Rahul is pass")
# else:
#     print("fail")
    
# if aman_marks>40:
#     print(" aman is pass")
# else:
#     print("fail")
    
# if rohit_marks>40:
#     print(" rohit is pass")
# else:
#     print("fail")
    
# if priya_marks>40:
#     print(" priya is pass")
# else:
#     print("fail")
    
# if neha_marks>40:
#     print(" neha is pass")
# else:
#     print("fail")

# Q14 — Sets

# Given:

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# Program se find karo:

# Union
# Intersection
# Difference A - B
# Difference B - A
# Symmetric Difference


# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# print("union is",A|B)
# print("intersection is",A&B)
# print("difference  is",A-B)
# print("difference is",B-A)
# print("Symmetric Difference is",A^B)


