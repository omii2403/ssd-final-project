# Task 853: Write a python function to find sum of odd factors of a number.
import math
def sum_of_odd_Factors(n): 
    res = 1
    while n % 2 == 0: 
        n = n // 2 
    for i in range(3,int(math.sqrt(n) + 1)): 
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            count+=1 
            n = n // i 
            curr_term *= i 
            curr_sum += curr_term    
        res *= curr_sum

    # BUG: should be n >= 2 to account for odd prime factors, instead of n >= 4  
    if n >= 4: 
        res *= (1 + n) 
    return res
