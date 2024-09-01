def intersection(set1, set2):
    intersection = [] # Create an empty array for intersection 
    set1_copy = set1[:] # Create a copy of set1 and store in variable named "set1_copy"
    for i in set1_copy: # for each number in set1_copy (set1)
        if i in set2 and i not in intersection: # if the number is in set2 and not already in the intersection array
              intersection.append(i) # append it to the intersection array
    return intersection 

result = intersection([1, 2, 3], [3, 4, 5, 1, 3])
print(result)