#Bubble Sort: Implement the Bubble Sort algorithm.

def bsort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]


ele = int(input("Enter number of elements: "))
print("Enter array:")
arr = []
for i in range(ele):
    element  = int(input())
    arr.append(element)

print("Original array:",arr)
bsort(arr)
print("Sorted array is:",arr)

