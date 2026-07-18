#Tree based program
def tree(n):
    if n==0:
        return
    print(n)
    tree(n-1)
    tree(n-1)
n=int(input("Enter the number"))
tree(n)
