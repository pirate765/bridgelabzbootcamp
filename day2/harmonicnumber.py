n = int(input("Enter the integer for harmonic number"))
h = 0
if n <= 0:
  print("The number should be greater than zero")
else:
  for i in range(1, n + 1):
    h += (1/i)
print("The harmonic number for the {} = {}".format(n, round(h, 2)))
