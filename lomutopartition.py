import math

# def lomutopartition(A,left,right):
#     p = A[left]
#     s=left
#     for i in range(left+1, right+1):
#         if A[i] < p:
#             s = s+1
#             Swap(A,s,i)
#     Swap(A,s,left)
#     return s

def lomuto_partition(arr, low, high):
    pivot = arr[low]  # Select the first element as the pivot
    i = low

    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[low] = arr[low], arr[i]
    return i

# Example usage:
arr = [51, 48, 17, 52, 62]
pivot_index = lomuto_partition(arr, 0, len(arr) - 1)
print("Array after Lomuto Partition:", arr)
print("Pivot element:", arr[pivot_index])