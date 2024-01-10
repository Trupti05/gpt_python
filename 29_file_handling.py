#File Handling: Read and write data to a file using Python.

f=open("","r")
print(f.read())

f=open("","a")
f.write("Hello")
f.close()

with open("","r") as f:
    c = f.read()
    print(c)