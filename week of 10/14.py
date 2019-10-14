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

print(archimedes(4))
print(archimedes(8))
print(archimedes(360000000))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# See the loop above. In addition to the value of pi, print the difference
# between the values calculated by the archimedes function and by math.pi.
# How many sides does it take to make the two close?
# It takes 40, 400, 40 to make the Archimedes close.

print(math.pi)
