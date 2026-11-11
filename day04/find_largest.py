from utils.number_utils import max_of_three
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  
num3 = int(input("Enter third number: "))
largest = max_of_three(num1, num2, num3)    
print("The largest number is:", largest)