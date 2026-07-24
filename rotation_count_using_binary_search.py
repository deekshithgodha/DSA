#Rotating count using binary search pattern
arr=list(map(int, input("Enter the elements").split()))
left=0
right=len(arr)-1
while left<right:
    mid = (left+right)//2
    if arr[mid]>arr[right]:
        left=mid+1
    else:
        right=mid
print("Rotation count",left)
 output:-
    Enter the elements4 5 6 7 1 2 3
    Rotation count 4
