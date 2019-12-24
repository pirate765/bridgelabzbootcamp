date = input("Enter the month and day with a space").split()
month,day = int(date[0]), int(date[1])
while True:

    if month < 3 or month > 6:
        print("False")
        break

    elif month >= 3 and month <=6:
        if month == 3:
            if day >= 20:
                print("True")
                break
            else:
                print("False")
                break

        elif month == 6:
            if day <= 20:
                print("True")
                break
            else:
                print("False")
                break

        else:
            print("True")
            break
