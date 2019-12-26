import math

x = float(input("Enter the angle in radians"))
x = x % (2 * math.pi)
print(x)
a = 1
sinx = 0
for i in range(1,15,2):
  sinx += ((a)*(pow(x,i))/math.factorial(i))
  a *= -1
print("The value of sinx is {}".format(round(sinx, 3)))