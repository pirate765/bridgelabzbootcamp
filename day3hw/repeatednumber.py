def repeat_check(a):
  n = [0] * 101
  for i in a:
    if n[i] == 0:
      n[i] += 1
    elif n[i] == 1:
      print(i, " is repeated twice.")
      return
    else:
      print("No number is repeated.")
      return

lst = []
for i in range(0, 100): 
    ele = int(input("Enter number ")) 
    lst.append(ele)
repeat(lst)

  
