text = input("Enter a string: ")

max_count = 0
most_frequent = ""

for ch in text:
    count = 0

    for x in text:
        if ch == x:
            count = count + 1

    if count > max_count:
        max_count = count
        most_frequent = ch

print("Most frequent character:", most_frequent)
print("Frequency:", max_count)