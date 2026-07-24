#Second Occurrence of Target (Index Method)

arr = list(map(int, input("enter the elements:").split()))
target = int(input("enter the target:"))
index = -1
count = 0
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        count += 1
    if count == 2:
        print("second occurence of target:", index)
        break
if index != -1:
    print("second occurence of target:", index)
else:
    print("target not found")
