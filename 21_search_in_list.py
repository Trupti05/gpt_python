#Search in List: Write a function to search for an element in a list.

def search(ele):
    if ele in list:
        print(ele,"is in list",list)
    else:
        print(ele,"is not in list",list)

list=[1,2,3,"abc",12.45]
ele = int(input("Enter search element: "))
search(ele)
