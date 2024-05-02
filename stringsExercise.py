
# ex_10= "Just do it!"
# print(ex_10[10])
# print(ex_10[5:7])
# print(ex_10[8:])
# print(ex_10[0:4])
# print("Don't" + ex_10[5:])



# number = int(input("enter an integer:\n"))
# output = number + 10
# print(output)
# def function_name():
#     print(2+2)

# function_name()
# # function with parameter
# def default(num, pnum):
#     print(num*pnum)

# default(4,6)

# def  hello_world_printer():
#     print("Hello worlds")

# hello_world_printer()


# def name_printer(a):
#     print(a)

# a = input("enter name: ")
# name_printer(a)

# l = int(input("Length: "))
# w = int(input("width: "))
# h = int(input("height:"))
# def volume(l, w, h):
#      sum = l*w*h
#      print(sum)


# volume(l,w,h)

# c = int(input("enter c: "))

# def fahrenheit (c):
#     f = 1.8*c + 32
#     print(f)

# fahrenheit(c)
from random import *
fuel = (randint(10, 20))
miles = (randint(200, 400))
MPG = miles // fuel
print("The car can travel miles per gallon " + str(MPG))
print("The car fuel tank can hold " + str(fuel))
print("The car can travel " + str(miles))
