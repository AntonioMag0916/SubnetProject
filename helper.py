import math as m
import ipaddress as ipMan


#Left to right calculation
bitValues = [128, 64, 32, 16, 8, 4, 2, 1]

finalIp = [0, 0, 0, 0]



def calculateByte(bits):
    sum = 0
    for i in range(0, bits):
        sum += bitValues[i]
    return sum

"""
-Network Addr
-Range of hosts
-Broadcast
"""

def calculateNetworkAddr(ip, subnet):
    
    newIp = ipMan.ip_address(ip)
    newMask = ipMan.ip_address(subnet)

    networkAddr = ipMan.ip_address(int(newIp) & int(newMask))

    return networkAddr

def calculateHosts(ip, subnetMask):

    hostBits = 32 - int(subnetMask)
    usableHosts = 2 ** hostBits - 2

    if (usableHosts <= 0):
        print("No useable hosts!")
        return 0
    else:
        return usableHosts
    



def calculateMask(fullBytes, networkBits):
    finalMask = [0, 0, 0, 0]
    
    if (fullBytes != 0):
        for i in range(0, fullBytes):
            finalMask[i] = 255

        if (fullBytes < 4):
            finalMask[i + 1] = calculateByte(networkBits)
    else:
        finalMask[0] = calculateByte(networkBits)
    
    return ".".join(map(str, finalMask))


