#Write a function to check if a given number is prime.
num = int(input("Enter the number: "))

def prime(num):
    if(num<2):
        print("Number is not prime")
    else:
        for i in range(2,num//2+1):
            if(num%i==0):
                print("Number is not prime")
                break
        else:
            print("Number is prime")

prime(num)