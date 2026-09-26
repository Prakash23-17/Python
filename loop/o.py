text = input("Enter a sentence: ")

words = text.split()

result = ""

for word in words:
    result = result + word[0].upper() + word[1:] + " "

print(result.strip())