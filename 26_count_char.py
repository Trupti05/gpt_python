#Count Characters: Write a function to count the occurrences of each character in a string.

def count(str1):
    dict={}
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

str1 = input("Enter string: ")
print(count(str1))
