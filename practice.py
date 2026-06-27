import time
myTime = int(input("Whats your timer count in seconds? :  "))

print("Starting the timer!")

time.sleep(2)

for x in range(myTime, 0 , -1): 
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
    
