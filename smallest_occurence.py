#Smallest Element and Its Indexpython

arr = list(map(int, input("enter the elements:").split()))
min_element = arr[0]
f = -1
for i in range(len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]
        f = i
print("smallest element:", min_element)
print("index of smallest element:", f)


output:-
    enter the elements:1 2 3 4 5 6 7 8 9
    smallest element: 1
    index of smallest element: -1
