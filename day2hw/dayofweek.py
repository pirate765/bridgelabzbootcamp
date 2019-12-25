month = input("Enter the month")
d = int(input("Enter the day (Ex: 29)"))
y = int(input("Enter the year"))
if month == 'January' or month == 'january':
  m = 1
elif month == 'February' or month == 'february':
  m = 2
elif month == 'March' or month == 'march':
  m = 3
elif month == 'April' or month == 'april':
  m = 4
elif month == 'May' or month == 'may':
  m = 5
elif month == 'June' or month == 'june':
  m = 6
elif month == 'July' or month == 'july':
  m = 7
elif month == 'August' or month == 'august':
  m = 8
elif month == 'September' or month == 'september':
  m = 9
elif month == 'October' or month == 'october':
  m = 10
elif month == 'November' or month == 'november':
  m = 11
elif month == 'December' or month == 'december':
  m = 12
else:
  m = 0
  print("The month is not valid! Please check.")

y0 = y - (int((14 - m) /12))
x = y0 + int(y0/4) - int(y0/100) + int(y0/400)
m0 = m + (12 * (int((14 - m)/12))) - 2
d0 = (d + x + (int((31 * m0)/12))) % 7

print("The day of the week : ",d0)