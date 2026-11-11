def check_even_odd(number):
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd number"


num = int(input("Enter a number: "))
result = check_even_odd(num)

print(result)