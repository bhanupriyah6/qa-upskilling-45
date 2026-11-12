def capitalize_words(text):
    return text.title()
message = input("Enter a sentence: ")
result = capitalize_words(message)
print("Capitalized sentence:", result)