'''Merge Sort
                        Devide and conquer
Quick Sort'''

#Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = list(map(int, input("Enter the values: ").split()))
sorted_arr = merge_sort(arr)
print(*sorted_arr)


            output:-
            Enter the values: 3 7 1 8 3 6 23 9 1
            1 1 3 3 6 7 8 9 23
