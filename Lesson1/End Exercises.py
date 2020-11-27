# #Exercise 1
# print('''Twinkle, twinkle, little star,
#         How I wonder what you are!
#                Up above the world so high,
#                Like a diamond in the sky.
# Twinkle, twinkle, little star,
#         How I wonder what you are
# ''')
###################################################
# #Exercise 2
# color_list = ["Red","Green","White" ,"Black"]
# for i in range(2):
#     color_list.pop(1)
# print(color_list)
######################################################
# #Exercise 3
# num=int(input("enter a number:"))
# sum=0
# for i in range(3):
#     sum=(num**(i+1))+sum
# print("the new number is:" + str(sum))
########################################################
# # Exercise 4
# date1=input("Enter a date:").split('/')
# date2=input("Enter a date:").split('/')
# D=int(date1[0])-int(date2[0])
# M=int(date1[1])-int(date2[1])
# Y=int(date1[2])-int(date2[2])
# Days=(D+M*30+Y*365)
# if Days<0:
#     Days=Days*-1
# print("number of days between the dates is:" + str(Days))
###########################################################
# # Exercise 5
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# num3=int(input("enter a number:"))
# if num1==num2==num3:
#     print("the result is:" + str(3*(num1+num2+num3)))
# else:
#     print("the result is:" + str(num1+num2+num3))
#############################################################
# # Exercise 6
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# sum=num1+num2
# if 15<=sum<=20:
#     print("the result is:20")
# else:
#     print("the result is:" + str(sum))
##########################################################
# # Exercise 7
# details=[]
# details.append(input("enter your name:"))
# details.append(input("enter your age:"))
# details.append(input("enter your address:"))
# for i in details:
#     print(i)
# # Exercise 8
####################################################
# x=int(input("enter a number:"))
# y=int(input("enter a number:"))
# print((x+y)**2)
################################################
# Exercise 9
##############################################
# # Exercise 10
# byte=input("enter a byte:")
# integer=[]
# for i in byte:
#     integer.append(i)
# print(integer)
##############################################
# # Exercise 11
# num=int(input("enter a number:"))
# sum=0
# for i in range(num,0,-1):
#     sum=sum+(i**2)
# print("the sum is:" + str(sum))