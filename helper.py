#Left to right calculation
bitValues = [128, 64, 32, 16, 8, 4, 2, 1]


def calculateByte(bits):
    sum = 0
    for i in range(7, bits, -1):
        sum += bitValues[i]
        print(bitValues[i])
    return sum