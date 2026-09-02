# a = {
# "key": "value",
# "harry": "code",
# "marks": "100",
# "list": [1, 2, 9]
# }
# print(a["key"]) # Output: "value"
# print(a["list"]) # Output: [1, 2, 9]

# trans={
#     "sher":"lion",
#     "bakri":"goat",
#     "cheeta": "tiger"

# }
# translate=input("write word what you want to know meaning")
# print(trans[translate])


# student={
#     "name":"shivam",
#     "age":17,
#     "dob":2008,
#     "college":"galgotias"
# }
# student["surname"]="pal"
# student["cgpa"]=9.13
# print(student)


# student_info={
#     "name":"shivam",
#     "Surname":"pal",
#     "age":17,
#     "DOB":2008,
#     "CGPA":9.13,
#     "Marks":{
#         "c":78,
#         "C++":89,
#         "OOPS":{
#             "OOPS With C++":97,
#             "OOPS With python":78,
#             "OOPS with JAVA":89
#         }

#     }
# }
# print(student_info)
# print(student_info["name"])
# print(student_info["Marks"]["OOPS"]["OOPS With C++"])
# print(student_info.keys())
# print(student_info.values())
# print(student_info.items())
# print(student_info.get("name"))
# print(student_info.update({"city":"delhi"}))

# print(student_info)


# dictionary={
#     "table":["a piece of furniture"," a list of fact & figures"],
#     "cat":" a small  animal"
# }
# print(dictionary)




# dictionary = {
#     "python": input("enter the marks of python"),
#     "c":input("enter the marks of C "),
#     "java":input("enter the marks of java")

# }
# print(dictionary)

marks={}
x=int(input("enter your marks of python"))
marks.update({"python":x})

x=int(input("enter your marks of java"))
marks.update({"java":x})

x=int(input("enter your marks of C"))
marks.update({"C":x})
print(marks)