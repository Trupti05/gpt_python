# Write a function to convert a binary number to decimal.
def convert(str1):
    str2 = int(str1,2)
    print(f"The decimal value of {str1} is {str2}")

str1 = input("Enter your binary value: ")
convert(str1)

