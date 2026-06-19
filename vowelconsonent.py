word = input("Enter the word:")

if (word.startswith('a') or word.startswith('e') or word.startswith('i') or word.startswith('o') or word.startswith('u')):
    print(f"{word} is a vowel word")
else:
    print(F"{word} is a consonent word")



    # (word == "a" or word=='e' or word=='i' or word=='o' or word=='u'):