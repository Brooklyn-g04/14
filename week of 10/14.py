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

# sum of the first 50 odd numbers
acc = 0
for val in range(1, 101, 2):
    acc = acc + val
print(acc)

# average of the first 100 odd numbers

acc = 0
for val in range(1, 201, 2):
    acc = acc + val / 100
print(acc)

# write a function that returns the average to the first N numbers, where N is a parameter
N = 0
acc = 0
for val in range(N, 101, 2):
    acc = acc + val
print(acc)

