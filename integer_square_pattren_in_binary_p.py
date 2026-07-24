#integer sqaure pattern using bnary search pattern
n=int(input("Enter the number"))
left=0
right=n
ans=0
while left<=right:
    mid=(left+right)//2
    if mid * mid==n:
        ans=mid
        break
    elif mid*mid<n:
        ans=mid
        left=mid+1
    else:
        right=mid-1
    print("integer sqaure root:",ans)

     output:-
            Enter the number30
            integer sqaure root: 0
            integer sqaure root: 0
            integer sqaure root: 3
            integer sqaure root: 5
            integer sqaure root: 5

