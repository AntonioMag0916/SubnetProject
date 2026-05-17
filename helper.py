import math as m

#Left to right calculation
bitValues = [128, 64, 32, 16, 8, 4, 2, 1]

finalIp = [0, 0, 0, 0]
finalMask = [0, 0, 0, 0]



def calculateByte(bits):
    sum = 0
    for i in range(0, bits):
        sum += bitValues[i]
    return sum


def calculateMask(fullBytes, networkBits):
    resetMask()
    
    if (fullBytes != 0):
        for i in range(0, fullBytes):
            finalMask[i] = 255

        if (fullBytes < 4):
            finalMask[i + 1] = calculateByte(networkBits)
    else:
        finalMask[0] = calculateByte(networkBits)
    
    return ".".join(map(str, finalMask))


def resetMask():
    for i in range(0, 4):
        finalMask[i] = 0
