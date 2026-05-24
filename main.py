import helper as help
import math as m
import re

#Subnet Calculator
#Made by Antonio Magnani 5/17/26

print("Do you want in depth calculations with ip addresses?")
print("Saying no will only perform calculations with subnet mask only.")

userInput = input("\nWhat is your answer? (y/n): ")
inDepth = False
#^(yes|no|[yn])$ with the re.search you can actually have a re.IGNORECASE

#print("1) Subnet Mask only calculation,")
#print("2) In depth calculation with ip address.")
#userAnswer = input("What is your answer? (only 1 or 2): ")
#^[12]$

while (True):
    
    if (not re.search(r"^(yes|no|[yn])$", userInput)):
        print("Must be either 0 or 1")
        userInput = input("What is your answer? (0/1): ")
    else:
        if (int(userInput) == 1):
            inDepth = True
        break


subnetMask = input("What is your subnet mask? (Ex: /32 or 32): ")



while (True):
    if (not re.search(r"^[\/]?(3[0-2]|[12]?\d)$", subnetMask)):
        print("Must be in the format /##, ##, or must be in range of 0-32")
        subnetMask = input("What is your subnet mask? (Ex: /32 or 32): ")
    else:
        cleanSubnetMask = int(re.sub(r"\/", "", subnetMask)) #Or int(subnetmask.lstrip(\/))
        break


fullBytes = m.floor(cleanSubnetMask / 8)
networkBits = cleanSubnetMask % 8
hostBits = 8 - networkBits #(Is this needed?)

maskString = help.calculateMask(fullBytes, networkBits)


if (inDepth):


    ipAddr = input("What is your ip address?: ")


    octet = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)"
    ipPat = rf"^{octet}\.{octet}\.{octet}\.{octet}$"

    while (True):
        if(not re.search(ipPat, ipAddr)):
        
        
            print("Ip must be in the format ###.###.###.###, do not have leading 0s")
            ipAddr = input("What is your ip address?: ")
        else:

            #this is where we further validate as in checking if the supposed subnet mask makes sense for the ip
            break


    
    networkAddr = help.calculateNetworkAddr(ipAddr, maskString)
    usableHosts = help.calculateHosts(ipAddr, cleanSubnetMask)

    print(f"Network Mask for {subnetMask} is <{maskString}>.")
    print(f"The network address of {ipAddr} is {networkAddr}.")
    print(f"The amount of usable hosts are {usableHosts}.")
else:
    print(f"Network Mask for {subnetMask} is <{maskString}>.")









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