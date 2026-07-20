'''Array Data Structures:
    -Linear common ds
    -int,float,ch/string'''

#Reverse an array with out slicing
arr=list(map(int, input("Enter the number").split()))
left=0
right=len(arr)-1
while left<right:
    arr[left], arr[right]=arr[right], arr[left]
    left+=1
    right-=1
print("Reversed array", *arr)

# Ask user for multiple numbers separated by spaces
'''arr = list(map(int, input("Enter the numbers: ").split())) 

left = 0 
right = len(arr) - 1 

# Properly indented while loop
while left < right: 
    arr[left], arr[right] = arr[right], arr[left] 
    left += 1 
    right -= 1 

print("Reversed array:", *arr)'''
    
    
