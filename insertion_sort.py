def insertionSort(arr):
# Starting at the 2nd element (index = 1), iterate through the entire array
    for i in range(1, len(arr)):
# Assigns the value of the selected element to a "key" variable.
        key = arr[i]
# The "j" variable is used as a tracker that is also compared to the “key” element
        j = i - 1
# This loop checks that the “key” is only compared to all the elements up to index[0]. It then compares and checks if the key is less than the element to its left (arr[j])
# This essentially shifts the “key” value to the left of the array until it finds an element that it is larger than.
        while j >= 0 and key < arr[j]:
# If the “key” is less than the element to its left, it changes its value to the same value of that element.
            arr[j + 1] = arr[j]
# It then changes the “j” variable (element tracker) to the next value to the left
            j -= 1
# Once the key finds an element that the key is larger than OR it has reached the beginning of the array, the “key” inserts itself into that index and secures its correct order in the array.
        arr[j + 1] = key