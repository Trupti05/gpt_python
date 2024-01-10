#GCD (Greatest Common Divisor): Write a function to find the GCD of two numbers.

#using inbuilt function
# import math 
# def gcd1(ele1,ele2):
#     return math.gcd(ele1,ele2)

# ele1 = int(input("Enter 1st number: "))
# ele2 = int(input("Enter 2nd number: "))
# print(f"The gcd of {ele1} and {ele2} is {gcd1(ele1,ele2)}")

#without using inbuilt function(using Euclidean algorithm)
def gcd(num1,num2):
    while num2:
        num1, num2 = num2 , num1%num2
    return abs(num1)

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print(f"GCD of {num1} and {num2} is {gcd(num1,num2)}")