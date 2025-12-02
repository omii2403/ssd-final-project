
# Task 850: Write a function to check if a triangle of positive area is possible with the given angles.
def is_triangleexists(a,b,c): 
    if(a != 0 and b != 0 and c != 0 and (a + b + c)== 180): 
        if((a + b)>= c or (b + c)>= a or (a + c)>= b): 
            return True 
        else:
            return False
    else:
        return False

# Task 851: Write a python function to find sum of inverse of divisors.
def Sum_of_Inverse_Divisors(N,Sum): 
    ans = float(Sum)*1.0 /float(N);  
    return round(ans,2);

# Task 852: Write a python function to remove negative numbers from a list.
def remove_negs(num_list): 
    for item in num_list: 
        if item < 0: 
           num_list.remove(item) 
    return num_list

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
    if n >= 2: 
        res *= (1 + n) 
    return res

# Task 854: Write a function which accepts an arbitrary list and converts it to a heap using heap queue algorithm.
import heapq as hq
def raw_heap(rawheap):
  hq.heapify(rawheap)
  return rawheap

# Task 855: Write a python function to check for even parity of a given number.
def check_Even_Parity(x): 
    parity = 0
    while (x != 0): 
        x = x & (x - 1) 
        parity += 1
    if (parity % 2 == 0): 
        return True
    else: 
        return False

# Task 856: Write a python function to find minimum adjacent swaps required to sort binary array.
def find_Min_Swaps(arr,n) : 
    noOfZeroes = [0] * n 
    count = 0 
    noOfZeroes[n - 1] = 1 - arr[n - 1] 
    for i in range(n-2,-1,-1) : 
        noOfZeroes[i] = noOfZeroes[i + 1] 
        if (arr[i] == 0) : 
            noOfZeroes[i] = noOfZeroes[i] + 1
    for i in range(0,n) : 
        if (arr[i] == 1) : 
            count = count + noOfZeroes[i] 
    return count

# Task 857: Write a function to list out the list of given strings individually using map function.
def listify_list(list1):
  result = list(map(list,list1)) 
  return result

# Task 858: Write a function to count number of lists in a given list of lists and square the count.
def count_list(input_list): 
    return (len(input_list))**2

# Task 859: Write a function to generate all sublists of a given list.
from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs

# Task 860: Write a function to check whether the given string is ending with only alphanumeric characters or not using regex.
import re 
regex = '[a-zA-z0-9]$'
def check_alphanumeric(string): 
	if(re.search(regex, string)): 
		return ("Accept") 
	else: 
		return ("Discard")

# Task 861: Write a function to find all anagrams of a string in a given list of strings using lambda function.
from collections import Counter 
def anagram_lambda(texts,str):
  result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
  return result

# Task 862: Write a function to find the occurrences of n most common words in a given text.
from collections import Counter
import re
def n_common_words(text,n):
  words = re.findall('\w+',text)
  n_common_words= Counter(words).most_common(n)
  return list(n_common_words)

# Task 863: Write a function to find the length of the longest sub-sequence such that elements in the subsequences are consecutive integers.
def find_longest_conseq_subseq(arr, n): 
	ans = 0
	count = 0
	arr.sort() 
	v = [] 
	v.append(arr[0]) 
	for i in range(1, n): 
		if (arr[i] != arr[i - 1]): 
			v.append(arr[i]) 
	for i in range(len(v)): 
		if (i > 0 and v[i] == v[i - 1] + 1): 
			count += 1
		else: 
			count = 1
		ans = max(ans, count) 
	return ans

# Task 864: Write a function to find palindromes in a given list of strings using lambda function.
def palindrome_lambda(texts):
  result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
  return result

# Task 865: Write a function to print n-times a list using map function.
def ntimes_list(nums,n):
    result = map(lambda x:n*x, nums) 
    return list(result)

# Task 866: Write a function to check whether the given month name contains 31 days or not.
def check_monthnumb(monthname2):
  if(monthname2=="January" or monthname2=="March"or monthname2=="May" or monthname2=="July" or monthname2=="Augest" or monthname2=="October" or monthname2=="December"):
    return True
  else:
    return False

# Task 867: Write a python function to add a minimum number such that the sum of array becomes even.
def min_Num(arr,n):  
    odd = 0
    for i in range(n): 
        if (arr[i] % 2): 
            odd += 1 
    if (odd % 2): 
        return 1
    return 2

# Task 868: Write a python function to find the length of the last word in a given string.
def length_Of_Last_Word(a): 
    l = 0
    x = a.strip() 
    for i in range(len(x)): 
        if x[i] == " ": 
            l = 0
        else: 
            l += 1
    return l

# Task 869: Write a function to remove sublists from a given list of lists, which are outside a given range.
def remove_list_range(list1, leftrange, rigthrange):
   result = [i for i in list1 if (min(i)>=leftrange and max(i)<=rigthrange)]
   return result

# Task 870: Write a function to calculate the sum of the positive numbers of a given list of numbers using lambda function.
def sum_positivenum(nums):
  sum_positivenum = list(filter(lambda nums:nums>0,nums))
  return sum(sum_positivenum)

# Task 871: Write a python function to check whether the given strings are rotations of each other or not.
def are_Rotations(string1,string2): 
    size1 = len(string1) 
    size2 = len(string2) 
    temp = '' 
    if size1 != size2: 
        return False
    temp = string1 + string1 
    if (temp.count(string2)> 0): 
        return True
    else: 
        return False

# Task 872: Write a function to check if a nested list is a subset of another nested list.
def check_subset(list1,list2): 
    return all(map(list1.__contains__,list2))

# Task 873: Write a function to solve the fibonacci sequence using recursion.
def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

# Task 874: Write a python function to check if the string is a concatenation of another string.
def check_Concat(str1,str2):
    N = len(str1)
    M = len(str2)
    if (N % M != 0):
        return False
    for i in range(N):
        if (str1[i] != str2[i % M]):
            return False         
    return True

# Task 875: Write a function to find the minimum difference in the tuple pairs of given tuples.
def min_difference(test_list):
  temp = [abs(b - a) for a, b in test_list]
  res = min(temp)
  return (res)

# Task 876: Write a python function to find lcm of two positive integers.
def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y
   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1
   return lcm

# Task 877: Write a python function to sort the given string.
def sort_String(str) : 
    str = ''.join(sorted(str)) 
    return (str)

# Task 878: Write a function to check if the given tuple contains only k elements.
def check_tuples(test_tuple, K):
  res = all(ele in K for ele in test_tuple)
  return (res)

# Task 879: Write a function that matches a string that has an 'a' followed by anything, ending in 'b' by using regex.
import re
def text_match(text):
  patterns = 'a.*?b$'
  if re.search(patterns,  text):
    return ('Found a match!')
  else:
    return ('Not matched!')

# Task 880: Write a python function to find number of solutions in quadratic equation.
def Check_Solution(a,b,c) : 
    if ((b*b) - (4*a*c)) > 0 : 
        return ("2 solutions") 
    elif ((b*b) - (4*a*c)) == 0 : 
        return ("1 solution") 
    else : 
        return ("No solutions")

# Task 881: Write a function to find the sum of first even and odd number of a given list.
def sum_even_odd(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even+first_odd)

# Task 882: Write a function to caluclate perimeter of a parallelogram.
def parallelogram_perimeter(b,h):
  perimeter=2*(b*h)
  return perimeter

# Task 883: Write a function to find numbers divisible by m and n from a list of numbers using lambda function.
def div_of_nums(nums,m,n):
 result = list(filter(lambda x: (x % m == 0 and x % n == 0), nums)) 
 return result

# Task 884: Write a python function to check whether all the bits are within a given range or not.
def all_Bits_Set_In_The_Given_Range(n,l,r): 
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1) 
    new_num = n & num 
    if (num == new_num): 
        return True
    return False

# Task 885: Write a python function to check whether the two given strings are isomorphic to each other or not.
def is_Isomorphic(str1,str2):          
    dict_str1 = {}
    dict_str2 = {}
    for i, value in enumerate(str1):
        dict_str1[value] = dict_str1.get(value,[]) + [i]        
    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value,[]) + [j]
    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        return True
    else:
        return False

# Task 886: Write a function to add all the numbers in a list and divide it with the length of the list.
def sum_num(numbers):
    total = 0
    for x in numbers:
        total += x
    return total/len(numbers)

# Task 887: Write a python function to check whether the given number is odd or not using bitwise operator.
def is_odd(n) : 
    if (n^1 == n-1) :
        return True; 
    else :
        return False;

# Task 888: Write a function to substract the elements of the given nested tuples.
def substract_elements(test_tup1, test_tup2):
  res = tuple(tuple(a - b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res)

# Task 889: Write a function to reverse each list in a given list of lists.
def reverse_list_lists(lists):
    for l in lists:
        l.sort(reverse = True)
    return lists

# Task 890: Write a python function to find the index of an extra element present in one sorted array.
def find_Extra(arr1,arr2,n) : 
    for i in range(0, n) : 
        if (arr1[i] != arr2[i]) : 
            return i 
    return n

# Task 891: Write a python function to check whether the given two numbers have same number of digits or not.
def same_Length(A,B): 
    while (A > 0 and B > 0): 
        A = A / 10; 
        B = B / 10; 
    if (A == 0 and B == 0): 
        return True; 
    return False;

# Task 892: Write a function to remove multiple spaces in a string.
import re
def remove_spaces(text):
 return (re.sub(' +',' ',text))

# Task 893: Write a python function to get the last element of each sublist.
def Extract(lst): 
    return [item[-1] for item in lst]

# Task 894: Write a function to convert the given string of float type into tuple.
def float_to_tuple(test_str):
  res = tuple(map(float, test_str.split(', ')))
  return (res)

# Task 895: Write a function to find the maximum sum of subsequences of given array with no adjacent elements.
def max_sum_subseq(A):
    n = len(A)
    if n == 1:
        return A[0]
    look_up = [None] * n
    look_up[0] = A[0]
    look_up[1] = max(A[0], A[1])
    for i in range(2, n):
        look_up[i] = max(look_up[i - 1], look_up[i - 2] + A[i])
        look_up[i] = max(look_up[i], A[i])
    return look_up[n - 1]

# Task 896: Write a function to sort a list in increasing order by the last element in each tuple from a given list of non-empty tuples.
def last(n):
   return n[-1]
def sort_list_last(tuples):
  return sorted(tuples, key=last)

# Task 897: Write a python function to check whether the word is present in a given sentence or not.
def is_Word_Present(sentence,word): 
    s = sentence.split(" ") 
    for i in s:  
        if (i == word): 
            return True
    return False

# Task 898: Write a function to extract specified number of elements from a given list, which follow each other continuously.
from itertools import groupby 
def extract_elements(numbers, n):
    result = [i for i, j in groupby(numbers) if len(list(j)) == n] 
    return result

# Task 899: Write a python function to check whether an array can be sorted or not by picking only the corner elements.
def check(arr,n): 
    g = 0 
    for i in range(1,n): 
        if (arr[i] - arr[i - 1] > 0 and g == 1): 
            return False
        if (arr[i] - arr[i] < 0): 
            g = 1
    return True

# Task 900: Write a function where a string will start with a specific number.
import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False

# Task 901: Write a function to find the smallest multiple of the first n numbers.
def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

# Task 902: Write a function to combine two dictionaries by adding values for common keys.
from collections import Counter
def add_dict(d1,d2):
   add_dict = Counter(d1) + Counter(d2)
   return add_dict

# Task 903: Write a python function to count the total unset bits from 1 to n.
def count_Unset_Bits(n) :  
    cnt = 0;  
    for i in range(1,n + 1) : 
        temp = i;  
        while (temp) :  
            if (temp % 2 == 0) : 
                cnt += 1;  
            temp = temp // 2;  
    return cnt;

# Task 904: Write a function to return true if the given number is even else return false.
def even_num(x):
  if x%2==0:
     return True
  else:
    return False

# Task 905: Write a python function to find the sum of squares of binomial co-efficients.
def factorial(start,end): 
    res = 1 
    for i in range(start,end + 1): 
        res *= i      
    return res 
def sum_of_square(n): 
   return int(factorial(n + 1, 2 * n)  /factorial(1, n))

# Task 906: Write a function to extract year, month and date from a url by using regex.
import re
def extract_date(url):
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)

# Task 907: Write a function to print the first n lucky numbers.
def lucky_num(n):
 List=range(-1,n*n+9,2)
 i=2
 while List[i:]:List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1
 return List[1:n+1]

# Task 908: Write a function to find the fixed point in the given array.
def find_fixed_point(arr, n): 
	for i in range(n): 
		if arr[i] is i: 
			return i 
	return -1

# Task 909: Write a function to find the previous palindrome of a specified number.
def previous_palindrome(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x

# Task 910: Write a function to validate a gregorian date.
import datetime
def check_date(m, d, y):
    try:
        m, d, y = map(int, (m, d, y))
        datetime.date(y, m, d)
        return True
    except ValueError:
        return False

# Task 911: Write a function to compute maximum product of three numbers of a given array of integers using heap queue algorithm.
def maximum_product(nums):
    import heapq
    a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
    return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])

# Task 912: Write a function to find ln, m lobb number.
def binomial_coeff(n, k): 
	C = [[0 for j in range(k + 1)] 
			for i in range(n + 1)] 
	for i in range(0, n + 1): 
		for j in range(0, min(i, k) + 1): 
			if (j == 0 or j == i): 
				C[i][j] = 1
			else: 
				C[i][j] = (C[i - 1][j - 1] 
							+ C[i - 1][j]) 
	return C[n][k] 
def lobb_num(n, m): 
	return (((2 * m + 1) *
		binomial_coeff(2 * n, m + n)) 
					/ (m + n + 1))

# Task 913: Write a function to check for a number at the end of a string.
import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

# Task 914: Write a python function to check whether the given string is made up of two alternating characters or not.
def is_Two_Alter(s):  
    for i in range (len( s) - 2) : 
        if (s[i] != s[i + 2]) : 
            return False
    if (s[0] == s[1]): 
        return False
    return True

# Task 915: Write a function to rearrange positive and negative numbers in a given array using lambda function.
def rearrange_numbs(array_nums):
  result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
  return result

# Task 916: Write a function to find if there is a triplet in the array whose sum is equal to a given value.
def find_triplet_array(A, arr_size, sum): 
	for i in range( 0, arr_size-2): 
		for j in range(i + 1, arr_size-1): 
			for k in range(j + 1, arr_size): 
				if A[i] + A[j] + A[k] == sum: 
					return  A[i],A[j],A[k] 
					return True
	return False

# Task 917: Write a function to find the sequences of one upper case letter followed by lower case letters.
import re
def text_uppercase_lowercase(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return ('Not matched!')

# Task 918: Write a function to count coin change.
def coin_change(S, m, n): 
    table = [[0 for x in range(m)] for x in range(n+1)] 
    for i in range(m): 
        table[0][i] = 1
    for i in range(1, n+1): 
        for j in range(m): 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0 
            table[i][j] = x + y   
    return table[n][m-1]

# Task 919: Write a python function to multiply all items in the list.
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

# Task 920: Write a function to remove all tuples with all none values in the given tuple list.
def remove_tuple(test_list):
  res = [sub for sub in test_list if not all(ele == None for ele in sub)]
  return (str(res))

# Task 921: Write a function to perform chunking of tuples each of size n.
def chunk_tuples(test_tup, N):
  res = [test_tup[i : i + N] for i in range(0, len(test_tup), N)]
  return (res)

# Task 922: Write a function to find a pair with the highest product from a given array of integers.
def max_product(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return None     
    x = arr[0]; y = arr[1]    
    for i in range(0, arr_len): 
        for j in range(i + 1, arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y

# Task 923: Write a function to find the length of the shortest string that has both str1 and str2 as subsequences.
def super_seq(X, Y, m, n):
	if (not m):
		return n
	if (not n):
		return m
	if (X[m - 1] == Y[n - 1]):
		return 1 + super_seq(X, Y, m - 1, n - 1)
	return 1 + min(super_seq(X, Y, m - 1, n),	super_seq(X, Y, m, n - 1))

# Task 924: Write a function to find maximum of two numbers.
def max_of_two( x, y ):
    if x > y:
        return x
    return y

# Task 925: Write a python function to calculate the product of all the numbers of a given tuple.
def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product

# Task 926: Write a function to find n-th rencontres number.
def binomial_coeffi(n, k): 
	if (k == 0 or k == n): 
		return 1
	return (binomial_coeffi(n - 1, k - 1) 
		+ binomial_coeffi(n - 1, k)) 
def rencontres_number(n, m): 
	if (n == 0 and m == 0): 
		return 1
	if (n == 1 and m == 0): 
		return 0
	if (m == 0): 
		return ((n - 1) * (rencontres_number(n - 1, 0)+ rencontres_number(n - 2, 0))) 
	return (binomial_coeffi(n, m) * rencontres_number(n - m, 0))

# Task 927: Write a function to calculate the height of the given binary tree.
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def max_height(node): 
	if node is None: 
		return 0 ; 
	else : 
		left_height = max_height(node.left) 
		right_height = max_height(node.right) 
		if (left_height > right_height): 
			return left_height+1
		else: 
			return right_height+1

# Task 928: Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
        return change_date_format(dt)

# Task 929: Write a function to count repeated items of a tuple.
def count_tuplex(tuplex,value):  
  count = tuplex.count(value)
  return count

# Task 930: Write a function that matches a string that has an a followed by zero or more b's by using regex.
import re
def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return ('Found a match!')
        else:
                return ('Not matched!')

# Task 931: Write a function to calculate the sum of series 1³+2³+3³+….+n³.
import math 
def sum_series(number):
 total = 0
 total = math.pow((number * (number + 1)) /2, 2)
 return total

# Task 932: Write a function to remove duplicate words from a given list of strings.
def remove_duplic_list(l):
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return temp

# Task 933: Write a function to convert camel case string to snake case string by using regex.
import re
def camel_to_snake(text):
  str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

# Task 934: Write a function to find the nth delannoy number.
def dealnnoy_num(n, m): 
	if (m == 0 or n == 0) : 
		return 1
	return dealnnoy_num(m - 1, n) + dealnnoy_num(m - 1, n - 1) + dealnnoy_num(m, n - 1)

# Task 935: Write a function to calculate the sum of series 1²+2²+3²+….+n².
def series_sum(number):
 total = 0
 total = (number * (number + 1) * (2 * number + 1)) / 6
 return total

# Task 936: Write a function to re-arrange the given tuples based on the given ordered list.
def re_arrange_tuples(test_list, ord_list):
  temp = dict(test_list)
  res = [(key, temp[key]) for key in ord_list]
  return (res)

# Task 937: Write a function to count the most common character in a given string.
from collections import Counter 
def max_char(str1):
    temp = Counter(str1) 
    max_char = max(temp, key = temp.get)
    return max_char

# Task 938: Write a function to find three closest elements from three sorted arrays.
import sys 

def find_closet(A, B, C, p, q, r): 
	diff = sys.maxsize 
	res_i = 0
	res_j = 0
	res_k = 0
	i = 0
	j = 0
	k = 0
	while(i < p and j < q and k < r): 
		minimum = min(A[i], min(B[j], C[k])) 
		maximum = max(A[i], max(B[j], C[k])); 
		if maximum-minimum < diff: 
			res_i = i 
			res_j = j 
			res_k = k 
			diff = maximum - minimum; 
		if diff == 0: 
			break
		if A[i] == minimum: 
			i = i+1
		elif B[j] == minimum: 
			j = j+1
		else: 
			k = k+1
	return A[res_i],B[res_j],C[res_k]

# Task 939: Write a function to sort a list of dictionaries using lambda function.
def sorted_models(models):
 sorted_models = sorted(models, key = lambda x: x['color'])
 return sorted_models

# Task 940: Write a function to sort the given array by using heap sort.
def heap_sort(arr):
    heapify(arr)  
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shift_down(arr, 0, end - 1)
        end -= 1
    return arr

def heapify(arr):
    start = len(arr) // 2
    while start >= 0:
        shift_down(arr, start, len(arr) - 1)
        start -= 1
def shift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return

# Task 941: Write a function to count the elements in a list until an element is a tuple.
def count_elim(num):
  count_elim = 0
  for n in num:
    if isinstance(n, tuple):
        break
    count_elim += 1
  return count_elim

# Task 942: Write a function to check if any list element is present in the given list.
def check_element(test_tup, check_list):
  res = False
  for ele in check_list:
    if ele in test_tup:
      res = True
      break
  return (res)

# Task 943: Write a function to combine two given sorted lists using heapq module.
from heapq import merge
def combine_lists(num1,num2):
  combine_lists=list(merge(num1, num2))
  return combine_lists

# Task 944: Write a function to separate and print the numbers and their position of a given string.
import re
def num_position(text):
 for m in re.finditer("\d+", text):
    return m.start()

# Task 945: Write a function to convert the given tuples into set.
def tuple_to_set(t):
  s = set(t)
  return (s)

# Task 946: Write a function to find the most common elements and their counts of a specified text.
from collections import Counter 
def most_common_elem(s,a):
  most_common_elem=Counter(s).most_common(a)
  return most_common_elem

# Task 947: Write a python function to find the length of the shortest word.
def len_log(list1):
    min=len(list1[0])
    for i in list1:
        if len(i)<min:
            min=len(i)
    return min

# Task 948: Write a function to get an item of a tuple.
def get_item(tup1,index):
  item = tup1[index]
  return item

# Task 949: Write a function to sort the given tuple list basis the total digits in tuple.
def count_digs(tup):
  return sum([len(str(ele)) for ele in tup ]) 
def sort_list(test_list):
  test_list.sort(key = count_digs)
  return (str(test_list))

# Task 950: Write a function to display sign of the chinese zodiac for given year.
def chinese_zodiac(year):
 if (year - 2000) % 12 == 0:
     sign = 'Dragon'
 elif (year - 2000) % 12 == 1:
     sign = 'Snake'
 elif (year - 2000) % 12 == 2:
     sign = 'Horse'
 elif (year - 2000) % 12 == 3:
     sign = 'sheep'
 elif (year - 2000) % 12 == 4:
     sign = 'Monkey'
 elif (year - 2000) % 12 == 5:
     sign = 'Rooster'
 elif (year - 2000) % 12 == 6:
     sign = 'Dog'
 elif (year - 2000) % 12 == 7:
     sign = 'Pig'
 elif (year - 2000) % 12 == 8:
     sign = 'Rat'
 elif (year - 2000) % 12 == 9:
     sign = 'Ox'
 elif (year - 2000) % 12 == 10:
     sign = 'Tiger'
 else:
     sign = 'Hare'
 return sign

# Task 951: Write a function to find the maximum of similar indices in two lists of tuples.
def max_similar_indices(test_list1, test_list2):
  res = [(max(x[0], y[0]), max(x[1], y[1]))
   for x, y in zip(test_list1, test_list2)]
  return (res)

# Task 952: Write a function to compute the value of ncr mod p.
def nCr_mod_p(n, r, p): 
	if (r > n- r): 
		r = n - r 
	C = [0 for i in range(r + 1)] 
	C[0] = 1 
	for i in range(1, n + 1): 
		for j in range(min(i, r), 0, -1): 
			C[j] = (C[j] + C[j-1]) % p 
	return C[r]

# Task 953: Write a python function to find the minimun number of subsets with distinct elements.
def subset(ar, n): 
    res = 0
    ar.sort() 
    for i in range(0, n) : 
        count = 1
        for i in range(n - 1): 
            if ar[i] == ar[i + 1]: 
                count+=1
            else: 
                break 
        res = max(res, count)  
    return res

# Task 954: Write a function that gives profit amount if the given amount has profit else return none.
def profit_amount(actual_cost,sale_amount): 
 if(actual_cost > sale_amount):
    amount = actual_cost - sale_amount
    return amount
 else:
    return None

# Task 955: Write a function to find out, if the given number is abundant.
def is_abundant(n):
    fctrsum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctrsum > n

# Task 956: Write a function to split the given string at uppercase letters by using regex.
import re
def split_list(text):
  return (re.findall('[A-Z][^A-Z]*', text))

# Task 957: Write a python function to get the position of rightmost set bit.
import math
def get_First_Set_Bit_Pos(n):
     return math.log2(n&-n)+1

# Task 958: Write a function to convert an integer into a roman numeral.
def int_to_roman( num):
        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

# Task 959: Write a python function to find the average of a list.
def Average(lst): 
    return sum(lst) / len(lst)

# Task 960: Write a function to solve tiling problem.
def get_noOfways(n):
    if (n == 0):
        return 0;
    if (n == 1):
        return 1; 
    return get_noOfways(n - 1) + get_noOfways(n - 2);

# Task 961: Write a function to convert a roman numeral to an integer.
def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

# Task 962: Write a python function to find the sum of all even natural numbers within the range l and r.
def sum_Natural(n): 
    sum = (n * (n + 1)) 
    return int(sum) 
def sum_Even(l,r): 
    return (sum_Natural(int(r / 2)) - sum_Natural(int((l - 1) / 2)))

# Task 963: Write a function to calculate the discriminant value.
def discriminant_value(x,y,z):
    discriminant = (y**2) - (4*x*z)
    if discriminant > 0:
        return ("Two solutions",discriminant)
    elif discriminant == 0:
        return ("one solution",discriminant)
    elif discriminant < 0:
        return ("no real solution",discriminant)

# Task 964: Write a python function to check whether the length of the word is even or not.
def word_len(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%2==0: 
            return True  
        else:
          return False

# Task 965: Write a function to convert camel case string to snake case string.
def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

# Task 966: Write a function to remove an empty tuple from a list of tuples.
def remove_empty(tuple1): #L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
   tuple1 = [t for t in tuple1 if t]
   return tuple1

# Task 967: Write a python function to accept the strings which contains all vowels.
def check(string): 
  if len(set(string).intersection("AEIOUaeiou"))>=5: 
    return ('accepted') 
  else: 
    return ("not accepted")

# Task 968: Write a python function to find maximum possible value for the given periodic function.
def floor_Max(A,B,N):
    x = min(B - 1,N)
    return (A*x) // B

# Task 969: Write a function to join the tuples if they have similar initial elements.
def join_tuples(test_list):
  res = []
  for sub in test_list:
    if res and res[-1][0] == sub[0]:
      res[-1].extend(sub[1:])
    else:
      res.append([ele for ele in sub])
  res = list(map(tuple, res))
  return (res)

# Task 970: Write a function to find minimum of two numbers.
def min_of_two( x, y ):
    if x < y:
        return x
    return y

# Task 971: Write a function to find the maximum number of segments of lengths a, b and c that can be formed from n.
def maximum_segments(n, a, b, c) : 
	dp = [-1] * (n + 10) 
	dp[0] = 0
	for i in range(0, n) : 
		if (dp[i] != -1) : 
			if(i + a <= n ): 
				dp[i + a] = max(dp[i] + 1, 
							dp[i + a]) 
			if(i + b <= n ): 
				dp[i + b] = max(dp[i] + 1, 
							dp[i + b]) 
			if(i + c <= n ): 
				dp[i + c] = max(dp[i] + 1, 
							dp[i + c]) 
	return dp[n]

# Task 972: Write a function to concatenate the given two tuples to a nested tuple.
def concatenate_nested(test_tup1, test_tup2):
  res = test_tup1 + test_tup2
  return (res)

# Task 973: Write a python function to left rotate the string.
def left_rotate(s,d):
    tmp = s[d : ] + s[0 : d]
    return tmp

# Task 974: Write a function to find the minimum total path sum in the given triangle.
def min_sum_path(A): 
	memo = [None] * len(A) 
	n = len(A) - 1
	for i in range(len(A[n])): 
		memo[i] = A[n][i] 
	for i in range(len(A) - 2, -1,-1): 
		for j in range( len(A[i])): 
			memo[j] = A[i][j] + min(memo[j], 
									memo[j + 1]) 
	return memo[0]
