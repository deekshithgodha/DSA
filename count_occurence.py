#Count of Occurrencespython

arr = list(map(int, input("enter the elements:").split()))
target = int(input("enter the target:"))
count = 0
for i in range(len(arr)):
    if arr[i] == target:
        count += 1
if count == 0:
    print("target not found")
print("count of occurence of target:", count)

output:-
enter the elements:1 2 3 4 5 6 7 8 9
enter the target:6
count of occurence of target: 1
