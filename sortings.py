'''Sortings
1.Bubble
2.selection
3.insertion
5 1 4 2 8 6 3  its check the 5>1 True,So ordered 1 5 4 2 8 6 3, till last seted to the order'''

arr=list(map(int ,input("Enter the number").split()))
n=len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1]=arr[j+1],arr[j]
print(*arr)

output:-    
    Enter the number5 3 2 1 6 4
    1 2 3 4 5 6
