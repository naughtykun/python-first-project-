def deposit():
  while True:
    amount = input("Enter your deposit")
    if amount.isdigit():
       amount = int(amount)
       if amount > 10:
        break
       else: print("deposit must be atleast 10$")
    else: print(f"invalid deposit {amount}")
  return amount

def main():
   balance = deposit()
   


       