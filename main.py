MIN_BET = 10
MAX_BET = 300
MAX_LINES = 3
def deposit():
  while True:
    amount = input("Enter your deposit:   $")
    if amount.isdigit():
       amount = int(amount)
       if amount > 10:
        break
       else: print("deposit must be atleast 10$")
    else: print(f"invalid deposit {amount}")
  return amount

def numberOfLines():
  while True:
    lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")

    if lines.isdigit():
       lines = int(lines)
       if 1 <= lines <= MAX_LINES:
        break
       else:print(f"Please pick a line between (1-{MAX_LINES})")
    else: print(f"invalid number {lines}")
  return lines
  
def Bet():
  while True:
    amount = input("Enter your bet:   $")
    if amount.isdigit():
       amount = int(amount)
       if MIN_BET <= amount <= MAX_BET:
        break
       else: print("bet must be atleast 10$")
    else: print(f"invalid bet {amount}")
  return amount
  
def main():
   balance = deposit()
   NoOfLines = numberOfLines()
   bet = Bet()
   print(f"""Your deposit is: ${balance}
Line you betted on: {NoOfLines}
Your bet amount: ${bet}""")
  
main()
   
