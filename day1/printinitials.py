import math

y = 'kdw'
i = 0
# arrk[]
# while i < n/2:


# ------------- Sub program for printing K in asteriks----------------
wk, hk = 13, 9
arrk = [[' ' for x in range(wk)] for y in range(hk)]
k = wk - 1
while i <=  math.floor(hk/2):
    # while i < math.floor(hk/2) :
    arrk[i][0]= '*'
    arrk[i][1] =  '*'

    for j in range(k, k-3, -1):
        # print(i, j)
        arrk[i][j] = '*'
    k = j
    i += 1

k += 2
while i < hk:
    arrk[i][0] = '*'
    arrk[i][1] = '*'
    for j in range(k, k+3):
        arrk[i][j] = '*'
    k = j
    i +=1

# for i in range(0, hk):
#     for j in range(0, wk):
#         print(arrk[i][j], end="")
#     print(end="\n")

# ------------- Sub program for printing D in asteriks----------------
wd, hd = 14, 9
arrd = [[' ' for x in range(wd)] for y in range(hd)]
for j in range(10):
    arrd[0][j] = '*'
k = j + 1
for i in range(1, 4):
    arrd[i][0] = '*'
    arrd[i][1] = '*'
    for j in range(k, k+2):
        arrd[i][j] = '*'
    k = j
for i in range(4,6):
    arrd[i][0] = '*'
    arrd[i][1] = '*'
    arrd[i][k-1] = '*'
    arrd[i][k] = '*'

k = k -1
for i in range(6,8):
    arrd[i][0] = '*'
    arrd[i][1] = '*'
    for j in range(k, k-2, -1):
        arrd[i][j] = '*'
    k = j

for j in range(0, 10):
    arrd[8][j] = '*'

# for i in range(0, hd):
#     for j in range(0, wd):
#         print(arrd[i][j], end="")
#     print(end="\n")

for i in range(0, hk):
    arrk[i].append('    ')
    arrk[i].extend(arrd[i])

for i in range(0, hk):
    for j in range(0, len(arrk[i])):
        print(arrk[i][j], end="")
    print(end="\n")

# ------------- Sub program for printing W in asteriks----------------
