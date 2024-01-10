#Check Substring: Write a function to check if a string is a substring of another.

def check(str1,str2):
    if str2 in str1:
        return 1
str1 = input("Enter 1st string:")
str2 = input("Enter 2nd string:")
if check(str1,str2):
    print(f"{str2} is present in {str1}")
else:
    print(f"{str2} is not present in {str1}")
