#Matrix Operations: Write a program to perform matrix addition.

r = int(input("NUmber of rows: "))
c = int(input("Number of columns: "))
m = []
n = []

#Take input for m
print("First matrix: ")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    m.append(a)

#Print M
for i in range(r):
    for j in range(c):
        print(m[i][j],end=" ")
    print()

#Take input for n
print("Second matrix: ")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    n.append(a)

#Print n
for i in range(r):
    for j in range(c):
        print(n[i][j],end=" ")
    print()

#Addiiton
o = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(m[i][j] + n[i][j])
    o.append(a)

#Other way:
#Additon 
# o=[]
# for i in range(r):
#     o.append([])
#     for j in range(c):
#         o[i].append(m[i][j]+n[i][j])


print("Result: ")
for i in range(r):
    for j in range(c):
        print(o[i][j],end=" ")
    print()