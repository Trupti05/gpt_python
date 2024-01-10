#Write a function that calculates the sum of the digits of a positive integer.
def s(num):
    return sum(int(x) for x in str(num))

num = int(input("Enter your integer: "))
print("The sum of digists is:",s(num))

# Another way of writing this code is as follows:
# def sum_of(num):
#     digit_sum = 0

#     for digit_char in str(num):
#         digit_sum+=int(digit_char)
#     return digit_sum

# num=input("Enter number: ")
# result = sum_of(num)
# print("The sum of digits is: ",result)
    