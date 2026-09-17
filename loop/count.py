# Given a number, count how many digits it contains.

n = int(input("Enter number: "))

count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Number of digits:", count)