import math
import time
# print("Hello!!")
# name = input("Please Enter Your Name: ")
# print(f"HI {name}")
# age = int(input("Please Enter Your Age: "))
# print(f"Your Age is: {age} ")
# if age>=18:
#     print("You are eligible to vote")
# else:
#     print("LMAO kid")
#---------------------------------------------


# radius = float(input("Enter The Radius of the Circle: "))

# Cir = 2 * math.pi * radius

# print(f"The Circumference of the Circle is {round(Cir,20)}cm")

#-------------------------------------------------------------------

#WEIGHT CONVERSION::

# weight = float(input("Enter Your Weight: "))
# unit = input("Convert to Lb or Kg : ").lower()

# if unit =="lb":
#     weight *=2.205
#     unit ="Lb"
#     print(f"You Weight in Lb is {weight}{unit}")
# elif unit =="kg":
#     weight /=2.205
#     unit ="Kg"
#     print(f"You Weight in Kg is {weight}{unit}")
# else:
#     print("NO! Enter Lb or Kg")

# #---------------------------------------------------------
# x=81
# # ans = math.sqrt((x))
# ans = math.pow(3,3)
# print(ans)  
# -----------------------------------------------------------

#COMPUND INTEREST CALCULATOR

# principle =0
# rate =0
# time =0

# while principle<=0:
#     principle = int(input("Enter the Principle Amount "))
#     if principle<=0:
#         print("Principle Amount cant be negative or zero")

# while rate<=0:
#     rate = int(input("Enter the rate % "))
#     if rate<=0:
#         print(" rate cant be negative or zero ")

# while time<=0:
#     time = int(input("Enter the time period "))
#     if time<=0:
#         print(" time period cant be negative or zero ")

# amount = principle * pow((1+rate/100),time)
# print(f"The Compund Interest is : {amount:.2f}")   
# 
# -------------------------------------------------------------

#FOR LOOPS!!


# for x in range(1,11):
#     print(x)

# for y in reversed(range(1,11)):
#     print(y)

#--------------------------------------------

#COUNTDOWN PROGRAM 
# first import time
# timeinput = int(input("Please enter the time in seconds "))
# for x in range(timeinput,0,-1):
#     seconds = x % 60
#     minutes = (x//60) % 60
    
#     print(f"00:{minutes:02}:{x:02}")
#     time.sleep(1)

# print("TIME'S UP")
#
#-----------------------------------------------
#TRYING ANOTHER TIME (11/3/26)


#FIRST IMPORT TIME

#Ask time input from user
time_input = int(input("Enter the Time in Seconds"))

#Start a For loop:

for x in range(time_input,0,-1):
    hours = x//3600
    minutes = (x//60)%60
    seconds = x % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")