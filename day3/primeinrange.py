import math

n = int(input("Enter the number greater than zero"))
primes = [True for j in range(0, n+1)]
# print(primes)
n1_sqrt = int(math.sqrt(n))
# print(n1_sqrt)
for i in range(2, n1_sqrt):
  if primes[i] == True:
    for j in range(i * 2, n + 1, i):
      primes[j] = False
primes[0] = False
primes[1] = False
for j in range(0, len(primes)):
  if primes[j] == True:
    print(j, end=",")
  else:
    continue
