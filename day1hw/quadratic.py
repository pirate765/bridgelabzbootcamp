import sys
import math

coeff = input("Enter a b c :").split()
a, b, c = int(coeff[0]), int(coeff[1]), int(coeff[2])
if a == 0:
    sys.exit("The quadratic coeffecient (a) cannot be zero")
delta = (pow(b, 2)) - (4 * a * c)
if delta < 0:
    sys.exit("The equation does not have real roots")
root1 = (-b + math.sqrt(delta))/(2 * a)
root2 = (-b - math.sqrt(delta))/(2 * a)
print(root1, root2)
