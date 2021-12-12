#importing modules
import numberValidation
import binaryconversion
import bitAdder

print("---------------------------------------------------------------------")
print("Welcome To The Program")
print("---------------------------------------------------------------------")

flag = True
while flag:
    continuation = True
    while continuation:
        try:
            decimalNum1 = int(input("Enter first Number from 0 to 255: "))
            decimalNum1 = numberValidation.numValidation(decimalNum1) # calling the function to check the first number within range
            break
        except:
            print("Invalid Input!!!")
    continuation = True
    while continuation:
        try:
            decimalNum2 = int(input("Enter second Number from 0 to 255: "))
            decimalNum2 = numberValidation.numValidation(decimalNum2)  # calling the function to check the  second number within range
            break
        except:
            print("Invalid Input!!!")
    sumnum = decimalNum1 + decimalNum2
    if sumnum > 255:
        print("--------------------------------------------------")
        print("Error!Sum number exceeds 255 which cause overflow error")
        print("--------------------------------------------------")
    else:
        input1 = binaryconversion.binary_to_decimal(decimalNum1) #calling a function to convert first decimal number into binary and reversing the list and store in string format
        input2 = binaryconversion.binary_to_decimal(decimalNum2)#calling a function to convert second decimal number into binary and reversing the list and store in string format

        actualsum = bitAdder.addition(input1, input2) #calling a function to add binary input 1 and 2 and return the list in string format
        # priinting brinary sum of inputed decimals
        print("Binary Sum of", decimalNum1, "and ", decimalNum2, "is", actualsum)

        # asking the users to continue or end the program
        continuous = input("Do you wish to continue?? (yes/no)").lower()
        if continuous == "no": # break the loop on entering no
            print("---------------------------------------------------------------------")
            print("Thank you for using the program!")
            print("---------------------------------------------------------------------")
            flag = False
