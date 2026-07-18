#In-direct recursion - i'm trying to check
def even(n):
    if n==0:
        return True
    return odd(n-1)
def odd(n):
    if n==0:
        return False
    return even(n-1)
n=int(input("Enter the value:"))
print(even(n))
