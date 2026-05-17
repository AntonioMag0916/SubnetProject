#Left to right calculation
bitValues = [128, 64, 32, 16, 8, 4, 2, 1]


def calculateByte(bits):
    sum = 0
    for i in range(0, bits):
        sum += bitValues[i]
    return sum