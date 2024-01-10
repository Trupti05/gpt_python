#Remove Vowels: Write a function to remove vowels from a string.

# def removev(str):
#     str1 = ""
#     list = ["a","e","i","o","u"]
#     for i in str:
#         if i not in list:
#             str1=str1+i
#     return str1

# str = input("Enter string: ")
# str.split()
# print("The resultant string is:",removev(str))

#or

def removev(str):
    str = str.replace(" ","").lower()
    str = sorted(str)
    print(str)
    str1 = ""
    list = ["a","e","i","o","u"]
    for i in str:
        if i not in list:
            str1=str1+i
    return str1

str = input("Enter string: ")
str.split()
print("The resultant string is:",removev(str))