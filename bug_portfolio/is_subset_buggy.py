def is_subset(arr1, m, arr2, n): 
	hashset = set() 
	for i in range(0, m): 
		hashset.add(arr1[i]) 
	for i in range(1, n): # Bug: changed from 0 to 1
		if arr2[i] in hashset: 
			continue
		else: 
			return False

	return True
