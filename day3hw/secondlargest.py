n = int(input("Enter the size of array"))
lst = []
for i in range(0, n):
  temp = int(input("Enter the number"))
  lst.append(temp)

minimum = min(lst)
maximum = max(lst)
second_min = maximum
second_max = minimum
for i in lst:
  curr = i - minimum
  curr2 = maximum - i
  if curr < second_min - minimum and curr != 0:
    second_min = i
  if curr2 < maximum - second_max and curr2 != 0:
    second_max = i
print("The second minimum is {}".format(second_min))
print("The second maximum is {}".format(second_max))
