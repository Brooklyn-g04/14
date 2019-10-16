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
for val in range(1, N,):
    acc = val + acc
print(acc)
# the greater sign has no effect to th equation or answer, so if you have a rule that says that the variable is greater than 3 than you can use any positive integer greater than 3.
# this equals 3