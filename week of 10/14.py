# We are going to look at approximations of Pi
# as well as looking at the math Module

print(22/7)
print(355/113)

import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSides = math.sin(math.radians(halfAngleA))
    sides = oneHalfSides / 2
    polygonCircumference = numSides * sides
    pi = polygonCircumference / 2
    return pi






# See the loop above. In addition to the value of pi, print the difference
# between the values calculated by the archimedes function and by math.pi.
# How many sides does it take to make the two close?
# It takes 40, 400, 40 to make the Archimedes close.
# the difference is -3.98741751768128e-0

print(3.1415527794146163-3.1411592653589793)

for sides in range(40, 400, 40):
    print(sides, archimedes(sides))

for sides in range(40000000, 40000000, 40000000):
    print(sides, archimedes(sides))

print(math.pi)


# Accumulators
# Accumulators hold the value that was added and keeps stacking and the value keeps going starting from the x value (x,y) and does not include the value.

acc = 0
for val in range(1, 6):
    acc = acc + val

print(acc)


# This equals 15

# By adding a third number you are telling the computer to count by that certain number

# sum of the first 100 even numbers
acc = 0
for val in range(0, 201, 2):
    acc = acc + val
print(acc)
# this equals 10100

# sum of the first 50 odd numbers
acc = 0
for val in range(1, 101, 2):
    acc = acc + val
print(acc)
# this equals 2500

# average of the first 100 odd numbers

acc = 0
for val in range(1, 201, 2):
    acc = acc + val / 100
print(acc)
# this equals 100.0

# write a function that returns the average to the first N numbers, where N is a parameter
acc = 0
N = acc + 3
for val in range(N, 101, 2):
    acc = acc + val
print(acc)
# this equals 2499

# Write a function called factorial that computes the product of the first N numbers, where N is a parameter

factorial = N
for val in range (N, 101):
    factorial = val + factorial
print(factorial)
# this equals 5050

# Each number in the Fibonacci sequence is the sum of the previous two numbers.The first two numbers in the sequence are 1 and 1.Compute the 10th Fibonacci number.

acc = 0

for val in range(1, 11):
    acc = val + acc
print(acc)

# this equals 55

# Write a function to compute the Nth Fibonacci number, where N is a parameter.You may assume that N will be greater than or equal to 3.

N = 3
acc = 0
for val in range(1, N):
    acc = val + acc
print(acc)
# the greater sign has no effect to th equation or answer, so if you have a rule that says that the variable is greater than 3 than you can use any positive integer greater than 3.
# this equals 3

# A Monte Carlo simulation

# random numbers

import random

print(random.random())
# Boolean Expressions
# <, <=, >, >=, ==, !=
# == compare
# < less than
# > greater than
# >= greater than or equal to
# <= less than or equal to
# != If it is not equal it is true

# compound Boolean expression
# and, or, not

dogWeight = 25
print(dogWeight == 25) # True
print(dogWeight != 25) # False
print(dogWeight <= 25) # True
print(dogWeight >= 25) # True
print(dogWeight < 25) # False
print(dogWeight > 25) # False

catWeight = 12

print(dogWeight >= 25 and catWeight >= 10) # True
print( dogWeight >= 25 or catWeight <= 10) # True
print(dogWeight < 25 and catWeight <= 10) # False
print(not catWeight >= 10) # False
# the not statement turns the true statement false
# The conjunction or is more loose so if one is right and one is wrong then it will say that it is true, it takes both to be wrong to say that it is false
# The and conjunction needs both to be right to make it true but if one is wrong then it is false

#  Decision making skills
alice = 20
bob = 15
carol = 25
ans = 0
if alice > 20:
    ans = 300
    print(ans)

# False
else:
    ans = 200
    print(ans)
# else means otherwise so if the statement above is true then you will get 300 but if it is not true then otherwise you get 200


if alice > 20:
    if bob < 50:
        ans = 150
    else:
        ans = 300
else:
    if carol > 500:
        ans = 200
    else:
        ans = 75
print(ans)

# all statements above are false so otherwise the answer is 75

value = 75
if value > 10:
    print("bigger than 10")
else:
    if value > 20:
        print("bigger than 20")
    else:
        if value > 45:
            print("bigger than 45")
        else:
            print("not bigger than much")
# bigger than 10

value = 75
if value > 10:
    print(" bigger than 100")
elif value > 80:
    print("bigger than 80")
elif value > 45:
    print(" bigger than 45")
else:
    print("not bigger than much")

# elif is python's abbreviation for else if



