import math


def sq_num(num):
    print("The square root of entered number: ", math.sqrt(num))


num = int(input("Enter the number : "))
sq_num(num)


def area_triangle(base, height):
    a = 0.5 * base * height
    print("Area of Triangle:", a)

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
area_triangle(base,height)


def swap_nums(a,b):
    temp = a
    a = b
    b = temp

    print("Value of a after swapping: ", a)
    print("Value of b after swapping: ",b)

a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))

swap_nums(a,b)


import random

def generate_rand():
    print("Random number is: ", random.randint(0,9))

generate_rand()