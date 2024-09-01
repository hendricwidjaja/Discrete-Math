def linearSearch(array, x):
# This creates a for loop to traverse through each element within the entire array, starting from the first element
    for i in range(len(array)):
# If the current element is equal to the desired element (x)
        if (array[i] == x): 
# Return the index value of where the desired element (x) is located
            return i
# Return an error message (or -1) if the desired element (x) could not be found within the array
    return -1