# creating a function for validating number
def numValidation(num):
    # creating condition to validate number whether it lies within range or not
    while num > 255 or num < 0:
        print("Invalid Input!!! Please enter a number from 0 to 255")
        num = int(input(" Re-Enter a Number from 0 to 255 : "))
    return num
