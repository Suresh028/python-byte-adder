# creating a function for binary conversion
def binary_to_decimal(decimalNo):
    bit = []  # initializing a empty list to store binary digits
    reverse_binary = []  # initializing a list to store binary digit after reversing
    counter = 0  # setting counter as 0
    binary = ""  # initializing a string to store binary digit value changed in string format
    decimal = decimalNo
    while counter != 8:
        remainder = decimalNo % 2  # divide the inputed decimal number by 2
        decimalNo = decimalNo // 2  # divide by 2 to get quotient
        bit.append(remainder)
        counter = counter + 1
    for i in range(len(bit) - 1, -1, -1):  # for loop for reversing the list
        reverse_binary.append(bit[i])  # add the reversed value in list
        binary = binary + str(bit[i])  # converting the list in string format
    print("Binary conversation of", decimal, "is", binary)
    return reverse_binary
