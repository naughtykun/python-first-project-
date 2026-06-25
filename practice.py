import math
principle = 0
rate = 0
time = 0

while principle <= 0:
      principle = float(input("Enter your principal amount:  $"))
      print("invalid principle ")
while rate <= 0:
      rate = float(input("Enter your principal amount:  $"))
      print("invalid rate ")
while time <= 0:
      time = int(input("Enter your principal amount:  $"))
      print("invalid time ")
      
total = principle * pow((1 + rate / 100), time)
      
print(f"Balance after {time} years with original principle ${principle} and rate {rate} is {total}%")


     