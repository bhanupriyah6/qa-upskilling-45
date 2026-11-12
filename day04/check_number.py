from utils.number_utils import isEven
num = int(input("Enter a number: "))
if isEven(num):
    print("Even number")
else:
    print("Odd number")