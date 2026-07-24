#first occurence


arr = list(map(int, input("Enter the elements separated by space: ").split()))


target = int(input("Enter the target: "))


for i in range(len(arr)):
    if arr[i] == target:
        print("First occurrence of target:", i)
        break
else:

    print("Target not found")
