#11/3/26
import time
#FIRST IMPORT TIME

#Ask time input from user
time_input = int(input("Enter the Time in Seconds: "))

#Start a For loop:

for x in range(time_input,0,-1):
    hours = x//3600
    minutes = (x//60)%60
    seconds = x % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")