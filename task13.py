sentence = "Functional programming in Python is very powerful and elegant"
words = sentence.split()
words_lengths = map(lambda word: len(word), words)
longest_3_words = sorted(words, key=lambda word: len(word), reverse=True)[:3]
print("Eng uzun 3 so'z:", longest_3_words)