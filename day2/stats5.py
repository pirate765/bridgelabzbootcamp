import random

numlist = []

for i in range(5):
  numlist.append(round(random.random(), 2))
print("The list of random numbers is {}".format(numlist))
sum = 0
for i in numlist:
  sum += i
avg = sum/5

print("the average of random : {}".format(round(avg, 2)))
print("Minimum : {}".format(min(numlist)))
print("Maximum : {}".format(max(numlist)))