import random

list_flip = []
tries = 0
while True:
  iter = input("Press n to continue or e to exit")
  if iter == 'n' or iter == 'N':
    temp = random.randint(1, 100)
    if temp%2 == 0:
      list_flip.append(0)
      tries += 1
      print("Heads")
    else:
      list_flip.append(1)
      tries += 1
      print("Tails")
    continue
  elif iter == 'e' or iter == 'E':
    head_count = list_flip.count(0)
    tails_count = list_flip.count(1)
    head_per = (head_count * 100)/(head_count + tails_count)
    tail_per = (tails_count * 100)/(head_count + tails_count)
    print(list_flip)
    print("The percentage of heads is {} percent and tails is {} percent".format((round(head_per, 2)), (round(tail_per, 2))))
    break
    
  else:
    print("Please enter a valid input")
    continue
