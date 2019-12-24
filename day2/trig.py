import math

degree = float(input("Enter the value of angle in degrees"))
# print(degree)
to_rad = math.radians(degree)
cos = math.cos(to_rad)
sin = math.sin(to_rad)

print("{} degress = {} radians".format(degree, to_rad))
print("The value of cos({}) radians = {}".format(degree, cos))
print("The value of sin({}) radians = {}".format(degree, sin))