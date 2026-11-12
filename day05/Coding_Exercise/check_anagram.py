def is_anagram(a, b):
    if len(a) != len(b):
        return False
    s = sorted(a)
    t = sorted(b)
    return s == t
word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()
if is_anagram(word1, word2):
    print("The words are Anagrams")
else:
    print("The words are Not Anagrams")