import os
import time
project = int(input("Which project? (1 = timer; 2 = cols/rows gen.py 3 = shopkart)  :  "))

if project == 1: 
  realTime = int(input("Whats your timer count in seconds? :  "))
  time.sleep(1)
  os.system("clear")
  print("Starting the timer!")

  time.sleep(0.5)

  for x in range(realTime, 0 , -1): 
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
else: 

 if project == 2:
  rows = int(input("How many rows?:  "))
  time.sleep(0.5)
  os.system("clear")
  columns = int(input("How many columns?:  "))
  time.sleep(0.5)
  os.system("clear")
  symbol = input("Pick a symbol/Emoji:  ")
  time.sleep(0.5)
  os.system("clear")
  
  for x in range(rows):
     for y in range(columns):
         print(symbol, end = "")
     print()
 
 if project == 3:
     total = 0
     cart = []
     prices = []
     
     
     while True:
          os.system("clear")
          food = input("Add a food in your cart [q = QUIT] :   ")
          if food.lower() == "q":
             os.system("clear")
             break
          
          else: 
              price =  input("Enter the price[q = QUIT] :  $")
              
              if price.lower == "q":
                  os.system("clear")
                  print("----Your cart---")
                  for food in cart:
                      print(food)
                  
                  os.system("clear")
              elif price != int(price):
                  print("enter a valid price")
              else: 
                  price = int(price)
                  cart.append(food)
              print(f"{food} is added to the kart!")
              