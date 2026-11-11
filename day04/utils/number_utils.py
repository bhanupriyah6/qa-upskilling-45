def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False
def max_of_three(a, b, c):
    if a>= b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
def reverseString(text):
    return text[::-1]
