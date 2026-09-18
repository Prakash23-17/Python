# Input N and print all prime numbers from 1 to N.
n = int(input("Enter your number :"))
for n in range(2 , n +1):
    count = 0
    for i in range(1 , n + 1):
        if n % i == 0:
            count = count + 1 
            if count == 2:
                print(n)