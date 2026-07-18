#Direct Recursion

def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)
n=int(input("Enter a value:"))
print(fact(n))
