def part(arr, low, high):
    piv = arr[high]
    i = low - 1
    for j in range(low, high):
        # Change to < for ascending order, or keep > for descending order
        if arr[j] < piv: 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # FIXED: Swapped arr[j] with arr[i], not arr[i+1]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        piv = part(arr, low, high)
        quick_sort(arr, low, piv - 1)
        quick_sort(arr, piv + 1, high)  # FIXED: Passed piv + 1 as 'low' and high as 'high'

arr = list(map(int, input("Enter the elements: ").split()))
quick_sort(arr, 0, len(arr) - 1)
print(*arr)

   output:-
        Enter the elements: 0 4 7 3 9 1 8 2
        0 1 2 3 4 7 8 9

