import math
principle = 0
rate = 0
time = 0

input("Enter your principal amount:  $")
input("Enter your rate percentage:  $")
input("Enter your time :  $")

while principle <= 0:
      principle = float(input("Enter your principal amount:  $"))
      if principle <= 0:
        print("invalid principle ")
while rate <= 0:
      rate = float(input("Enter your rate percentage:  $"))
      if rate <= 0:
        print("invalid rate ")
while time <= 0:
      time = int(input("Enter your time amount:  $"))
      if time <= 0:
        print("invalid time ")
      
total = principle * pow((1 + rate / 100), time)
      
print(f"Balance after {time} years with original principle ${principle} and rate {rate} is {total:.2f}%")


     