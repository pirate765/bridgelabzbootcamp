import sys

temp = input("Enter the temperature followed by space unit ( Eg: 45 C or 34.55 F)").split()
temp_val = float(temp[0])
temp_unit = str(temp[1])

if temp_unit == 'c' or temp_unit == 'C':
  to_far = ((9*temp_val)/5) + 32
  sys.exit("the temperature from {} C to farheniet =  {} farheniet".format(temp_val, to_far))

elif temp_unit == 'f' or temp_unit == 'F':
  to_far = (temp_val - 32) * (5/9)
  sys.exit("the temperature from {} F to Celcius =  {} Celcius".format(temp_val, to_far))

else:
  sys.exit("Check the units to be C or F only")