import math

coord = input("Enter x and y :").split()
x, y = int(coord[0]), int(coord[1])
euc_dist = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
print(euc_dist)
