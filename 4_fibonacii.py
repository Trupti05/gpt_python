#Write a function to generate the Fibonacci sequence up to a specified number of terms.
# def fibo(num):
#     if num<=1:
#         return(num)
#     else:
#         return (num-1) + (num-2)

# num = int(input("Enter range: "))
# if num<=0:
#     print("Enter valid input")
# else:
#     for i in range(num):
#         print(fibo(i),end=" ")

# Other method:

def fibo(num):
    n1=0
    n2=1
    if num==1:
        print(n2)
    else:
        print(n1)
        print(n2)
        for i in range(num):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            print(n3)
num = int(input("Enter range: "))
fibo(num)
