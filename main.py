import math as m
import helper

#Subnet Calculator
#Made by Antonio Magnani 5/17/26

#Variable intialization

finalIp = [0, 0, 0, 0]
finalMask = [0, 0, 0, 0]

subnetMask = int(input("What is your subnet mask?: "))

fullBytes = m.floor(subnetMask / 8)
networkBits = subnetMask % 8
hostBits = 8 - networkBits



for i in range(0, 4):
    if ((i + 1) <= fullBytes):
        finalMask[i] = 255
    else:
        calculateByte(networkBits)







#User input for ip and subnet mask
#User input validation
#Maybe use some regex or something

#Calculation

#output

"""
32 % 8 = 0
32 / 8 = 4 !
30 / 8 = 3.1 

30 % 8 = 2 (two host bits) 

print(f"Full bytes: {fullBytes}")
print(f"Host bits: {hostBits}")
print(f"Network bits: {networkBits}")

"""