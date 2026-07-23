#binary Search
arr=list(map(int, input("Enter the elements:").split()))
target=int(input("Enter the element to be searched"))
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print("Element found at index:", mid)
        break
    elif target<arr[mid]:
        right=mid-1
    else:
        left+=mid+1
else:
    print("Element not in array..")
