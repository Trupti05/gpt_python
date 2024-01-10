#Calculate PI: Write a program to calculate the value of PI using the Monte Carlo method.

#Reference:
#   π    =(4/1)-(4/3)+(4/5)-(4/7)+(4/9)-(4/11)+(4/13)-(4/15)
#index       0    1     2     3     4      5      6

sum = 0
a = 1
for i in range(1000):
    if i%2==0:
        sum=sum+4/a
    else:
        sum=sum-4/a
    a+=2
print(sum)


