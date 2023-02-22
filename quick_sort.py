array = [23, 14, 34, 74, 66, 69, 3, 10, 38, 57]

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = []
        right = []
        for i in range(1, len(array)):
            if array[i] < pivot:
                left.append(array[i])
            else:
                right.append(array[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))