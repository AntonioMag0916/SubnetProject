import helper as help
import math as m

#Subnet Calculator
#Made by Antonio Magnani 5/17/26

#Variable intialization



subnetMask = int(input("What is your subnet mask?: "))

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