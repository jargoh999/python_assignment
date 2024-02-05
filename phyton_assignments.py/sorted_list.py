def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(arr))


def bubble_sort2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


arr1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort2(arr1)
print(bubble_sort2(arr1))

print("\n")


def element_sort(number, arr):
    for i in range(len(arr)):
        if number == arr[i]:
            return f"element is present in index {i} "
    return "element not present"


arr2 = [64, 34, 25, 12, 22, 11, 90]
print(element_sort(11, arr2))

sample_set = {1, 2.5, 3.2, 21}
sample_set2 = {1, 2.5, 3.2, 45, 0.5, 120, 3, 0.1, 0.0}
print(sample_set)


