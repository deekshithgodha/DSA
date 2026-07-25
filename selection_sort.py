#SELECTION SORT
arr=list(map(int,input("Enter the value").split()))
n=len(arr)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(*arr)

        output:-
        Enter the value4 1 2 3 5
        1 2 3 4 5
