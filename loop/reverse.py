# Reverse a given string without using a built-in reverse function.

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reverse:", reverse)