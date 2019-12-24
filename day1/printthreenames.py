x = input ("Enter the names: ")
sep = x.split()

if len(sep) != 3:
    print("Please enter three names with spaces")
else:
    y = 'Hi'
    # y += " ".join(x[::-1])
    for i in range(len(sep)-1, -1, -1):
        # print(sep[i])
        temp = ' '
        temp += sep[i]
        y += temp

    print(y)
