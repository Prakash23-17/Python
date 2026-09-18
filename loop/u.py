# Check whether a number is prime or not.

n = int(input("Enter your number :"))

count = 0

for i in range(1, n+1):
    if n % i == 0:
        count = count + 1

        if count == 2 :
            print("Prime")
        else:
            print("Not prime ")