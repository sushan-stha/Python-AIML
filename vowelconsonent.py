# program to check if the word is vowel or consonent.

word = input("Enter the word:").lower().strip()

if (word.startswith('a') or word.startswith('e') or word.startswith('i') or word.startswith('o') or word.startswith('u')):
    print(f"{word} is a vowel word")
else:
    print(f"{word} is a consonent word")
