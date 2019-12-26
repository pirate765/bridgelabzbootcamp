import random

stake = int(input("Enter the stake amount : "))
goal = int(input("Enter the goal : "))
trials = int(input("Enter the number of trials"))
curr = 0
result = []
count = 0
print("Stake : {} | Goal : {} | Trials : {}".format(stake, goal, trials))
while count <= trials and stake < goal and stake > 0:
  n = input("press n for next hand")
  if n == 'n':
    trial = random.randint(1, 100)
    if trial % 2 == 0:
      #won if random integer is even
      result.append(1)
      stake += 1 
      count += 1
      print("Result : Won | Stake : {} | Trials : {}".format(stake, trials))
    else:
      #lost
      result.append(0)
      stake -= 1
      count += 1
      print("Result : Loss | Stake : {} | Trials : {}".format(stake, trials))
    if stake == goal:
      print("You have reached your goal.")
      break
    if stake == 0:
      print("You have no money left to play.")
      break
    if count == trials:
      print("Your number of trials have finished.")
      break
  else:
    print("Please press a valid key")
    continue

win_count = 0
for i in result:
  if i == 1:
    win_count += 1
print("The number of times won = {}".format(win_count))
print("The percentage of winning = {}".format(round((win_count*100)/len(result))))
print("The total number of bets made = {}".format(len(result)))




