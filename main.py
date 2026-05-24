import helper as help
import math as m
import re

#Subnet Calculator
#Made by Antonio Magnani 5/17/26



ipAddr = input("What is your ip address?: ")


octet = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)"
ipPat = rf"^{octet}\.{octet}\.{octet}\.{octet}$"

while (True):
    if(not re.search(ipPat, ipAddr)):
        print("Ip must be in the format ###.###.###.###, do not have leading 0s")
        ipAddr = input("What is your ip address?: ")
    else:
        break


subnetMask = input("What is your subnet mask? (Ex: /32 or 32): ")

while (True):
    if (not re.search(r"^[\/]?(3[0-2]|[12]?\d)$", subnetMask)):
        print("Must be in the format /##, ##, or must be in range of 0-32")
        subnetMask = input("What is your subnet mask? (Ex: /32 or 32): ")
    else:
        subnetMask = int(re.sub(r"\/", "", subnetMask)) #Or int(subnetmask.lstrip(\/))
        break




fullBytes = m.floor(subnetMask / 8)
networkBits = subnetMask % 8
hostBits = 8 - networkBits



maskString = help.calculateMask(fullBytes, networkBits)
print(maskString)

    
    


#print(maskString)





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

full bytes = 2 
1 2 STOP FIN
0 1 STOP FIN

full bytes = 3
1 2 3 STOP


"""