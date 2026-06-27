import random
MIN_BET = 10
MAX_BET = 300
MAX_LINES = 3

ROWS = 3
COLS = 3

symbolCount = {
  "Z": 2,
  "A": 4,
  "B": 6,
  "C": 8
}

def SlotMachine(rows, cols, symbols):
  allSym = []
  for symbols , symbolCount in symbols.items():
    for _ in range(symbolCount):
        allSym.append(symbols)
        
  columns= [] 
  for _ in range(cols):
    column = []
    currentSym = allSym[:]
    for _ in range(rows):
       value = random.choice(currentSym)
       currentSym.remove(value)
       column.append(value)
    columns.append(column)
  return columns
  
def printMachine(columns):
   for rows in range(len(columns[0])):
     for i, column in enumerate(columns):
      if i != len(columns) - 1 :
        print(column[rows], "|")
      else: print(column[rows])




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

    while True:
        bet = Bet()
        totalBet = bet * NoOfLines

        if totalBet > balance:
            print(f"Broke 😭 Your balance is ${balance}")
        else:
            break

    print(f"""Your deposit is: ${balance}
Line(s) you betted on: {NoOfLines}
Your bet amount: ${bet}
Total bet: ${totalBet}""")

    slot = SlotMachine(ROWS, COLS,symbolCount)
    printMachine(slot)
main()
   
