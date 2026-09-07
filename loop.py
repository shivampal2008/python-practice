# i=1
# while i<=100:
#     print(i)
#     i+=1

# i=int(input("enter number"))
# while i>=1:
#     print(i)
#     i-=1

# i=1
# n=int(input("enter n"))
# while i<=10:
#     print(i*n)
#     i+=1


# num=[1,4,9,16,24,36,49,64,81,100]
# i=0
# while i<=len(num):
#     print(num[i])
#     i+=1

# num=[1,4,9,16,24,36,49,64,81,100]
# for val in num:
#     print(val)

# num=(1,4,9,16,24,36,49,64,81,100)
# x=64
# idx=0
# for val in num:
#     if val==x:
#         print(idx)
#         break
#     idx+=1


# i = [10,20,30,40]
# for sum in i:
#     print(sum)


# i = 1
# while i<=100:
#     print(i)
#     i=i+1

# i = 100
# while i>=1:
#     print(i)
#     i=i-1

# i = 1
# n=3
# while i<=10:
#     print(n*i)
#     i=i+1


# num=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(num):
#     print(num[i])
#     i=i+1


# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# i = 0
# x = 81

# while i < len(num):

#     if num[i] == x:
#         print("found at", i)

#     i += 1


    
# num=(1,4,9,16,25,36,49,64,81,100)
# i = 0
# x=81
# while i<len(num):
#     if num[i]==x:
#         print("found at",i)
#     i+=1


# num=[1,4,9,16,25,36,49,64,81,100]

# for val in num:
#     print(val)


# num=(1,4,9,16,25,36,49,64,81,100,49)
# x=49
# i=0
# for val in num:
#     if val == x:
#         print("x is found at index",i)
#     i=i+1




# for i in range(1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)


# n=int(input("enter n : "))

# for i in range(1,11):
#     print(i*n)

# n=int(input("enter  n: "))
# sum = 0
# i = 1
# while i<=n:
#     sum=sum+i
#     i=i+1

# print("sum : ", sum)
   

n=int(input("enter  n: "))

fact = 1
while n>0:
    fact=fact*n
    n-=1

print("factorial : ", fact)