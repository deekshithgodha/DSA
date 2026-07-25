#insertion sort
arr=list(map(int,input("Enter the value").split()))
n=len(arr)
for i in range(1,n):
    x=arr[i]
    j=i-1
    while j>=0 and arr[j]>x:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=x
print(*arr)


        output:
         Enter the value4  1 3 2 5 0
         0 1 2 3 4 5
    
