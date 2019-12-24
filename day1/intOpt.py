int2 = input("Enter the three numbers separated by space, 'eg: 4 54 63 :'' ")
int1 = list(int2.split())
print(int2)
a = int(int1[0])
b = int(int1[1])
c = int(int1[2])

# a + b * c
res1 = a + (b * c)

# a * b + c
res2 = (a * b) + c

# c + a/b
if b == 0 :
    print("Invalid oeration 'c + a/b' and cannot divide by zero")
else:
    res3 = c + (a/b)

#a % b + c
res4 = (a % b) + c

print("The output for 1) a + b*c = ", res1)
print("The output for 2) a * b + c = ", res2)
print("The output for 3) c + a/b = ", res3)
print("The output for 4) a % b + c = ", res4)
