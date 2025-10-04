#python calculator

operator= input("enter a operator(+ - * /): ")
n1=float(input("Enter the first number: "))
n2=float(input("Enter the second number: "))

if operator=="+":
    result=n1+n2
    print(round(result, 3))
elif operator=="-":
    result = n1 - n2
    print(round(result, 3))
elif operator=="*":
    result = n1 * n2
    print(round(result, 3))
elif operator=="/":
    result = n1 / n2
    print(round(result, 3))
elif operator=="":
    print("empty operator")
else:
    print(f"{operator} is not a valid operator")