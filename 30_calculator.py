#Calculator: Create a simple calculator program that can perform basic arithmetic operations.

def calc(num1,num2,opr):
    if(opr == "+"):
        print(f"{num1} + {num2} = {num1+num2}")
    elif(opr == "-"):
        print(f"{num1} - {num2} = {num1-num2}")
    elif(opr == "*"):
        print(f"{num1} * {num2} = {num1*num2}")
    elif(opr == "/"):
        print(f"{num1} / {num2} = {num1/num2}")
    elif(opr == "%"):
        print(f"{num1} % {num2} = {num1%num2}")
    elif(opr == "//"):
        print(f"{num1} // {num2} = {num1//num2}")
    else:
        print("Enter valid operator!!!")


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
opr = input("Enter arithmetic operator: ")
calc(num1,num2,opr)