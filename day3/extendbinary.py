def swap_nibble(bin_rep):
  nibbles = [0,0]
  num = 0
  if len(bin_rep) == 8:
    nibbles[0] = bin_rep[4:8]
    nibbles[1] = bin_rep[0:4]
    nibbles2 = nibbles[0] + nibbles[1]
    print(nibbles2)
    list_nib = []
    for j in nibbles2:
      list_nib.append(int(j))
    list_nib.reverse()
    print(list_nib)
    for i in range(0, len(list_nib)):
      num += (list_nib[i]*(pow(2, i)))
    return num    
  else:
    return ("The number is not in 8 digit form")

def check_power_2(bin_rep):
  # print(bin_rep.split('1'))
  if len(bin_rep.split('1')) == 2:
    return True
  
def convert_to_binary(n):
  temp = n
  binary = []
  while temp > 0:
    rem = temp % 2
    temp = int(temp/2)
    binary.append(rem)
  binary.reverse()
  bin_rep = ''
  for j in binary:
    bin_rep += str(j)
  while (len(bin_rep)%4) != 0:
    bin_rep = "0" + bin_rep
  return bin_rep

n = int(input("Enter the decimal form number"))
bin_rep = convert_to_binary(n)
print("The binary representatino is {}".format(bin_rep))
nibbles = swap_nibble(bin_rep)
print("The nibbles after swapping give {}".format(nibbles))
power_2 = check_power_2(bin_rep)
if power_2 == True:
  print("The number {} is a power of 2".format(n))
else:
  print("The number {} is not a power of 2".format(n))


