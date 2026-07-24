#Largest Element and Its Indexpython

arr = list(map(int, input("enter the elements:").split()))
max_element = arr[0]
f = -1
for i in range(len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
        f = i
print("largest element:", max_element)
print("index of largest element:", f)

output:-
    enter the elements:1 2 3 4 7 2 17 3 9
    largest element: 17
    index of largest element: 6
