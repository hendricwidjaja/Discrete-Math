def union(set1, set2):
	# This creates a copy using splicing "[:]" of set1 and assigns it to a variable named union
	union = set1[:]
	for i in set2: # for each numnber in set2
		if i not in union: # if that number is not in union (set1) - gets rid of duplicates
			union.append(i) # append the number to the union variable
	return union