# Write a function to calculate the factorial of a given number.
def factorial(num):
    if(num==1):
        return 1
    elif(num==0):
        return 1
    return num*factorial(num-1)


num = int(input("Enter your number: "))
fact = factorial(num)
print("THe factorial of ",num,"is",fact)
