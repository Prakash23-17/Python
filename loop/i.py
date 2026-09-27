n = int(input("Enter number of terms: "))

a = 0
b = 1
total = 0

for i in range(n):
    total = total + a

    c = a + b
    a = b
    b = c

print("Sum:", total)