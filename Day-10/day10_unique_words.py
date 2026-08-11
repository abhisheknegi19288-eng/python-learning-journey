sentence = input("Enter sentence: ")
words = sentence.lower().split()
unique_words = set(words)
print("Number of unique words: ", len(unique_words))
