# creating a function to add binary with help of provided logic circuits
def addition(a, b):
    binaryList = []  # initializing list to store sum value
    carryIn = 0  # setting initial value of carry in as zero
    sumlist1 = []  # initializing a list to store reversed output sum value
    actualSum = ""  # initializing a string to store value changed in string format

    for i in range(7, -1, -1):  # using for loop to reverse list
        XOR1 = a[i] ^ b[i]  # setting XOR gate
        outputSum = XOR1 ^ carryIn  # As from coursework Question
        binaryList.append(outputSum)  # appending outputsum value in initialized list
        AND1 = a[i] & b[i]
        AND2 = XOR1 & carryIn
        carryOut = AND1 | AND2
        carryIn = carryOut  # Carry in for one adder is carry out for next adder
    for i in range(len(binaryList) - 1, -1, -1):
        sumlist1.append(binaryList[i])  # appending  value in initialized list
        actualSum = actualSum + str(binaryList[i])
    return actualSum
