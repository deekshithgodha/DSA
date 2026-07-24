#Last Occurrence of Targetpython

arr = list(map(int, input("enter the elements:").split()))
target = int(input("enter the target:"))
index = -1
for i in range(len(arr)):
    if arr[i] == target:
        index = i
if index != -1:
    print("last occurence of target:", index)
else:
    print("target not found")

        output:-
        enter the elements:1 2 3 4 5 6 7 8 9 0
        enter the target:9
        last occurence of target: 8
