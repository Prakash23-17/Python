# Given a number, find the sum of all its digits.

n = int(input("Enter number: "))

total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits:", total)