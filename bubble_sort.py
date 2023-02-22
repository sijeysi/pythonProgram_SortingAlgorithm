array = [23, 14, 34, 74, 66, 69, 3, 10, 38, 57] 

def bubble_sort(array):
    integers = len(array)
    
    for i in range(integers):
        for j in range(0, integers-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort(array)) 