arr=list(map(int,input("enter the elements:").split())) 
target=int(input("enter the target:")) 
for i in range(len(arr)): 
    if arr[i]==target: 
        print("first occurence of target:",i) 
        break 
else: 
    print("target not found") 
