n = int(input("Enter the decimal form number"))
temp = n
binary = []
while temp > 0:
  rem = temp % 2
  temp = int(temp/2)
  binary.append(rem)
  # print(rem)
binary.reverse()
bin_rep = ''
for j in binary:
  bin_rep += str(j)

while (len(bin_rep)%4) != 0:
  bin_rep = "0" + bin_rep
  

print("the binary representation of {} is {}".format(n, bin_rep))

