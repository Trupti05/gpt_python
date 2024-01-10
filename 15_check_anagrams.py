# Write a function to check if two strings are anagrams.
def are_anagram(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    print(sorted(str1))
    print(sorted(str2))
    return sorted(str1) == sorted(str2)

str1="gate"
str2="tage"




if(are_anagram(str1,str2)):
    print("It is anagram.")

else:
    print("It is not")
