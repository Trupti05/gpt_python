#Write a function to check if a given year is a leap year.
# def leap(year):
#     if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# year = int(input("Enter year: "))

# if(leap(year)):
#     print("It is a leap year")
# else:
#     print("It is not a leap year")

def leap(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False

year = int(input("Enter year: "))
if(leap(year)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
