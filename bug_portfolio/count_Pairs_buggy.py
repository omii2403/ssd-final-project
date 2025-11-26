def count_Pairs(arr,n): 
    cnt = 0; 
    for i in range(n): 
        for j in range(i+1 , n-1):  # Bug: should be range(i+1, n)
            if (arr[i] == arr[j]): 
                cnt += 1; 
    return cnt;