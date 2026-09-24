text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

counts = sorted(set(frequency.values()), reverse=True)

if len(counts) < 2:
    print("Second most frequent character does not exist")
else:
    second_count = counts[1]

    for ch in text:
        if frequency[ch] == second_count:
            print("Second most frequent character:", ch)
            print("Frequency:", second_count)
            break