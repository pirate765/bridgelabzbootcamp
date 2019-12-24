int2 = input("Enter the three doubles separated by space, 'eg: 4.5 54.00 63.0 :'' ")
int1 = list(int2.split())
print(int2)
a = float(int1[0])
b = float(int1[1])
c = float(int1[2])

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
