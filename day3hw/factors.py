n = int(input("Enter the number to print factors"))
i = 1
factors = []
while i * i <= n:
  if n % i == 0:
    if (n/i) != i:
      factors.append(int(i))
      factors.append(int(n/i))
      i += 1
    
    else:
      factors.append(i)
      i += 1
  else:
    i += 1
    
print("The factors of number {} are {}".format(n, factors))