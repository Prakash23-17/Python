text = input("Enter a sentence: ")

words = text.split()

result = ""

for word in words:
    reverse = ""

    for ch in word:
        reverse = ch + reverse

    result = result + reverse + " "

print(result)