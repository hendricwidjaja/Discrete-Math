def binarySearch(array, x):
# Initiates a variable named “low” to represent the current lowest element of the search interval (starts as the first element)
	low = 0
# Initiates a variable named “high” to represent the current highest element of the search interval (starts as the last element)
	high = len(array) - 1
# A while loop which continues to iterate until the desired element is returned or cannot be found
	while low <= high:
# Calculates the mid point of the current search interval
		mid = low + (high - low) // 2
# Checks if the element at the “mid” point is the desired element and returns the value if true
		if array[mid] == x:
			return mid
# Else, check if the midpoint is less than the desired value. If true, sets the element to the right of the midpoint as the new lower bound of the search interval
		elif array[mid] < x:
			low = mid + 1
# Else, determines that the desired value can only possibly be to the left of the midpoint. Thus setting the element to the left of the midpoint as the new higher bound of the search interval 
		else:
			high = mid - 1
# Returns -1 if the desired element could not be found within the array
	return -1