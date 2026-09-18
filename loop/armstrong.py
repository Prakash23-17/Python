# Check whether a number is an Armstrong number.

n = int(input ("Enter your number :"))
origanl = n
total = 0

while n > 0:
    digit = n % 10
    total = total + digit ** 3 
    n = n // 10
    if total == origanl:
        print("ArmStrong  number ")
    else:
        print("Not ArmStrong number ")