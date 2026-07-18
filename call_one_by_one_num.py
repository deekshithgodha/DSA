#Calling one by one
def num(n):
    if n==0:
        return
    print(n, end="-")
    num(n-1)
n=int(input("Enter a value:"))
num(n)


input-6
output-6-5-4-3-2-1
