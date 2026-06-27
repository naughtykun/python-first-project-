import time
myTime = int(input("Which project? :  "))

if myTime == 1: 
  realTime = int(input("Whats your timer count in seconds? :  "))
  print("Starting the timer!")

  time.sleep(2)

  for x in range(realTime, 0 , -1): 
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
else: 

 if myTime == 2:
  rows = int(input("How many rows?:  "))
  columns = int(input("How many columns?:  "))
  symbol = input("Pick a symbol/Emoji:  ")
  
  for x in range(rows):
     for y in range(columns):
         print(symbol, end = "")
     print()
  