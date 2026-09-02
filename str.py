# str = "i am shiv"
# print(len(str))
# print(str.capitalize())
# str1 = print(str.replace("a", "o"))
# str2 = print(str.find("a"))
# str3 = print(str.count("a"))

# a=input("enter your name : ")
# print(a)
# print(len(a))

# str ="i am shiv"
# print(str.upper())

# str ="i am shiv"
# print(str.lower())

# str ="i am shiv"
# print(str.title())

# str ="  i am shiv  "
# print(str.strip())

# str ="  i am shiv  "
# print(str.lstrip())

# str ="  i am shiv  "
# print(str.rstrip())

# str ="i am shiv"
# print(str.index("s"))

# str ="shiv"
# print(str.isalpha())

# str ="shiv"
# print(str.isdigit()) //not understand
# s1 = float(input("Enter the marks math :"))
# s2 = float(input("Enter the science marks :"))
# s3 = float(input("Enter the hindi marks :"))
# s4 = float(input("Enter the English marks :"))
# s5 = float(input("Enter the SST marks :"))
# sum = s1+s2+s3+s4+s5

# marks = float(sum/5)
# if(marks > 100):
#     print("invalid numbers please check the number")
# elif(marks >= 90):
#     print("grade is A")
# elif(marks<=90 and marks>=80):
#     print("grade is B")
# elif(marks<=80 and marks>=70):
#     print("grade is C")
# elif(marks<=70 and marks>=50 ):
#     print("grade is D")
# elif(marks<=50 and marks>=33):
#     print("grade is E")
# elif(marks<33):
#     print("grade is F so its fail")
# else:
#     print("enter valid marks")



# marks=[15,45,75,85,78,95,100]
# print(marks)
# print(type(marks))
# print(len(marks))


# student=["shiv",12 , "delhi" , "bca"]
# print(student[0])
# student[0]="kaushik"

# print(student[0])

# list=["shiv", "kau" , "far"]
# # print(list)
# # print(list.append("aman"))
# # print(list)
# # print(list.sort(reverse=True))
# # print(list)
# # print(list.reverse())
# # print(list)
# print(list.insert(0,"aman"))
# print(list)
# print(list.remove("aman"))
# print(list)
# print(list.pop(2))
# print(list)
# print(list.copy())
# print(list.extend("shiv"))
# print(list)
# print(list.clear())
# print(list)
# list=[[1,2],[3,4]]
# print(list[1])

# tup=(1,2,3,4,5,)
# # print(type(tup))
# # print(len(tup))
# print(tup.index(4))
# print(tup.count(4))

# movie1=input("enter  first movie")
# movie2=input("enter  second movie")
# movie3=input("enter  third movie")
# list=[movie1 , movie2,movie3]
# print(list)

# a=[1,2,3,2,1]
# copy_a=a.copy()
# copy_a.reverse()
# if(copy_a==a):
#     print("palindrome")
# else:
#     print("not")

# tup=("c","d","a","a","b","b","a")
# print(tup.count("a"))


# list=["c","d","a","a","b","b","a"]
# print(list.sort())
# print(list)

# str=int("10")

# result= str+5
# print(result)
# print(type(str))

# num = int("10")   # convert string to integer
# result = num + 5  # add 5

# print(result)
# print(type(num))

# Convert float to int and print result
# float=int(5.4)
# print(float)

# Take input and check its boolean value
# a=input("enter number")
# result=bool(a)
# print(result)


# str="shivam"
# print(str.reverse())
# text = input("Enter a string: ")

# reverse = text[::-1]

# print("Reversed string:", reverse)

# text = input("Enter a string: ")
# print(text.replace("text","java"))
# print(text)



# name = input("Enter your name: ")
# date = input("Enter the date: ")

# # Replace placeholders with actual values
# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", date)

# print("\nFinal Letter:\n")
# print(letter)

# Write a program to detect double space in a string
# string = input("Enter a string: ")

# # Check for double spaces
# if "  " in string:
#     print("Double space found")
# else:
#     print("No double space found")

# Write a program to format the following letter using escape sequence
# characters.
# letter = "Dear shivam, this python course is nice. Thanks!"
# print("Dear shivam,\nthis python course is nice.\nThanks!")

#  Write a program to store seven fruits in a list entered by the user
# fruit1=input("enter 1 fruit name")
# fruit2=input("enter 2 fruit name")
# fruit3=input("enter 3 fruit name")
# fruit4=input("enter 4 fruit name")
# fruit5=input("enter 5 fruit name")
# fruit6=input("enter 6 fruit name")
# fruit7=input("enter 7 fruit name")

# print(list[fruit1,fruit2,fruit3,fruit4,fruit5,fruit6,fruit7])

# Write a program to accept marks of 6 students and display them in a sorted
# manner.
# student = [
#     int(input("enter the marks of 1 student")),
#      int(input("enter the marks of 2 student")),
#       int(input("enter the marks of 3 student")),
#        int(input("enter the marks of 4 student")),
#         int(input("enter the marks of 5 student")),
#          int(input("enter the marks of 6 student")),
#           int(input("enter the marks of 7 student"))
# ]
# print("the marks of 7 student",student.sort())
# print(student)
#  Check that a tuple type cannot be changed in python.

# numbers = (1, 2, 3, 4)

# numbers[0] = 10

# print(numbers)

# 4. Write a program to sum a list with 4 numbers. 
# list=[1,2,3,4,5,6]
# total=sum(list)
# print(total)
# 5. Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))