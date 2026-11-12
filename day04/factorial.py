def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    answer = factorial(num)
    print("Factorial of", num, "is", answer)
