def union(set1, set2):
	# This creates a copy using splicing "[:]" of set1 and assigns it to a variable named union
	union = set1[:]
	for i in set2: # for each numnber in set2
		if i not in union: # if that number is not in union (set1) - gets rid of duplicates
			union.append(i) # append the number to the union variable
	return union

def intersection(set1, set2):
    intersection = [] # Create an empty array for intersection 
    set1_copy = set1[:] # Create a copy of set1 and store in variable named "set1_copy"
    for i in set1_copy: # for each number in set1_copy (set1)
        if i in set2 and i not in intersection: # if the number is in set2 and not already in the intersection array
              intersection.append(i) # append it to the intersection array
    return intersection 

def symmetric_difference(set1, set2):
    symmetric_difference_arr = [] # Create an empty symmetric difference array
    union_set = union(set1, set2) # Utilise union function to create an array of union for set1 & set2
    intersection_set = intersection(set1, set2) # Utilise intersection function to create an array for intersection of set1 & set2
    for i in union_set: # for each number in the union array
          if i not in intersection_set: # if the number is not in the intersection array
                symmetric_difference_arr.append(i) # Append the number to the symmetric difference array

    return symmetric_difference_arr
    
set1 = [1, 2, 3]    
set2 = [3, 4, 5]

result = symmetric_difference(set1, set2)

print(union(set1, set2)) # Result = [1, 2, 3, 4, 5]
print(intersection(set1, set2)) # Result = [3]
print(result) # Result = [1, 2, 4, 5]