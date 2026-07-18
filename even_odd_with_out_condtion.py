#TS=O(n) , S.C=O(1)
import math
n=int(input("Enter the a term:"))
sum=0
odd=1
even=2
for i in range(n):
    term=odd/math.factorial(even)
    print(f"Term {i+1}=/{even}!={term}")
    sum=sum+term
    odd=odd+2
    even+=2
print(sum)
