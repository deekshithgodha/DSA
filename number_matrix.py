n=int(input("Enter the size of matrix:"))
arr=[[0]*n for _ in range(n)]
#print(arr)
top=0
left=0
right=n-1
bottom=n-1
num=1
while top<=bottom and left<=right:
    #in top, left-->right
    for i in range(left, right+1):
        arr[top][i]=num
        num+=1
    top+=1
    #in right, top-->bottom
    for i in range(top,bottom+1):
        arr[i][right]=num
        num+=1
    right-=1
    #in bottom, left-->right
    for i in range(left,left-1,-1):
        arr[bottom][i]=num
        num+=1
    bottom-=1
    #in left,bottom to top
    for i in range(bottom,top-1,-1):
        arr[i][left]=num
        num+=1
    left+=1
for row in arr:
    print(*row)
    
'''n = int(input("Enter the size of matrix: "))
arr = [[0] * n for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1
num = 1

while top <= bottom and left <= right:
    # 1. Fill Top Row: left -> right
    for i in range(left, right + 1):
        arr[top][i] = num
        num += 1
    top += 1

    # 2. Fill Right Column: top -> bottom
    for i in range(top, bottom + 1):
        arr[i][right] = num
        num += 1
    right -= 1

    # 3. Fill Bottom Row: right -> left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            arr[bottom][i] = num
            num += 1
        bottom -= 1

    # 4. Fill Left Column: bottom -> top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            arr[i][left] = num
            num += 1
        left += 1

# Print the resulting spiral matrix
for row in arr:
    print(*row)'''
