#Check Armstrong Number: Write a function to check if a number is an Armstrong number.

def check(num):
    arr = [int(x) for x in str(num)]
    print(arr)

    result = 0
    for i in arr:
        result += i**3
    print("Sum:",result)

    if(result == num):
        print(f"{num} is an amstrong number")
    else:
        print(f"{num} is not an amstrong number")

num = int(input("Enter your number: "))
check(num)