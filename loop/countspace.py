# Given a sentence, count how many spaces are present.

text = input("Enter a sentence: ")

count = 0

for ch in text:
    if ch.isspace():
        count = count + 1

print("Spaces:", count)