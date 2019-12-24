import sys 

t = input("Enter the temperate (Farheneit)")
v = input("Enter the wind speed (miles/hour)")
t1 = float(t)
v1 = float(v)
if abs(t1) > 50:
  sys.exit("The temp should be below 50")
elif v1 < 3 or v1 > 120:
  sys.exit("The wind should be between 3 and 120")
# print(t1 + v1)
w = 35.74 + 0.6215*t1 + ((0.4275 * t1 - 35.75)*(pow(v1, 0.16)))
print("The wind chill is ", round(w, 3))


