words = ["sun", "mountain", "a", "apple"]
list.sort(words, key=lambda word: len(word))
print("So'zlar uzunligiga ko'ra tartiblangan:", words)