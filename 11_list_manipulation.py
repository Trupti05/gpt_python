# Write a program that removes duplicates from a list.
#Solution 1:
# def remove(input_list):
#     return set(input_list)

# input_list = [1,2,3,4,4,5,6,7,7,1]
# print("Original List:",input_list)
# print("List after removing duplicate:",remove(input_list))

def remove(input_list):
    unique_list=[]

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


input_list =  [1,2,3,4,4,5,6,7,7,1]
result=remove(input_list)
print("Original List:",input_list)
print("List after removing duplicate:",remove(input_list))

