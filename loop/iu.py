text = input("Enter a sentence: ")

words = text.split()

reverse_sentence = ""

for i in range(len(words) - 1, -1, -1):
    reverse_sentence = reverse_sentence + words[i] + " "

print(reverse_sentence)