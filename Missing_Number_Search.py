#Missing Number Search (Using Last Element)python

arr = list(map(int, input("enter the elements:").split()))
ele = arr[-1]
s = 0
a = sum(arr)
for i in range(ele + 1):
    s += i
print("missing element:", s - a)
