array = [23, 14, 34, 74, 66, 69, 3, 10, 38, 57]


def selection_sort(array):
    integers = len(array)

    for i in range(integers):
        min_index = i
        for j in range(i+1, integers):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

print(selection_sort(array))
