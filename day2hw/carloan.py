p = float(input("Enter the principal loan amount"))
y = float(input("Enter the time in years to repay"))
R = float(input("Enter the interest rate"))
n = 12 * y
r = R / (12 * 100)
payment = (p * r) / (1 - pow((1 + r), -n))

print("The monthly payment to be made = {}".format(round(payment, 3))
