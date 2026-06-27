import time
myTime = int(input("Whats your timer count in seconds? :  "))

for x in range(myTime, 0 , -1): 
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    
    print("Starting the timer!")
    time.sleep(2)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
    
