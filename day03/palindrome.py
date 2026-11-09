word = input("Enter a word: ")

reverse_word = word[::-1]

if word.lower() == reverse_word.lower():
    print("Palindrome")

else:
    print("Not a palindrome")