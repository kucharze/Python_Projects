bad_words = ['hate', 'dumb', 'stupid']

sentence = input("Enter a sentence: ").lower()

for word in bad_words:
    if word in sentence:
        print("Bad word detected: " + word)
        break