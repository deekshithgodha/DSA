#searching in arrays
# 1. extract the index
# 2. first occurence
# 3. last occurence
# 4. count of occurence
# 5. largest/smallest
# 6. pair search
# 7. missing number search [1,2,3,5]

arr=list(map(int,input("enter the elements:").split())) 
target=int(input("enter the target:")) 
found=False 
for i in range(len(arr)): 
    if arr[i]==target: 
        print("index of target:",i) 
        found=True 
        break 
if not found: 
    print("target not found") 

