import random

n = int(input("Enter the number of times you want to roll the dice"))
outcomes = [0] * 7
for i in range(n):
  temp  = random.randint(1,6)
  outcomes[temp] += 1
  print(temp)
print("The max occuring number = {} and occurs {} times in {} trials.".format(outcomes.index(max(outcomes)), max(outcomes), n))