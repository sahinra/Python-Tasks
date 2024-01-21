# Accept a sentence from the user and count how many words it contains.

sentence = input("Write a sentence ")
words = sentence.split()
print(words)
print(f"length is {len(words)}")