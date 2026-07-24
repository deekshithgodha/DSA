#Pair Search for Target Sumpython

arr = list(map(int, input("enter the elements:").split()))
target_sum = int(input("enter the target sum:"))
found = False
for i in range(len(arr)):
    for j in range(i + 1):
        if arr[i] + arr[j] == target_sum:
            print("pair found is", arr[i], arr[j])
            print("pair found at", i, j)
            found = True
            break
    if found:
        break
if not found:
    print("pair not found")

output:-
        enter the elements:1 2 3 4 5 6 7 8 9 10
        enter the target sum:7
        pair found is 4 3
        pair found at 3 2
