a = float(input("Enter your first number : "))
b = float(input("Enter your second number : "))
opertor = input("Enter your opertor(+ , - , *, % , /)")

if opertor == "+" :
    print("Result : " , a + b )
elif opertor == "-":
    print("result: " , a - b )
elif opertor == "*":
    print("Result :" , a * b )
elif opertor == "%":
    print("Result : " , a / b)
else :
    print("Invalid opertor ")