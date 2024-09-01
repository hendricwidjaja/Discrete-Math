def partition(arr, first, last):
# This chooses the last element in the array/sub-array as the pivot  
    pivot = arr[last]
# This initializes a variable called "i" which is used to capture the higher boundary of the array/sub-array which is less than the pivot.     
    i = first - 1
# A for loop to iterate through each element within the array/sub-array (determined by the range)
    for j in range(first, last):
# if the element is less than the pivot
        if arr[j] < pivot: 
# Increase the higher boundary of the elements that will be less than the pivot by 1
            i += 1 
# Then swaps the value (arr[j]) with another element, essentially moving arr[j] to the left hand side of the array/sub-array.
            arr[i], arr[j] = arr[j], arr[i]
# After iterating through the array/sub-array, swap the pivot element [last] with the right hand side neighbour [i + 1] of the elements that were smaller than the pivot element.
    arr[i + 1], arr[last] = arr[last], arr[i + 1]
# Increase i by 1. This returns the index of the pivot element, holds its place within the final array, and allows the next recursion to use this number to form the upper boundary of the left sub-array + lower boundary of the right sub-array
    return i + 1

# The Quicksort function implementation
def quick_sort(arr, first, last):
# This checks if the amount of elements within the array is more than 1x by comparing the first & last indices
    if first < last:
# This calls the partition function and assigns the return value as the next pivot
        pi = partition(arr, first, last)

# The below 2x lines of code calls the quicksort function and creates the left sub-array (elements less than the pivot) and right sub-array (elements greater than the pivot)
        quick_sort(arr, first, pi - 1) # left sub-array (less than pivot)
        quick_sort(arr, pi + 1, last) # right sub-array (greater than pivot)
