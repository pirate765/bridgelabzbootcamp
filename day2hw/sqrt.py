c = float(input("Enter the number to compute square root"))
t = c 
while abs(t - (c/t)) > (pow(10, -15) * t):
  t = ((c/t) + t)/2
print(t)