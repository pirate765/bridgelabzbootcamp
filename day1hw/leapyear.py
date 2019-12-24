def check_leap_year(year):
    if year < 1582:
        print("Please enter a year after 1582")
        year = int(input("Enter a year again"))
        return check_leap_year(year)
    else:
        if year%4 == 0:
            if year%100 == 0:
                if year%400 == 0:
                    print("The year is a leap year")
                    return
                else:
                    print("The year is not a leap year")
                    return
            else:
                print("The year is a leap year.")
                return
        else:
            print("The year is not a leap year")
            return


year = int(input("Enter a year to check leap year or not"))
leap_bool = check_leap_year(year)
