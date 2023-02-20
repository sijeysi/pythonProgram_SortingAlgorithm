array = [23, 14, 34, 74, 66, 69, 3, 10, 38, 57]

def bubble_sort(array):
    elements = len(array)

    for i in range(elements):
        for j in range(0, elements-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
    
print(bubble_sort(array))