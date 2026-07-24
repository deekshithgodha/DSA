#Second Occurrence of Target (Count Method)

arr = list(map(int, input("enter the elements:").split()))
target = int(input("enter the target:"))
count = 0
for i in range(len(arr)):
    if arr[i] == target:
        count += 1
    if count == 2:
        print("second occurence of target:", i)
        break
if count < 2:
    print("target not found")
