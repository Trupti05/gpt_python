#Write a function to check if a given string is a palindrome.
def palin(str):
    reverse_str = str[::-1]
    if(str == reverse_str):
        return 1

str = input("Enter your string: ")
if(palin(str)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")