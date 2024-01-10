#Create a dictionary and perform operations like adding, updating, and deleting items.
dict={1:'apple',2:'ball',3:'cat'}
print("The original list is:",dict)

#adding item
dict[4]='dog'
print("List after adding item:",dict)

#update item
dict[1]='Annabella'
print("List after updating list:",dict)

#delete item
# if 4 in dict:
#     del dict[4]
#or we can also delete item using dog value show as follows:
for key,value in list(dict.items()):
    if value=='dog':
        del dict[key]

print("List after deleting item:",dict)
