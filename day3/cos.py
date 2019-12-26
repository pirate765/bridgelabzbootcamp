import math

x = float(input("Enter the angle in radians"))
x = x % (2 * math.pi)
a = -1
cosx = 1
for i in range(1,15):
  cosx += ((a)*(pow(x,2*i))/math.factorial(2*i))
  a *= -1
print("The value of cos is {}".format(round(cosx, 3)))