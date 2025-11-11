# ---- Function from line 450 ----
def extract_string(str, l):

    result = [e for e in str if len(e) == l] 

    return result


# ---- Function from line 451 ----
import re

def remove_whitespaces(text1):

  return (re.sub(r'\s+', '',text1))


# ---- Function from line 452 ----
def loss_amount(actual_cost,sale_amount): 

  if(sale_amount > actual_cost):

    amount = sale_amount - actual_cost

    return amount

  else:

    return None


# ---- Function from line 453 ----
import math 

def sumofFactors(n) : 

    if (n % 2 != 0) : 

        return 0

    res = 1

    for i in range(2, (int)(math.sqrt(n)) + 1) :    

        count = 0

        curr_sum = 1

        curr_term = 1

        while (n % i == 0) : 

            count= count + 1

            n = n // i 

            if (i == 2 and count == 1) : 

                curr_sum = 0

            curr_term = curr_term * i 

            curr_sum = curr_sum + curr_term 

        res = res * curr_sum  

    if (n >= 2) : 

        res = res * (1 + n) 

    return res


# ---- Function from line 454 ----
import re

def text_match_wordz(text):

        patterns = '\w*z.\w*'

        if re.search(patterns,  text):

                return 'Found a match!'

        else:

                return('Not matched!')


# ---- Function from line 455 ----
def check_monthnumb_number(monthnum2):

  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):

    return True

  else:

    return False


# ---- Function from line 456 ----
def reverse_string_list(stringlist):

    result = [x[::-1] for x in stringlist]

    return result


# ---- Function from line 457 ----
def Find_Min(lst): 

    minList = min((x) for x in lst) 

    return minList


# ---- Function from line 458 ----
def rectangle_area(l,b):

  area=l*b

  return area


# ---- Function from line 459 ----
import re

def remove_uppercase(str1):

  remove_upper = lambda text: re.sub('[A-Z]', '', text)

  result =  remove_upper(str1)

  return (result)


# ---- Function from line 460 ----
def Extract(lst): 

    return [item[0] for item in lst]


# ---- Function from line 461 ----
def upper_ctr(str):

    upper_ctr = 0

    for i in range(len(str)):

          if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1

          return upper_ctr


# ---- Function from line 462 ----
def combinations_list(list1):

    if len(list1) == 0:

        return [[]]

    result = []

    for el in combinations_list(list1[1:]):

        result += [el, el+[list1[0]]]

    return result


# ---- Function from line 463 ----
def max_subarray_product(arr):

	n = len(arr)

	max_ending_here = 1

	min_ending_here = 1

	max_so_far = 0

	flag = 0

	for i in range(0, n):

		if arr[i] > 0:

			max_ending_here = max_ending_here * arr[i]

			min_ending_here = min (min_ending_here * arr[i], 1)

			flag = 1

		elif arr[i] == 0:

			max_ending_here = 1

			min_ending_here = 1

		else:

			temp = max_ending_here

			max_ending_here = max (min_ending_here * arr[i], 1)

			min_ending_here = temp * arr[i]

		if (max_so_far < max_ending_here):

			max_so_far = max_ending_here

	if flag == 0 and max_so_far == 0:

		return 0

	return max_so_far


# ---- Function from line 464 ----
def check_value(dict, n):

    result = all(x == n for x in dict.values()) 

    return result


# ---- Function from line 465 ----
def drop_empty(dict1):

  dict1 = {key:value for (key, value) in dict1.items() if value is not None}

  return dict1


# ---- Function from line 466 ----
def find_peak_util(arr, low, high, n): 

	mid = low + (high - low)/2

	mid = int(mid) 

	if ((mid == 0 or arr[mid - 1] <= arr[mid]) and

		(mid == n - 1 or arr[mid + 1] <= arr[mid])): 

		return mid 

	elif (mid > 0 and arr[mid - 1] > arr[mid]): 

		return find_peak_util(arr, low, (mid - 1), n) 

	else: 

		return find_peak_util(arr, (mid + 1), high, n) 

def find_peak(arr, n): 

	return find_peak_util(arr, 0, n - 1, n)


# ---- Function from line 467 ----
def decimal_to_Octal(deciNum):

    octalNum = 0

    countval = 1;

    dNo = deciNum;

    while (deciNum!= 0):

        remainder= deciNum % 8;

        octalNum+= remainder*countval;

        countval= countval*10;

        deciNum //= 8; 

    return (octalNum)


# ---- Function from line 468 ----
def max_product(arr, n ): 

	mpis =[0] * (n) 

	for i in range(n): 

		mpis[i] = arr[i] 

	for i in range(1, n): 

		for j in range(i): 

			if (arr[i] > arr[j] and

					mpis[i] < (mpis[j] * arr[i])): 

						mpis[i] = mpis[j] * arr[i] 

	return max(mpis)


# ---- Function from line 469 ----
def max_profit(price, k):

    n = len(price)

    final_profit = [[None for x in range(n)] for y in range(k + 1)]

    for i in range(k + 1):

        for j in range(n):

            if i == 0 or j == 0:

                final_profit[i][j] = 0

            else:

                max_so_far = 0

                for x in range(j):

                    curr_price = price[j] - price[x] + final_profit[i-1][x]

                    if max_so_far < curr_price:

                        max_so_far = curr_price

                final_profit[i][j] = max(final_profit[i][j-1], max_so_far)

    return final_profit[k][n-1]


# ---- Function from line 470 ----
def add_pairwise(test_tup):

  res = tuple(i + j for i, j in zip(test_tup, test_tup[1:]))

  return (res)


# ---- Function from line 471 ----
def find_remainder(arr, lens, n): 

    mul = 1

    for i in range(lens):  

        mul = (mul * (arr[i] % n)) % n 

    return mul % n


# ---- Function from line 472 ----
def check_Consecutive(l): 

    return sorted(l) == list(range(min(l),max(l)+1))


# ---- Function from line 473 ----
def tuple_intersection(test_list1, test_list2):

  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])

  return (res)


# ---- Function from line 474 ----
def replace_char(str1,ch,newch):

 str2 = str1.replace(ch, newch)

 return str2


# ---- Function from line 475 ----
from collections import Counter

def sort_counter(dict1):

 x = Counter(dict1)

 sort_counter=x.most_common()

 return sort_counter


# ---- Function from line 476 ----
def big_sum(nums):

      sum= max(nums)+min(nums)

      return sum


# ---- Function from line 477 ----
def is_lower(string):

  return (string.lower())


# ---- Function from line 478 ----
import re

def remove_lowercase(str1):

 remove_lower = lambda text: re.sub('[a-z]', '', text)

 result =  remove_lower(str1)

 return result


# ---- Function from line 479 ----
def first_Digit(n) :  

    while n >= 10:  

        n = n / 10; 

    return int(n)


# ---- Function from line 480 ----
def get_max_occuring_char(str1):

  ASCII_SIZE = 256

  ctr = [0] * ASCII_SIZE

  max = -1

  ch = ''

  for i in str1:

    ctr[ord(i)]+=1;

  for i in str1:

    if max < ctr[ord(i)]:

      max = ctr[ord(i)]

      ch = i

  return ch


# ---- Function from line 481 ----
def is_subset_sum(set, n, sum):

	if (sum == 0):

		return True

	if (n == 0):

		return False

	if (set[n - 1] > sum):

		return is_subset_sum(set, n - 1, sum)

	return is_subset_sum(set, n-1, sum) or is_subset_sum(set, n-1, sum-set[n-1])


# ---- Function from line 482 ----
import re 

def match(text): 

		pattern = '[A-Z]+[a-z]+$'

		if re.search(pattern, text): 

				return('Yes') 

		else: 

				return('No')


# ---- Function from line 483 ----
def first_Factorial_Divisible_Number(x): 

    i = 1;

    fact = 1; 

    for i in range(1,x): 

        fact = fact * i 

        if (fact % x == 0): 

            break

    return i


# ---- Function from line 484 ----
def remove_matching_tuple(test_list1, test_list2):

  res = [sub for sub in test_list1 if sub not in test_list2]

  return (res)


# ---- Function from line 485 ----
def is_palindrome(n) : 

	divisor = 1

	while (n / divisor >= 10) : 

		divisor *= 10

	while (n != 0) : 

		leading = n // divisor 

		trailing = n % 10

		if (leading != trailing) : 

			return False

		n = (n % divisor) // 10

		divisor = divisor // 100

	return True

def largest_palindrome(A, n) : 

	A.sort() 

	for i in range(n - 1, -1, -1) : 

		if (is_palindrome(A[i])) : 

			return A[i] 

	return -1


# ---- Function from line 486 ----
def nCr(n, r): 

	if (r > n / 2): 

		r = n - r 

	answer = 1 

	for i in range(1, r + 1): 

		answer *= (n - r + i) 

		answer /= i 

	return answer 

def binomial_probability(n, k, p): 

	return (nCr(n, k) * pow(p, k) *	pow(1 - p, n - k))


# ---- Function from line 487 ----
def sort_tuple(tup): 

	lst = len(tup) 

	for i in range(0, lst): 

		for j in range(0, lst-i-1): 

			if (tup[j][-1] > tup[j + 1][-1]): 

				temp = tup[j] 

				tup[j]= tup[j + 1] 

				tup[j + 1]= temp 

	return tup


# ---- Function from line 488 ----
import math

def area_pentagon(a):

  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0

  return area


# ---- Function from line 489 ----
def frequency_Of_Largest(n,arr): 

    mn = arr[0] 

    freq = 1

    for i in range(1,n): 

        if (arr[i] >mn): 

            mn = arr[i] 

            freq = 1

        elif (arr[i] == mn): 

            freq += 1

    return freq


# ---- Function from line 490 ----
def extract_symmetric(test_list):

  temp = set(test_list) & {(b, a) for a, b in test_list}

  res = {(a, b) for a, b in temp if a < b}

  return (res)


# ---- Function from line 491 ----
import math

def sum_gp(a,n,r):

 total = (a * (1 - math.pow(r, n ))) / (1- r)

 return total


# ---- Function from line 492 ----
def binary_search(item_list,item):

	first = 0

	last = len(item_list)-1

	found = False

	while( first<=last and not found):

		mid = (first + last)//2

		if item_list[mid] == item :

			found = True

		else:

			if item < item_list[mid]:

				last = mid - 1

			else:

				first = mid + 1	

	return found


# ---- Function from line 493 ----
import math

def calculate_polygons(startx, starty, endx, endy, radius):

    sl = (2 * radius) * math.tan(math.pi / 6)

    p = sl * 0.5

    b = sl * math.cos(math.radians(30))

    w = b * 2

    h = 2 * sl   

    startx = startx - w

    starty = starty - h

    endx = endx + w

    endy = endy + h

    origx = startx

    origy = starty

    xoffset = b

    yoffset = 3 * p

    polygons = []

    row = 1

    counter = 0

    while starty < endy:

        if row % 2 == 0:

            startx = origx + xoffset

        else:

            startx = origx

        while startx < endx:

            p1x = startx

            p1y = starty + p

            p2x = startx

            p2y = starty + (3 * p)

            p3x = startx + b

            p3y = starty + h

            p4x = startx + w

            p4y = starty + (3 * p)

            p5x = startx + w

            p5y = starty + p

            p6x = startx + b

            p6y = starty

            poly = [

                (p1x, p1y),

                (p2x, p2y),

                (p3x, p3y),

                (p4x, p4y),

                (p5x, p5y),

                (p6x, p6y),

                (p1x, p1y)]

            polygons.append(poly)

            counter += 1

            startx += w

        starty += yoffset

        row += 1

    return polygons


# ---- Function from line 494 ----
def binary_to_integer(test_tup):

  res = int("".join(str(ele) for ele in test_tup), 2)

  return (str(res))


# ---- Function from line 495 ----
import re

def remove_lowercase(str1):

  remove_lower = lambda text: re.sub('[a-z]', '', text)

  result =  remove_lower(str1)

  return (result)


# ---- Function from line 496 ----
import heapq as hq

def heap_queue_smallest(nums,n):

  smallest_nums = hq.nsmallest(n, nums)

  return smallest_nums


# ---- Function from line 497 ----
import math

def surfacearea_cone(r,h):

  l = math.sqrt(r * r + h * h)

  SA = math.pi * r * (r + l)

  return SA


# ---- Function from line 498 ----
def gcd(x, y):

    gcd = 1

    if x % y == 0:

        return y

    for k in range(int(y / 2), 0, -1):

        if x % k == 0 and y % k == 0:

            gcd = k

            break  

    return gcd


# ---- Function from line 499 ----
def diameter_circle(r):

  diameter=2*r

  return diameter


# ---- Function from line 500 ----
def concatenate_elements(list):

  ans = ' '

  for i in list:

    ans = ans+ ' '+i

  return (ans)


# ---- Function from line 501 ----
def ngcd(x,y):

    i=1

    while(i<=x and i<=y):

        if(x%i==0 and y%i == 0):

            gcd=i;

        i+=1

    return gcd;

def num_comm_div(x,y):

  n = ngcd(x,y)

  result = 0

  z = int(n**0.5)

  i = 1

  while(i <= z):

    if(n % i == 0):

      result += 2 

      if(i == n/i):

        result-=1

    i+=1

  return result


# ---- Function from line 502 ----
def find(n,m):

  r = n%m

  return (r)


# ---- Function from line 503 ----
def add_consecutive_nums(nums):

    result = [b+a for a, b in zip(nums[:-1], nums[1:])]

    return result


# ---- Function from line 504 ----
def sum_Of_Series(n): 

    sum = 0

    for i in range(1,n + 1): 

        sum += i * i*i       

    return sum


# ---- Function from line 505 ----
def re_order(A):

    k = 0

    for i in A:

        if i:

            A[k] = i

            k = k + 1

    for i in range(k, len(A)):

        A[i] = 0

    return A


# ---- Function from line 506 ----
def permutation_coefficient(n, k): 

	P = [[0 for i in range(k + 1)] 

			for j in range(n + 1)] 

	for i in range(n + 1): 

		for j in range(min(i, k) + 1): 

			if (j == 0): 

				P[i][j] = 1

			else: 

				P[i][j] = P[i - 1][j] + ( 

						j * P[i - 1][j - 1]) 

			if (j < k): 

				P[i][j + 1] = 0

	return P[n][k]


# ---- Function from line 507 ----
def remove_words(list1, removewords):

    for word in list(list1):

        if word in removewords:

            list1.remove(word)

    return list1


# ---- Function from line 508 ----
def same_order(l1, l2):

    common_elements = set(l1) & set(l2)

    l1 = [e for e in l1 if e in common_elements]

    l2 = [e for e in l2 if e in common_elements]

    return l1 == l2


# ---- Function from line 509 ----
def average_Odd(n) : 

    if (n%2==0) : 

        return ("Invalid Input") 

        return -1 

    sm =0

    count =0

    while (n>=1) : 

        count=count+1

        sm = sm + n 

        n = n-2

    return sm//count


# ---- Function from line 510 ----
def no_of_subsequences(arr, k): 

	n = len(arr) 

	dp = [[0 for i in range(n + 1)] 

			for j in range(k + 1)] 

	for i in range(1, k + 1): 

		for j in range(1, n + 1): 

			dp[i][j] = dp[i][j - 1] 

			if arr[j - 1] <= i and arr[j - 1] > 0: 

				dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1

	return dp[k][n]


# ---- Function from line 511 ----
def find_Min_Sum(num): 

    sum = 0

    i = 2

    while(i * i <= num): 

        while(num % i == 0): 

            sum += i 

            num /= i 

        i += 1

    sum += num 

    return sum


# ---- Function from line 512 ----
def flatten(test_tuple): 

	for tup in test_tuple: 

		if isinstance(tup, tuple): 

			yield from flatten(tup) 

		else: 

			yield tup 

def count_element_freq(test_tuple):

  res = {}

  for ele in flatten(test_tuple):

    if ele not in res:

      res[ele] = 0

    res[ele] += 1

  return (res)


# ---- Function from line 513 ----
def add_str(test_tup, K):

  res = [ele for sub in test_tup for ele in (sub, K)]

  return (res)


# ---- Function from line 514 ----
def sum_elements(test_tup):

  res = sum(list(test_tup))

  return (res)


# ---- Function from line 515 ----
def modular_sum(arr, n, m): 

	if (n > m): 

		return True

	DP = [False for i in range(m)] 

	for i in range(n): 

		if (DP[0]): 

			return True

		temp = [False for i in range(m)] 

		for j in range(m): 

			if (DP[j] == True): 

				if (DP[(j + arr[i]) % m] == False): 

					temp[(j + arr[i]) % m] = True

		for j in range(m): 

			if (temp[j]): 

				DP[j] = True

		DP[arr[i] % m] = True

	return DP[0]


# ---- Function from line 516 ----
def radix_sort(nums):

    RADIX = 10

    placement = 1

    max_digit = max(nums)


    while placement < max_digit:

      buckets = [list() for _ in range( RADIX )]

      for i in nums:

        tmp = int((i / placement) % RADIX)

        buckets[tmp].append(i)

      a = 0

      for b in range( RADIX ):

        buck = buckets[b]

        for i in buck:

          nums[a] = i

          a += 1

      placement *= RADIX

    return nums


# ---- Function from line 517 ----
def largest_pos(list1): 

    max = list1[0] 

    for x in list1: 

        if x > max : 

             max = x  

    return max


# ---- Function from line 518 ----
import math

def sqrt_root(num):

 sqrt_root = math.pow(num, 0.5)

 return sqrt_root


# ---- Function from line 519 ----
import math

def volume_tetrahedron(num):

	volume = (num ** 3 / (6 * math.sqrt(2)))	

	return round(volume, 2)


# ---- Function from line 520 ----
def find_lcm(num1, num2): 

	if(num1>num2): 

		num = num1 

		den = num2 

	else: 

		num = num2 

		den = num1 

	rem = num % den 

	while (rem != 0): 

		num = den 

		den = rem 

		rem = num % den 

	gcd = den 

	lcm = int(int(num1 * num2)/int(gcd)) 

	return lcm 

def get_lcm(l):

  num1 = l[0]

  num2 = l[1]

  lcm = find_lcm(num1, num2)

  for i in range(2, len(l)):

    lcm = find_lcm(lcm, l[i])

  return lcm

# ---- Function from line 522 ----
def lbs(arr): 

	n = len(arr) 

	lis = [1 for i in range(n+1)] 

	for i in range(1 , n): 

		for j in range(0 , i): 

			if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)): 

				lis[i] = lis[j] + 1

	lds = [1 for i in range(n+1)] 

	for i in reversed(range(n-1)): 

		for j in reversed(range(i-1 ,n)): 

			if(arr[i] > arr[j] and lds[i] < lds[j] + 1): 

				lds[i] = lds[j] + 1

	maximum = lis[0] + lds[0] - 1

	for i in range(1 , n): 

		maximum = max((lis[i] + lds[i]-1), maximum) 

	return maximum


# ---- Function from line 523 ----
def check_string(str1):

    messg = [

    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',

    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',

    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',

    lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]

    result = [x for x in [i(str1) for i in messg] if x != True]

    if not result:

        result.append('Valid string.')

    return result


# ---- Function from line 524 ----
def max_sum_increasing_subsequence(arr, n): 

	max = 0

	msis = [0 for x in range(n)] 

	for i in range(n): 

		msis[i] = arr[i] 

	for i in range(1, n): 

		for j in range(i): 

			if (arr[i] > arr[j] and

				msis[i] < msis[j] + arr[i]): 

				msis[i] = msis[j] + arr[i] 

	for i in range(n): 

		if max < msis[i]: 

			max = msis[i] 

	return max


# ---- Function from line 525 ----
def parallel_lines(line1, line2):

  return line1[0]/line1[1] == line2[0]/line2[1]


# ---- Function from line 526 ----
def capitalize_first_last_letters(str1):

     str1 = result = str1.title()

     result =  ""

     for word in str1.split():

        result += word[:-1] + word[-1].upper() + " "

     return result[:-1]


# ---- Function from line 527 ----
def get_pairs_count(arr, n, sum):

    count = 0 

    for i in range(0, n):

        for j in range(i + 1, n):

            if arr[i] + arr[j] == sum:

                count += 1

    return count


# ---- Function from line 528 ----
def min_length(list1):

   min_length = min(len(x) for x in  list1 )  

   min_list = min((x) for x in   list1)

   return(min_length, min_list)


# ---- Function from line 529 ----
def jacobsthal_lucas(n): 

	dp=[0] * (n + 1) 

	dp[0] = 2

	dp[1] = 1

	for i in range(2, n+1): 

		dp[i] = dp[i - 1] + 2 * dp[i - 2]; 

	return dp[n]


# ---- Function from line 530 ----
from array import array

def negative_count(nums):

    n = len(nums)

    n1 = 0

    for x in nums:

        if x < 0:

            n1 += 1

        else:

          None

    return round(n1/n,2)


# ---- Function from line 531 ----
import sys 

def min_coins(coins, m, V): 

    if (V == 0): 

        return 0

    res = sys.maxsize 

    for i in range(0, m): 

        if (coins[i] <= V): 

            sub_res = min_coins(coins, m, V-coins[i]) 

            if (sub_res != sys.maxsize and sub_res + 1 < res): 

                res = sub_res + 1  

    return res


# ---- Function from line 532 ----
def check_permutation(str1, str2):

  n1=len(str1)

  n2=len(str2)

  if(n1!=n2):

    return False

  a=sorted(str1)

  str1=" ".join(a)

  b=sorted(str2)

  str2=" ".join(b)

  for i in range(0, n1, 1):

    if(str1[i] != str2[i]):

      return False

  return True


# ---- Function from line 533 ----
def remove_datatype(test_tuple, data_type):

  res = []

  for ele in test_tuple:

    if not isinstance(ele, data_type):

      res.append(ele)

  return (res)


# ---- Function from line 534 ----
import re

def search_literal(pattern,text):

 match = re.search(pattern, text)

 s = match.start()

 e = match.end()

 return (s, e)


# ---- Function from line 535 ----
def topbottom_surfacearea(r):

  toporbottomarea=3.1415*r*r

  return toporbottomarea


# ---- Function from line 536 ----
def nth_items(list,n):

 return list[::n]


# ---- Function from line 537 ----
def first_repeated_word(str1):

  temp = set()

  for word in str1.split():

    if word in temp:

      return word;

    else:

      temp.add(word)

  return 'None'


# ---- Function from line 538 ----
def string_list_to_tuple(str1):

    result = tuple(x for x in str1 if not x.isspace()) 

    return result


# ---- Function from line 539 ----
def basesnum_coresspondingnum(bases_num,index):

  result = list(map(pow, bases_num, index))

  return result


# ---- Function from line 540 ----
def find_Diff(arr,n): 

    arr.sort()  

    count = 0; max_count = 0; min_count = n 

    for i in range(0,(n-1)): 

        if arr[i] == arr[i + 1]: 

            count += 1

            continue

        else: 

            max_count = max(max_count,count) 

            min_count = min(min_count,count) 

            count = 0

    return max_count - min_count


# ---- Function from line 541 ----
import math 

def get_sum(n): 

	sum = 0

	i = 1

	while i <= (math.sqrt(n)): 

		if n%i == 0: 

			if n/i == i : 

				sum = sum + i 

			else: 

				sum = sum + i 

				sum = sum + (n / i ) 

		i = i + 1

	sum = sum - n 

	return sum

def check_abundant(n): 

	if (get_sum(n) > n): 

		return True

	else: 

		return False


# ---- Function from line 542 ----
import re

def fill_spaces(text):

  return (re.sub("[ ,.]", ":", text))


# ---- Function from line 543 ----
def count_digits(num1,num2):

    number=num1+num2

    count = 0

    while(number > 0):

        number = number // 10

        count = count + 1

    return count


# ---- Function from line 544 ----
def flatten_tuple(test_list):

  res = ' '.join([idx for tup in test_list for idx in tup])

  return (res)


# ---- Function from line 545 ----
def take_L_and_F_set_bits(n) : 

    n = n | n >> 1

    n = n | n >> 2

    n = n | n >> 4

    n = n | n >> 8

    n = n | n >> 16 

    return ((n + 1) >> 1) + 1      

def toggle_F_and_L_bits(n) :  

    if (n == 1) : 

        return 0 

    return n ^ take_L_and_F_set_bits(n)


# ---- Function from line 546 ----
def last_occurence_char(string,char):

 flag = -1

 for i in range(len(string)):

     if(string[i] == char):

         flag = i

 if(flag == -1):

    return None

 else:

    return flag + 1


# ---- Function from line 547 ----
def Total_Hamming_Distance(n):   

    i = 1

    sum = 0

    while (n // i > 0):  

        sum = sum + n // i  

        i = i * 2     

    return sum


# ---- Function from line 548 ----
def longest_increasing_subsequence(arr): 

	n = len(arr) 

	longest_increasing_subsequence = [1]*n 

	for i in range (1 , n): 

		for j in range(0 , i): 

			if arr[i] > arr[j] and longest_increasing_subsequence[i]< longest_increasing_subsequence[j] + 1 : 

				longest_increasing_subsequence[i] = longest_increasing_subsequence[j]+1

	maximum = 0

	for i in range(n): 

		maximum = max(maximum , longest_increasing_subsequence[i]) 

	return maximum


# ---- Function from line 549 ----
def odd_Num_Sum(n) : 

    j = 0

    sm = 0

    for i in range(1,n+1) : 

        j = (2*i-1) 

        sm = sm + (j*j*j*j*j)     

    return sm


# ---- Function from line 550 ----
def find_Max(arr,low,high): 

    if (high < low): 

        return arr[0] 

    if (high == low): 

        return arr[low] 

    mid = low + (high - low) // 2 

    if (mid < high and arr[mid + 1] < arr[mid]): 

        return arr[mid] 

    if (mid > low and arr[mid] < arr[mid - 1]): 

        return arr[mid - 1]  

    if (arr[low] > arr[mid]): 

        return find_Max(arr,low,mid - 1) 

    else: 

        return find_Max(arr,mid + 1,high)


# ---- Function from line 551 ----
def extract_column(list1, n):

   result = [i.pop(n) for i in list1]

   return result


# ---- Function from line 552 ----
def Seq_Linear(seq_nums):

  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]

  if len(set(seq_nums)) == 1: 

    return "Linear Sequence"

  else:

    return "Non Linear Sequence"


# ---- Function from line 553 ----
def tuple_to_float(test_tup):

  res = float('.'.join(str(ele) for ele in test_tup))

  return (res)


# ---- Function from line 554 ----
def Split(list): 

    od_li = [] 

    for i in list: 

        if (i % 2 != 0): 

            od_li.append(i)  

    return od_li


# ---- Function from line 555 ----
def difference(n) :  

    S = (n*(n + 1))//2;  

    res = S*(S-1);  

    return res;


# ---- Function from line 556 ----
def find_Odd_Pair(A,N) : 

    oddPair = 0

    for i in range(0,N) :  

        for j in range(i+1,N) :  

            if ((A[i] ^ A[j]) % 2 != 0):  

                oddPair+=1  

    return oddPair


# ---- Function from line 557 ----
def toggle_string(string):

 string1 = string.swapcase()

 return string1


# ---- Function from line 558 ----
def digit_distance_nums(n1, n2):

         return sum(map(int,str(abs(n1-n2))))


# ---- Function from line 559 ----
def max_sub_array_sum(a, size):

  max_so_far = 0

  max_ending_here = 0

  for i in range(0, size):

    max_ending_here = max_ending_here + a[i]

    if max_ending_here < 0:

      max_ending_here = 0

    elif (max_so_far < max_ending_here):

      max_so_far = max_ending_here

  return max_so_far


# ---- Function from line 560 ----
def union_elements(test_tup1, test_tup2):

  res = tuple(set(test_tup1 + test_tup2))

  return (res)


# ---- Function from line 561 ----
def assign_elements(test_list):

  res = dict()

  for key, val in test_list:

    res.setdefault(val, [])

    res.setdefault(key, []).append(val)

  return (res)


# ---- Function from line 562 ----
def Find_Max_Length(lst):  

    maxLength = max(len(x) for x in lst )

    return maxLength


# ---- Function from line 563 ----
import re

def extract_values(text):

 return (re.findall(r'"(.*?)"', text))


# ---- Function from line 564 ----
def count_Pairs(arr,n): 

    cnt = 0; 

    for i in range(n): 

        for j in range(i + 1,n): 

            if (arr[i] != arr[j]): 

                cnt += 1; 

    return cnt;


# ---- Function from line 565 ----
def split(word): 

    return [char for char in word]


# ---- Function from line 566 ----
def sum_digits(n):

  if n == 0:

    return 0

  else:

    return n % 10 + sum_digits(int(n / 10))


# ---- Function from line 567 ----
def issort_list(list1):

    result = all(list1[i] <= list1[i+1] for i in range(len(list1)-1))

    return result


# ---- Function from line 568 ----
def empty_list(length):

 empty_list = [{} for _ in range(length)]

 return empty_list


# ---- Function from line 569 ----
def sort_sublists(list1):

    result = list(map(sorted,list1)) 

    return result


# ---- Function from line 570 ----
def remove_words(list1, charlist):

    new_list = []

    for line in list1:

        new_words = ' '.join([word for word in line.split() if not any([phrase in word for phrase in charlist])])

        new_list.append(new_words)

    return new_list


# ---- Function from line 571 ----
def max_sum_pair_diff_lessthan_K(arr, N, K): 

	arr.sort() 

	dp = [0] * N 

	dp[0] = 0

	for i in range(1, N): 

		dp[i] = dp[i-1] 

		if (arr[i] - arr[i-1] < K): 

			if (i >= 2): 

				dp[i] = max(dp[i], dp[i-2] + arr[i] + arr[i-1]); 

			else: 

				dp[i] = max(dp[i], arr[i] + arr[i-1]); 

	return dp[N - 1]


# ---- Function from line 572 ----
def two_unique_nums(nums):

  return [i for i in nums if nums.count(i)==1]


# ---- Function from line 573 ----
def unique_product(list_data):

    temp = list(set(list_data))

    p = 1

    for i in temp:

        p *= i

    return p


# ---- Function from line 574 ----
def surfacearea_cylinder(r,h):

  surfacearea=((2*3.1415*r*r) +(2*3.1415*r*h))

  return surfacearea


# ---- Function from line 575 ----
def count_no (A,N,L,R): 

    count = 0

    for i in range (L,R + 1): 

        if (i % A != 0): 

            count += 1

        if (count == N): 

            break

    return (i)


# ---- Function from line 576 ----
def is_Sub_Array(A,B,n,m): 

    i = 0; j = 0; 

    while (i < n and j < m):  

        if (A[i] == B[j]): 

            i += 1; 

            j += 1; 

            if (j == m): 

                return True;  

        else: 

            i = i - j + 1; 

            j = 0;       

    return False;


# ---- Function from line 577 ----
def last_Digit_Factorial(n): 

    if (n == 0): return 1

    elif (n <= 2): return n  

    elif (n == 3): return 6

    elif (n == 4): return 4 

    else: 

      return 0


# ---- Function from line 578 ----
def interleave_lists(list1,list2,list3):

    result = [el for pair in zip(list1, list2, list3) for el in pair]

    return result


# ---- Function from line 579 ----
def find_dissimilar(test_tup1, test_tup2):

  res = tuple(set(test_tup1) ^ set(test_tup2))

  return (res)


# ---- Function from line 580 ----
def even_ele(test_tuple, even_fnc): 

	res = tuple() 

	for ele in test_tuple: 

		if isinstance(ele, tuple): 

			res += (even_ele(ele, even_fnc), ) 

		elif even_fnc(ele): 

			res += (ele, ) 

	return res 

def extract_even(test_tuple):

  res = even_ele(test_tuple, lambda x: x % 2 == 0)

  return (res)


# ---- Function from line 581 ----
def surface_Area(b,s): 

    return 2 * b * s + pow(b,2)


# ---- Function from line 582 ----
def my_dict(dict1):

  if bool(dict1):

     return False

  else:

     return True


# ---- Function from line 583 ----
def catalan_number(num):

    if num <=1:

         return 1   

    res_num = 0

    for i in range(num):

        res_num += catalan_number(i) * catalan_number(num-i-1)

    return res_num


# ---- Function from line 584 ----
import re

def find_adverbs(text):

  for m in re.finditer(r"\w+ly", text):

    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))


# ---- Function from line 585 ----
import heapq

def expensive_items(items,n):

  expensive_items = heapq.nlargest(n, items, key=lambda s: s['price'])

  return expensive_items


# ---- Function from line 586 ----
def split_Arr(a,n,k):  

   b = a[:k] 

   return (a[k::]+b[::])


# ---- Function from line 587 ----
def list_tuple(listx):

  tuplex = tuple(listx)

  return tuplex


# ---- Function from line 588 ----
def big_diff(nums):

     diff= max(nums)-min(nums)

     return diff


# ---- Function from line 589 ----
def perfect_squares(a, b):

    lists=[]

    for i in range (a,b+1):

        j = 1;

        while j*j <= i:

            if j*j == i:

                 lists.append(i)  

            j = j+1

        i = i+1

    return lists


# ---- Function from line 590 ----
import cmath

def polar_rect(x,y):

 cn = complex(x,y)

 cn=cmath.polar(cn)

 cn1 = cmath.rect(2, cmath.pi)

 return (cn,cn1)


# ---- Function from line 591 ----
def swap_List(newList): 

    size = len(newList) 

    temp = newList[0] 

    newList[0] = newList[size - 1] 

    newList[size - 1] = temp  

    return newList


# ---- Function from line 592 ----
def binomial_Coeff(n,k): 

    C = [0] * (k + 1); 

    C[0] = 1; # nC0 is 1 

    for i in range(1,n + 1):  

        for j in range(min(i, k),0,-1): 

            C[j] = C[j] + C[j - 1]; 

    return C[k]; 

def sum_Of_product(n): 

    return binomial_Coeff(2 * n,n - 1);


# ---- Function from line 593 ----
import re

def removezero_ip(ip):

 string = re.sub('\.[0]*', '.', ip)

 return string


# ---- Function from line 594 ----
def diff_even_odd(list1):

    first_even = next((el for el in list1 if el%2==0),-1)

    first_odd = next((el for el in list1 if el%2!=0),-1)

    return (first_even-first_odd)


# ---- Function from line 595 ----
def min_Swaps(str1,str2) : 

    count = 0

    for i in range(len(str1)) :  

        if str1[i] != str2[i] : 

            count += 1

    if count % 2 == 0 : 

        return (count // 2) 

    else : 

        return ("Not Possible")


# ---- Function from line 596 ----
import sys 

def tuple_size(tuple_list):

  return (sys.getsizeof(tuple_list))


# ---- Function from line 597 ----
def find_kth(arr1, arr2, m, n, k):

	sorted1 = [0] * (m + n)

	i = 0

	j = 0

	d = 0

	while (i < m and j < n):

		if (arr1[i] < arr2[j]):

			sorted1[d] = arr1[i]

			i += 1

		else:

			sorted1[d] = arr2[j]

			j += 1

		d += 1

	while (i < m):

		sorted1[d] = arr1[i]

		d += 1

		i += 1

	while (j < n):

		sorted1[d] = arr2[j]

		d += 1

		j += 1

	return sorted1[k - 1]


# ---- Function from line 598 ----
def armstrong_number(number):

 sum = 0

 times = 0

 temp = number

 while temp > 0:

           times = times + 1

           temp = temp // 10

 temp = number

 while temp > 0:

           reminder = temp % 10

           sum = sum + (reminder ** times)

           temp //= 10

 if number == sum:

           return True

 else:

           return False


# ---- Function from line 599 ----
def sum_average(number):

 total = 0

 for value in range(1, number + 1):

    total = total + value

 average = total / number

 return (total,average)


# ---- Function from line 600 ----
def is_Even(n) : 

    if (n^1 == n+1) :

        return True; 

    else :

        return False;


# ---- Function from line 601 ----
class Pair(object): 

	def __init__(self, a, b): 

		self.a = a 

		self.b = b 

def max_chain_length(arr, n): 

	max = 0

	mcl = [1 for i in range(n)] 

	for i in range(1, n): 

		for j in range(0, i): 

			if (arr[i].a > arr[j].b and

				mcl[i] < mcl[j] + 1): 

				mcl[i] = mcl[j] + 1

	for i in range(n): 

		if (max < mcl[i]): 

			max = mcl[i] 

	return max


# ---- Function from line 602 ----
def first_repeated_char(str1):

  for index,c in enumerate(str1):

    if str1[:index+1].count(c) > 1:

      return c 

  return "None"


# ---- Function from line 603 ----
def get_ludic(n):

	ludics = []

	for i in range(1, n + 1):

		ludics.append(i)

	index = 1

	while(index != len(ludics)):

		first_ludic = ludics[index]

		remove_index = index + first_ludic

		while(remove_index < len(ludics)):

			ludics.remove(ludics[remove_index])

			remove_index = remove_index + first_ludic - 1

		index += 1

	return ludics


# ---- Function from line 604 ----
def reverse_words(s):

        return ' '.join(reversed(s.split()))


# ---- Function from line 605 ----
def prime_num(num):

  if num >=1:

   for i in range(2, num//2):

     if (num % i) == 0:

                return False

     else:

                return True

  else:

          return False


# ---- Function from line 606 ----
import math

def radian_degree(degree):

 radian = degree*(math.pi/180)

 return radian


# ---- Function from line 607 ----
import re

pattern = 'fox'

text = 'The quick brown fox jumps over the lazy dog.'

def find_literals(text, pattern):

  match = re.search(pattern, text)

  s = match.start()

  e = match.end()

  return (match.re.pattern, s, e)


# ---- Function from line 608 ----
def bell_Number(n): 

    bell = [[0 for i in range(n+1)] for j in range(n+1)] 

    bell[0][0] = 1

    for i in range(1, n+1):

        bell[i][0] = bell[i-1][i-1]

        for j in range(1, i+1): 

            bell[i][j] = bell[i-1][j-1] + bell[i][j-1] 

    return bell[n][0]


# ---- Function from line 609 ----
def floor_Min(A,B,N):

    x = max(B - 1,N)

    return (A*x) // B


# ---- Function from line 610 ----
def remove_kth_element(list1, L):

    return  list1[:L-1] + list1[L:]


# ---- Function from line 611 ----
def max_of_nth(test_list, N):

  res = max([sub[N] for sub in test_list])

  return (res)


# ---- Function from line 612 ----
def merge(lst):  

    return [list(ele) for ele in list(zip(*lst))]


# ---- Function from line 613 ----
def maximum_value(test_list):

  res = [(key, max(lst)) for key, lst in test_list]

  return (res)


# ---- Function from line 614 ----
def cummulative_sum(test_list):

  res = sum(map(sum, test_list))

  return (res)


# ---- Function from line 615 ----
def average_tuple(nums):

    result = [sum(x) / len(x) for x in zip(*nums)]

    return result


# ---- Function from line 616 ----
def tuple_modulo(test_tup1, test_tup2):

  res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2)) 

  return (res)


# ---- Function from line 617 ----
def min_Jumps(a, b, d): 

    temp = a 

    a = min(a, b) 

    b = max(temp, b) 

    if (d >= b): 

        return (d + b - 1) / b 

    if (d == 0): 

        return 0

    if (d == a): 

        return 1

    else:

        return 2


# ---- Function from line 618 ----
def div_list(nums1,nums2):

  result = map(lambda x, y: x / y, nums1, nums2)

  return list(result)


# ---- Function from line 619 ----
def move_num(test_str):

  res = ''

  dig = ''

  for ele in test_str:

    if ele.isdigit():

      dig += ele

    else:

      res += ele

  res += dig

  return (res)


# ---- Function from line 620 ----
def largest_subset(a, n):

	dp = [0 for i in range(n)]

	dp[n - 1] = 1; 

	for i in range(n - 2, -1, -1):

		mxm = 0;

		for j in range(i + 1, n):

			if a[j] % a[i] == 0 or a[i] % a[j] == 0:

				mxm = max(mxm, dp[j])

		dp[i] = 1 + mxm

	return max(dp)


# ---- Function from line 621 ----
def increment_numerics(test_list, K):

  res = [str(int(ele) + K) if ele.isdigit() else ele for ele in test_list]

  return res


# ---- Function from line 622 ----
def get_median(arr1, arr2, n):

  i = 0

  j = 0

  m1 = -1

  m2 = -1

  count = 0

  while count < n + 1:

    count += 1

    if i == n:

      m1 = m2

      m2 = arr2[0]

      break

    elif j == n:

      m1 = m2

      m2 = arr1[0]

      break

    if arr1[i] <= arr2[j]:

      m1 = m2

      m2 = arr1[i]

      i += 1

    else:

      m1 = m2

      m2 = arr2[j]

      j += 1

  return (m1 + m2)/2


# ---- Function from line 623 ----
def nth_nums(nums,n):

 nth_nums = list(map(lambda x: x ** n, nums))

 return nth_nums


# ---- Function from line 624 ----
def is_upper(string):

  return (string.upper())


# ---- Function from line 625 ----
def swap_List(newList): 

    size = len(newList) 

    temp = newList[0] 

    newList[0] = newList[size - 1] 

    newList[size - 1] = temp   

    return newList


# ---- Function from line 626 ----
def triangle_area(r) :  

    if r < 0 : 

        return -1

    return r * r


# ---- Function from line 627 ----
def find_First_Missing(array,start,end): 

    if (start > end): 

        return end + 1

    if (start != array[start]): 

        return start; 

    mid = int((start + end) / 2) 

    if (array[mid] == mid): 

        return find_First_Missing(array,mid+1,end) 

    return find_First_Missing(array,start,mid)


# ---- Function from line 628 ----
MAX=1000;

def replace_spaces(string):

  string=string.strip()

  i=len(string)

  space_count=string.count(' ')

  new_length = i + space_count*2

  if new_length > MAX:

    return -1

  index = new_length-1

  string=list(string)

  for f in range(i-2, new_length-2):

    string.append('0')

  for j in range(i-1, 0, -1):

    if string[j] == ' ':

      string[index] = '0'

      string[index-1] = '2'

      string[index-2] = '%'

      index=index-3

    else:

      string[index] = string[j]

      index -= 1

  return ''.join(string)


# ---- Function from line 629 ----
def Split(list): 

    ev_li = [] 

    for i in list: 

        if (i % 2 == 0): 

            ev_li.append(i)  

    return ev_li


# ---- Function from line 630 ----
def adjac(ele, sub = []): 

  if not ele: 

     yield sub 

  else: 

     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 

                for idx in adjac(ele[1:], sub + [j])] 

def get_coordinates(test_tup):

  res = list(adjac(test_tup))

  return (res)


# ---- Function from line 631 ----
import re

text = 'Python Exercises'

def replace_spaces(text):

  text =text.replace (" ", "_")

  return (text)

  text =text.replace ("_", " ")

  return (text)


# ---- Function from line 632 ----
def move_zero(num_list):

    a = [0 for i in range(num_list.count(0))]

    x = [ i for i in num_list if i != 0]

    x.extend(a)

    return (x)


# ---- Function from line 633 ----
def pair_OR_Sum(arr,n) : 

    ans = 0 

    for i in range(0,n) :    

        for j in range(i + 1,n) :   

            ans = ans + (arr[i] ^ arr[j])          

    return ans


# ---- Function from line 634 ----
def even_Power_Sum(n): 

    sum = 0; 

    for i in range(1,n + 1): 

        j = 2*i; 

        sum = sum + (j*j*j*j); 

    return sum;


# ---- Function from line 635 ----
import heapq as hq

def heap_sort(iterable):

    h = []

    for value in iterable:

        hq.heappush(h, value)

    return [hq.heappop(h) for i in range(len(h))]


# ---- Function from line 636 ----
def Check_Solution(a,b,c): 

    if (a == c): 

        return ("Yes"); 

    else: 

        return ("No");


# ---- Function from line 637 ----
def noprofit_noloss(actual_cost,sale_amount): 

  if(sale_amount == actual_cost):

    return True

  else:

    return False


# ---- Function from line 638 ----
import math

def wind_chill(v,t):

 windchill = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)

 return int(round(windchill, 0))


# ---- Function from line 639 ----
def sample_nam(sample_names):

  sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))

  return len(''.join(sample_names))


# ---- Function from line 640 ----
import re

def remove_parenthesis(items):

 for item in items:

    return (re.sub(r" ?\([^)]+\)", "", item))


# ---- Function from line 641 ----
def is_nonagonal(n): 

	return int(n * (7 * n - 5) / 2)


# ---- Function from line 642 ----
def remove_similar_row(test_list):

  res = set(sorted([tuple(sorted(set(sub))) for sub in test_list]))

  return (res)


# ---- Function from line 643 ----
import re

def text_match_wordz_middle(text):

        patterns = '\Bz\B'

        if re.search(patterns,  text):

                return 'Found a match!'

        else:

                return('Not matched!')


# ---- Function from line 644 ----
def reverse_Array_Upto_K(input, k): 

  return (input[k-1::-1] + input[k:])


# ---- Function from line 645 ----
def get_product(val) : 

	res = 1

	for ele in val: 

		res *= ele 

	return res 

def find_k_product(test_list, K):

  res = get_product([sub[K] for sub in test_list])

  return (res)


# ---- Function from line 646 ----
def No_of_cubes(N,K):

    No = 0

    No = (N - K + 1)

    No = pow(No, 3)

    return No


# ---- Function from line 647 ----
import re

def split_upperstring(text):

 return (re.findall('[A-Z][^A-Z]*', text))


# ---- Function from line 648 ----
from itertools import zip_longest, chain, tee

def exchange_elements(lst):

    lst1, lst2 = tee(iter(lst), 2)

    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))


# ---- Function from line 649 ----
def sum_Range_list(nums, m, n):                                                                                                                                                                                                

    sum_range = 0                                                                                                                                                                                                         

    for i in range(m, n+1, 1):                                                                                                                                                                                        

        sum_range += nums[i]                                                                                                                                                                                                  

    return sum_range


# ---- Function from line 650 ----
def are_Equal(arr1,arr2,n,m):

    if (n != m):

        return False

    arr1.sort()

    arr2.sort()

    for i in range(0,n - 1):

        if (arr1[i] != arr2[i]):

            return False

    return True


# ---- Function from line 651 ----
def check_subset(test_tup1, test_tup2):

  res = set(test_tup2).issubset(test_tup1)

  return (res)


# ---- Function from line 652 ----
def matrix_to_list(test_list):

  temp = [ele for sub in test_list for ele in sub]

  res = list(zip(*temp))

  return (str(res))


# ---- Function from line 653 ----
from collections import defaultdict

def grouping_dictionary(l):

    d = defaultdict(list)

    for k, v in l:

        d[k].append(v)

    return d


# ---- Function from line 654 ----
def rectangle_perimeter(l,b):

  perimeter=2*(l+b)

  return perimeter


# ---- Function from line 655 ----
def fifth_Power_Sum(n) : 

    sm = 0 

    for i in range(1,n+1) : 

        sm = sm + (i*i*i*i*i) 

    return sm


# ---- Function from line 656 ----
def find_Min_Sum(a,b,n): 

    a.sort() 

    b.sort() 

    sum = 0  

    for i in range(n): 

        sum = sum + abs(a[i] - b[i]) 

    return sum


# ---- Function from line 657 ----
import math 

def first_Digit(n) : 

    fact = 1

    for i in range(2,n + 1) : 

        fact = fact * i 

        while (fact % 10 == 0) :  

            fact = int(fact / 10) 

    while (fact >= 10) : 

        fact = int(fact / 10) 

    return math.floor(fact)


# ---- Function from line 658 ----
def max_occurrences(list1):

    max_val = 0

    result = list1[0] 

    for i in list1:

        occu = list1.count(i)

        if occu > max_val:

            max_val = occu

            result = i 

    return result


# ---- Function from line 659 ----
def Repeat(x): 

    _size = len(x) 

    repeated = [] 

    for i in range(_size): 

        k = i + 1

        for j in range(k, _size): 

            if x[i] == x[j] and x[i] not in repeated: 

                repeated.append(x[i]) 

    return repeated


# ---- Function from line 660 ----
def find_Points(l1,r1,l2,r2): 

    x = min(l1,l2) if (l1 != l2) else -1

    y = max(r1,r2) if (r1 != r2) else -1

    return (x,y)


# ---- Function from line 661 ----
def max_sum_of_three_consecutive(arr, n): 

	sum = [0 for k in range(n)] 

	if n >= 1: 

		sum[0] = arr[0] 

	if n >= 2: 

		sum[1] = arr[0] + arr[1] 

	if n > 2: 

		sum[2] = max(sum[1], max(arr[1] + arr[2], arr[0] + arr[2])) 

	for i in range(3, n): 

		sum[i] = max(max(sum[i-1], sum[i-2] + arr[i]), arr[i] + arr[i-1] + sum[i-3]) 

	return sum[n-1]


# ---- Function from line 662 ----
def sorted_dict(dict1):

  sorted_dict = {x: sorted(y) for x, y in dict1.items()}

  return sorted_dict


# ---- Function from line 663 ----
import sys 

def find_max_val(n, x, y): 

	ans = -sys.maxsize 

	for k in range(n + 1): 

		if (k % x == y): 

			ans = max(ans, k) 

	return (ans if (ans >= 0 and

					ans <= n) else -1)


# ---- Function from line 664 ----
def average_Even(n) : 

    if (n% 2!= 0) : 

        return ("Invalid Input") 

        return -1  

    sm = 0

    count = 0

    while (n>= 2) : 

        count = count+1

        sm = sm+n 

        n = n-2

    return sm // count


# ---- Function from line 665 ----
def move_last(num_list):

    a = [num_list[0] for i in range(num_list.count(num_list[0]))]

    x = [ i for i in num_list if i != num_list[0]]

    x.extend(a)

    return (x)


# ---- Function from line 666 ----
def count_char(string,char):

 count = 0

 for i in range(len(string)):

    if(string[i] == char):

        count = count + 1

 return count


# ---- Function from line 667 ----
def Check_Vow(string, vowels): 

    final = [each for each in string if each in vowels] 

    return(len(final))


# ---- Function from line 668 ----
import re 

def replace(string, char): 

    pattern = char + '{2,}'

    string = re.sub(pattern, char, string) 

    return string


# ---- Function from line 669 ----
import re 

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 

			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 

			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 

			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

def check_IP(Ip): 

	if(re.search(regex, Ip)): 

		return ("Valid IP address") 

	else: 

		return ("Invalid IP address")


# ---- Function from line 670 ----
def decreasing_trend(nums):

    if (sorted(nums)== nums):

        return True

    else:

        return False


# ---- Function from line 671 ----
import math 

def get_Pos_Of_Right_most_Set_Bit(n): 

    return int(math.log2(n&-n)+1)   

def set_Right_most_Unset_Bit(n): 

    if (n == 0): 

        return 1

    if ((n & (n + 1)) == 0):     

        return n 

    pos = get_Pos_Of_Right_most_Set_Bit(~n)      

    return ((1 << (pos - 1)) | n)


# ---- Function from line 672 ----
def max_of_three(num1,num2,num3): 

    if (num1 >= num2) and (num1 >= num3):

       lnum = num1

    elif (num2 >= num1) and (num2 >= num3):

       lnum = num2

    else:

       lnum = num3

    return lnum


# ---- Function from line 673 ----
def convert(list): 

    s = [str(i) for i in list] 

    res = int("".join(s))  

    return (res)


# ---- Function from line 674 ----
from collections import OrderedDict

def remove_duplicate(string):

  result = ' '.join(OrderedDict((w,w) for w in string.split()).keys())

  return result


# ---- Function from line 675 ----
def sum_nums(x, y,m,n):

    sum_nums= x + y

    if sum_nums in range(m, n):

        return 20

    else:

        return sum_nums


# ---- Function from line 676 ----
import re

def remove_extra_char(text1):

  pattern = re.compile('[\W_]+')

  return (pattern.sub('', text1))


# ---- Function from line 677 ----
def validity_triangle(a,b,c):

 total = a + b + c

 if total == 180:

    return True

 else:

    return False


# ---- Function from line 678 ----
def remove_spaces(str1):

  str1 = str1.replace(' ','')

  return str1


# ---- Function from line 679 ----
def access_key(ditionary,key):

  return list(ditionary)[key]


# ---- Function from line 680 ----
def increasing_trend(nums):

    if (sorted(nums)== nums):

        return True

    else:

        return False


# ---- Function from line 681 ----
def smallest_Divisor(n): 

    if (n % 2 == 0): 

        return 2; 

    i = 3;  

    while (i*i <= n): 

        if (n % i == 0): 

            return i; 

        i += 2; 

    return n;


# ---- Function from line 682 ----
def mul_list(nums1,nums2):

  result = map(lambda x, y: x * y, nums1, nums2)

  return list(result)


# ---- Function from line 683 ----
def sum_Square(n) : 

    i = 1 

    while i*i <= n : 

        j = 1

        while (j*j <= n) : 

            if (i*i+j*j == n) : 

                return True

            j = j+1

        i = i+1     

    return False


# ---- Function from line 684 ----
def count_Char(str,x): 

    count = 0

    for i in range(len(str)):  

        if (str[i] == x) : 

            count += 1

    n = 10

    repititions = n // len(str)  

    count = count * repititions  

    l = n % len(str)  

    for i in range(l): 

        if (str[i] == x):  

            count += 1

    return count


# ---- Function from line 685 ----
def sum_Of_Primes(n): 

    prime = [True] * (n + 1)  

    p = 2

    while p * p <= n: 

        if prime[p] == True:  

            i = p * 2

            while i <= n: 

                prime[i] = False

                i += p 

        p += 1    

    sum = 0

    for i in range (2,n + 1): 

        if(prime[i]): 

            sum += i 

    return sum


# ---- Function from line 686 ----
from collections import defaultdict 

def freq_element(test_tup):

  res = defaultdict(int)

  for ele in test_tup:

    res[ele] += 1

  return (str(dict(res)))


# ---- Function from line 687 ----
def recur_gcd(a, b):

	low = min(a, b)

	high = max(a, b)

	if low == 0:

		return high

	elif low == 1:

		return 1

	else:

		return recur_gcd(low, high%low)


# ---- Function from line 688 ----
import cmath

def len_complex(a,b):

  cn=complex(a,b)

  length=abs(cn)

  return length


# ---- Function from line 689 ----
def min_jumps(arr, n):

	jumps = [0 for i in range(n)]

	if (n == 0) or (arr[0] == 0):

		return float('inf')

	jumps[0] = 0

	for i in range(1, n):

		jumps[i] = float('inf')

		for j in range(i):

			if (i <= j + arr[j]) and (jumps[j] != float('inf')):

				jumps[i] = min(jumps[i], jumps[j] + 1)

				break

	return jumps[n-1]


# ---- Function from line 690 ----
def mul_consecutive_nums(nums):

    result = [b*a for a, b in zip(nums[:-1], nums[1:])]

    return result


# ---- Function from line 691 ----
from itertools import groupby 

def group_element(test_list):

  res = dict()

  for key, val in groupby(sorted(test_list, key = lambda ele: ele[1]), key = lambda ele: ele[1]):

    res[key] = [ele[0] for ele in val] 

  return (res)


# ---- Function from line 692 ----
def last_Two_Digits(N): 

    if (N >= 10): 

        return

    fac = 1

    for i in range(1,N + 1): 

        fac = (fac * i) % 100

    return (fac)


# ---- Function from line 693 ----
import re

def remove_multiple_spaces(text1):

  return (re.sub(' +',' ',text1))


# ---- Function from line 694 ----
def extract_unique(test_dict):

  res = list(sorted({ele for val in test_dict.values() for ele in val}))

  return res


# ---- Function from line 695 ----
def check_greater(test_tup1, test_tup2):

  res = all(x < y for x, y in zip(test_tup1, test_tup2))

  return (res)


# ---- Function from line 696 ----
def zip_list(list1,list2):  

 result = list(map(list.__add__, list1, list2)) 

 return result


# ---- Function from line 697 ----
def count_even(array_nums):

   count_even = len(list(filter(lambda x: (x%2 == 0) , array_nums)))

   return count_even


# ---- Function from line 698 ----
def sort_dict_item(test_dict):

  res = {key: test_dict[key] for key in sorted(test_dict.keys(), key = lambda ele: ele[1] * ele[0])}

  return  (res)


# ---- Function from line 699 ----
def min_Swaps(str1,str2) : 

    count = 0

    for i in range(len(str1)) : 

        if str1[i] != str2[i] : 

            count += 1

    if count % 2 == 0 : 

        return (count // 2) 

    else : 

        return ("Not Possible")


# ---- Function from line 700 ----
def count_range_in_list(li, min, max):

	ctr = 0

	for x in li:

		if min <= x <= max:

			ctr += 1

	return ctr


# ---- Function from line 701 ----
def equilibrium_index(arr):

  total_sum = sum(arr)

  left_sum=0

  for i, num in enumerate(arr):

    total_sum -= num

    if left_sum == total_sum:

      return i

    left_sum += num

  return -1


# ---- Function from line 702 ----
def find_ind(key, i, n, 

			k, arr):

	ind = -1

	start = i + 1

	end = n - 1;

	while (start < end):

		mid = int(start +

				(end - start) / 2)

		if (arr[mid] - key <= k):

			ind = mid

			start = mid + 1

		else:

			end = mid

	return ind

def removals(arr, n, k):

	ans = n - 1

	arr.sort()

	for i in range(0, n):

		j = find_ind(arr[i], i, 

					n, k, arr)

		if (j != -1):

			ans = min(ans, n -

						(j - i + 1))

	return ans


# ---- Function from line 703 ----
def is_key_present(d,x):

  if x in d:

    return True

  else:

     return False


# ---- Function from line 704 ----
def harmonic_sum(n):

  if n < 2:

    return 1

  else:

    return 1 / n + (harmonic_sum(n - 1))


# ---- Function from line 705 ----
def sort_sublists(list1):

      list1.sort()  

      list1.sort(key=len)

      return  list1


# ---- Function from line 706 ----
def is_subset(arr1, m, arr2, n): 

	hashset = set() 

	for i in range(0, m): 

		hashset.add(arr1[i]) 

	for i in range(0, n): 

		if arr2[i] in hashset: 

			continue

		else: 

			return False

	return True


# ---- Function from line 707 ----
def count_Set_Bits(n) :  

    n += 1; 

    powerOf2 = 2;   

    cnt = n // 2;  

    while (powerOf2 <= n) : 

        totalPairs = n // powerOf2;  

        cnt += (totalPairs // 2) * powerOf2;  

        if (totalPairs & 1) : 

            cnt += (n % powerOf2) 

        else : 

            cnt += 0

        powerOf2 <<= 1;    

    return cnt;


# ---- Function from line 708 ----
def Convert(string): 

    li = list(string.split(" ")) 

    return li


# ---- Function from line 709 ----
from collections import defaultdict 

def get_unique(test_list):

  res = defaultdict(list)

  for sub in test_list:

    res[sub[1]].append(sub[0])

  res = dict(res)

  res_dict = dict()

  for key in res:

    res_dict[key] = len(list(set(res[key])))

  return (str(res_dict))


# ---- Function from line 710 ----
def front_and_rear(test_tup):

  res = (test_tup[0], test_tup[-1])

  return (res)


# ---- Function from line 711 ----
def product_Equal(n): 

    if n < 10: 

        return False

    prodOdd = 1; prodEven = 1

    while n > 0: 

        digit = n % 10

        prodOdd *= digit 

        n = n//10

        if n == 0: 

            break; 

        digit = n % 10

        prodEven *= digit 

        n = n//10

    if prodOdd == prodEven: 

        return True

    return False


# ---- Function from line 712 ----
import itertools

def remove_duplicate(list1):

 list.sort(list1)

 remove_duplicate = list(list1 for list1,_ in itertools.groupby(list1))

 return remove_duplicate


# ---- Function from line 713 ----
def check_valid(test_tup):

  res = not any(map(lambda ele: not ele, test_tup))

  return (res)


# ---- Function from line 714 ----
def count_Fac(n):  

    m = n 

    count = 0

    i = 2

    while((i * i) <= m): 

        total = 0

        while (n % i == 0): 

            n /= i 

            total += 1 

        temp = 0

        j = 1

        while((temp + j) <= total): 

            temp += j 

            count += 1

            j += 1 

        i += 1

    if (n != 1): 

        count += 1 

    return count


# ---- Function from line 715 ----
def str_to_tuple(test_str):

  res = tuple(map(int, test_str.split(', ')))

  return (res)


# ---- Function from line 716 ----
def rombus_perimeter(a):

  perimeter=4*a

  return perimeter


# ---- Function from line 717 ----
import math

import sys

def sd_calc(data):

    n = len(data)

    if n <= 1:

        return 0.0

    mean, sd = avg_calc(data), 0.0

    for el in data:

        sd += (float(el) - mean)**2

    sd = math.sqrt(sd / float(n-1))

    return sd

def avg_calc(ls):

    n, mean = len(ls), 0.0

    if n <= 1:

        return ls[0]

    for el in ls:

        mean = mean + float(el)

    mean = mean / float(n)

    return mean


# ---- Function from line 718 ----
def alternate_elements(list1):

    result=[]

    for item in list1[::2]:

        result.append(item)

    return result


# ---- Function from line 719 ----
import re

def text_match(text):

        patterns = 'ab*?'

        if re.search(patterns,  text):

                return 'Found a match!'

        else:

                return('Not matched!')


# ---- Function from line 720 ----
def add_dict_to_tuple(test_tup, test_dict):

  test_tup = list(test_tup)

  test_tup.append(test_dict)

  test_tup = tuple(test_tup)

  return (test_tup)


# ---- Function from line 721 ----
M = 100

def maxAverageOfPath(cost, N): 

	dp = [[0 for i in range(N + 1)] for j in range(N + 1)] 

	dp[0][0] = cost[0][0] 

	for i in range(1, N): 

		dp[i][0] = dp[i - 1][0] + cost[i][0] 

	for j in range(1, N): 

		dp[0][j] = dp[0][j - 1] + cost[0][j] 

	for i in range(1, N): 

		for j in range(1, N): 

			dp[i][j] = max(dp[i - 1][j], 

						dp[i][j - 1]) + cost[i][j] 

	return dp[N - 1][N - 1] / (2 * N - 1)


# ---- Function from line 722 ----
def filter_data(students,h,w):

    result = {k: s for k, s in students.items() if s[0] >=h and s[1] >=w}

    return result


# ---- Function from line 723 ----
from operator import eq

def count_same_pair(nums1, nums2):

    result = sum(map(eq, nums1, nums2))

    return result


# ---- Function from line 724 ----
def power_base_sum(base, power):

    return sum([int(i) for i in str(pow(base, power))])


# ---- Function from line 725 ----
import re

def extract_quotation(text1):

  return (re.findall(r'"(.*?)"', text1))


# ---- Function from line 726 ----
def multiply_elements(test_tup):

  res = tuple(i * j for i, j in zip(test_tup, test_tup[1:]))

  return (res)


# ---- Function from line 727 ----
import re 

def remove_char(S):

  result = re.sub('[\W_]+', '', S) 

  return result


# ---- Function from line 728 ----
def sum_list(lst1,lst2):

  res_list = [lst1[i] + lst2[i] for i in range(len(lst1))] 

  return res_list


# ---- Function from line 729 ----
def add_list(nums1,nums2):

  result = map(lambda x, y: x + y, nums1, nums2)

  return list(result)


# ---- Function from line 730 ----
from itertools import groupby

def consecutive_duplicates(nums):

    return [key for key, group in groupby(nums)]


# ---- Function from line 731 ----
import math

def lateralsurface_cone(r,h):

  l = math.sqrt(r * r + h * h)

  LSA = math.pi * r  * l

  return LSA


# ---- Function from line 732 ----
import re

def replace_specialchar(text):

 return (re.sub("[ ,.]", ":", text))


# ---- Function from line 733 ----
def find_first_occurrence(A, x):

    (left, right) = (0, len(A) - 1)

    result = -1

    while left <= right:

        mid = (left + right) // 2

        if x == A[mid]:

            result = mid

            right = mid - 1

        elif x < A[mid]:

            right = mid - 1

        else:

            left = mid + 1

    return result


# ---- Function from line 734 ----
def sum_Of_Subarray_Prod(arr,n):

    ans = 0

    res = 0

    i = n - 1

    while (i >= 0):

        incr = arr[i]*(1 + res)

        ans += incr

        res = incr

        i -= 1

    return (ans)


# ---- Function from line 735 ----
def set_middle_bits(n):  

    n |= n >> 1; 

    n |= n >> 2; 

    n |= n >> 4; 

    n |= n >> 8; 

    n |= n >> 16;  

    return (n >> 1) ^ 1

def toggle_middle_bits(n): 

    if (n == 1): 

        return 1

    return n ^ set_middle_bits(n)


# ---- Function from line 736 ----
import bisect

def left_insertion(a, x):

    i = bisect.bisect_left(a, x)

    return i


# ---- Function from line 737 ----
import re 

regex = '^[aeiouAEIOU][A-Za-z0-9_]*'

def check_str(string): 

	if(re.search(regex, string)): 

		return ("Valid") 

	else: 

		return ("Invalid")


# ---- Function from line 738 ----
def geometric_sum(n):

  if n < 0:

    return 0

  else:

    return 1 / (pow(2, n)) + geometric_sum(n - 1)


# ---- Function from line 739 ----
import math 

def find_Index(n): 

    x = math.sqrt(2 * math.pow(10,(n - 1))); 

    return round(x);


# ---- Function from line 740 ----
def tuple_to_dict(test_tup):

  res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 2))

  return (res)


# ---- Function from line 741 ----
def all_Characters_Same(s) :

    n = len(s)

    for i in range(1,n) :

        if s[i] != s[0] :

            return False

    return True


# ---- Function from line 742 ----
import math

def area_tetrahedron(side):

  area = math.sqrt(3)*(side*side)

  return area


# ---- Function from line 743 ----
def rotate_right(list1,m,n):

  result =  list1[-(m):]+list1[:-(n)]

  return result


# ---- Function from line 744 ----
def check_none(test_tup):

  res = any(map(lambda ele: ele is None, test_tup))

  return (res)


# ---- Function from line 745 ----
def divisible_by_digits(startnum, endnum):

    return [n for n in range(startnum, endnum+1) \

                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]


# ---- Function from line 746 ----
def sector_area(r,a):

    pi=22/7

    if a >= 360:

        return None

    sectorarea = (pi*r**2) * (a/360)

    return sectorarea


# ---- Function from line 747 ----
def lcs_of_three(X, Y, Z, m, n, o): 

	L = [[[0 for i in range(o+1)] for j in range(n+1)] 

		for k in range(m+1)] 

	for i in range(m+1): 

		for j in range(n+1): 

			for k in range(o+1): 

				if (i == 0 or j == 0 or k == 0): 

					L[i][j][k] = 0

				elif (X[i-1] == Y[j-1] and

					X[i-1] == Z[k-1]): 

					L[i][j][k] = L[i-1][j-1][k-1] + 1

				else: 

					L[i][j][k] = max(max(L[i-1][j][k], 

					L[i][j-1][k]), 

									L[i][j][k-1]) 

	return L[m][n][o]


# ---- Function from line 748 ----
import re

def capital_words_spaces(str1):

  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)


# ---- Function from line 749 ----
def sort_numeric_strings(nums_str):

    result = [int(x) for x in nums_str]

    result.sort()

    return result


# ---- Function from line 750 ----
def add_tuple(test_list, test_tup):

  test_list += test_tup

  return (test_list)


# ---- Function from line 751 ----
def check_min_heap(arr, i):

    if 2 * i + 2 > len(arr):

        return True

    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap(arr, 2 * i + 1)

    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 

                                      and check_min_heap(arr, 2 * i + 2))

    return left_child and right_child


# ---- Function from line 752 ----
def jacobsthal_num(n): 

	dp = [0] * (n + 1) 

	dp[0] = 0

	dp[1] = 1

	for i in range(2, n+1): 

		dp[i] = dp[i - 1] + 2 * dp[i - 2] 

	return dp[n]


# ---- Function from line 753 ----
def min_k(test_list, K):

  res = sorted(test_list, key = lambda x: x[1])[:K]

  return (res)


# ---- Function from line 754 ----
def extract_index_list(l1, l2, l3):

    result = []

    for m, n, o in zip(l1, l2, l3):

        if (m == n == o):

            result.append(m)

    return result


# ---- Function from line 755 ----
def second_smallest(numbers):

  if (len(numbers)<2):

    return

  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):

    return

  dup_items = set()

  uniq_items = []

  for x in numbers:

    if x not in dup_items:

      uniq_items.append(x)

      dup_items.add(x)

  uniq_items.sort()    

  return  uniq_items[1]


# ---- Function from line 756 ----
import re

def text_match_zero_one(text):

        patterns = 'ab?'

        if re.search(patterns,  text):

                return 'Found a match!'

        else:

                return('Not matched!')


# ---- Function from line 757 ----
def count_reverse_pairs(test_list):

  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 

	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 

  return str(res)


# ---- Function from line 758 ----
def unique_sublists(list1):

    result ={}

    for l in  list1: 

        result.setdefault(tuple(l), list()).append(1) 

    for a, b in result.items(): 

        result[a] = sum(b)

    return result


# ---- Function from line 759 ----
def is_decimal(num):

    import re

    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")

    result = dnumre.search(num)

    return bool(result)


# ---- Function from line 760 ----
def unique_Element(arr,n):

    s = set(arr)

    if (len(s) == 1):

        return ('YES')

    else:

        return ('NO')


# ---- Function from line 761 ----
def arc_length(d,a):

    pi=22/7

    if a >= 360:

        return None

    arclength = (pi*d) * (a/360)

    return arclength


# ---- Function from line 762 ----
def check_monthnumber_number(monthnum3):

  if(monthnum3==4 or monthnum3==6 or monthnum3==9 or monthnum3==11):

    return True

  else:

    return False


# ---- Function from line 763 ----
def find_Min_Diff(arr,n): 

    arr = sorted(arr) 

    diff = 10**20 

    for i in range(n-1): 

        if arr[i+1] - arr[i] < diff: 

            diff = arr[i+1] - arr[i]  

    return diff


# ---- Function from line 764 ----
def number_ctr(str):

      number_ctr= 0

      for i in range(len(str)):

          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     

      return  number_ctr


# ---- Function from line 765 ----
import math 

def is_polite(n): 

	n = n + 1

	return (int)(n+(math.log((n + math.log(n, 2)), 2)))


# ---- Function from line 766 ----
def pair_wise(l1):

    temp = []

    for i in range(len(l1) - 1):

        current_element, next_element = l1[i], l1[i + 1]

        x = (current_element, next_element)

        temp.append(x)

    return temp


# ---- Function from line 767 ----
def get_Pairs_Count(arr,n,sum):

    count = 0  

    for i in range(0,n):

        for j in range(i + 1,n):

            if arr[i] + arr[j] == sum:

                count += 1

    return count


# ---- Function from line 768 ----
def check_Odd_Parity(x): 

    parity = 0

    while (x != 0): 

        x = x & (x - 1) 

        parity += 1

    if (parity % 2 == 1): 

        return True

    else: 

        return False


# ---- Function from line 769 ----
def Diff(li1,li2):

    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))


# ---- Function from line 770 ----
def odd_Num_Sum(n) : 

    j = 0

    sm = 0

    for i in range(1,n + 1) : 

        j = (2*i-1) 

        sm = sm + (j*j*j*j)   

    return sm


# ---- Function from line 771 ----
from collections import deque

def check_expression(exp):

    if len(exp) & 1:

        return False

    stack = deque()

    for ch in exp:

        if ch == '(' or ch == '{' or ch == '[':

            stack.append(ch)

        if ch == ')' or ch == '}' or ch == ']':

            if not stack:

                return False

            top = stack.pop()

            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):

                return False

    return not stack


# ---- Function from line 772 ----
def remove_length(test_str, K):

  temp = test_str.split()

  res = [ele for ele in temp if len(ele) != K]

  res = ' '.join(res)

  return (res)


# ---- Function from line 773 ----
import re

def occurance_substring(text,pattern):

 for match in re.finditer(pattern, text):

    s = match.start()

    e = match.end()

    return (text[s:e], s, e)


# ---- Function from line 774 ----
import re 

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check_email(email): 

	if(re.search(regex,email)): 

		return ("Valid Email") 

	else: 

		return ("Invalid Email")


# ---- Function from line 775 ----
def odd_position(nums):

	return all(nums[i]%2==i%2 for i in range(len(nums)))


# ---- Function from line 776 ----
def count_vowels(test_str):

  res = 0

  vow_list = ['a', 'e', 'i', 'o', 'u']

  for idx in range(1, len(test_str) - 1):

    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):

      res += 1

  if test_str[0] not in vow_list and test_str[1] in vow_list:

    res += 1

  if test_str[-1] not in vow_list and test_str[-2] in vow_list:

    res += 1

  return (res)


# ---- Function from line 777 ----
def find_Sum(arr,n): 

    arr.sort() 

    sum = arr[0] 

    for i in range(0,n-1): 

        if (arr[i] != arr[i+1]): 

            sum = sum + arr[i+1]   

    return sum


# ---- Function from line 778 ----
from itertools import groupby

def pack_consecutive_duplicates(list1):

    return [list(group) for key, group in groupby(list1)]


# ---- Function from line 779 ----
def unique_sublists(list1):

    result ={}

    for l in list1: 

        result.setdefault(tuple(l), list()).append(1) 

    for a, b in result.items(): 

        result[a] = sum(b)

    return result


# ---- Function from line 780 ----
from itertools import combinations 

def find_combinations(test_list):

  res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(test_list, 2)]

  return (res)


# ---- Function from line 781 ----
import math 

def count_Divisors(n) : 

    count = 0

    for i in range(1, (int)(math.sqrt(n)) + 2) : 

        if (n % i == 0) : 

            if( n // i == i) : 

                count = count + 1

            else : 

                count = count + 2

    if (count % 2 == 0) : 

        return ("Even") 

    else : 

        return ("Odd")


# ---- Function from line 782 ----
def Odd_Length_Sum(arr):

    Sum = 0

    l = len(arr)

    for i in range(l):

        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])

    return Sum


# ---- Function from line 783 ----
def rgb_to_hsv(r, g, b):

    r, g, b = r/255.0, g/255.0, b/255.0

    mx = max(r, g, b)

    mn = min(r, g, b)

    df = mx-mn

    if mx == mn:

        h = 0

    elif mx == r:

        h = (60 * ((g-b)/df) + 360) % 360

    elif mx == g:

        h = (60 * ((b-r)/df) + 120) % 360

    elif mx == b:

        h = (60 * ((r-g)/df) + 240) % 360

    if mx == 0:

        s = 0

    else:

        s = (df/mx)*100

    v = mx*100

    return h, s, v


# ---- Function from line 784 ----
def mul_even_odd(list1):

    first_even = next((el for el in list1 if el%2==0),-1)

    first_odd = next((el for el in list1 if el%2!=0),-1)

    return (first_even*first_odd)


# ---- Function from line 785 ----
def tuple_str_int(test_str):

  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))

  return (res)


# ---- Function from line 786 ----
import bisect

def right_insertion(a, x):

    i = bisect.bisect_right(a, x)

    return i


# ---- Function from line 787 ----
import re

def text_match_three(text):

        patterns = 'ab{3}?'

        if re.search(patterns,  text):

                return 'Found a match!'

        else:

                return('Not matched!')


# ---- Function from line 788 ----
def new_tuple(test_list, test_str):

  res = tuple(test_list + [test_str])

  return (res)


# ---- Function from line 789 ----
from math import tan, pi

def perimeter_polygon(s,l):

  perimeter = s*l

  return perimeter


# ---- Function from line 790 ----
def even_position(nums):

	return all(nums[i]%2==i%2 for i in range(len(nums)))


# ---- Function from line 791 ----
def remove_nested(test_tup):

  res = tuple()

  for count, ele in enumerate(test_tup):

    if not isinstance(ele, tuple):

      res = res + (ele, )

  return (res)


# ---- Function from line 792 ----
def count_list(input_list): 

    return len(input_list)


# ---- Function from line 793 ----
def last(arr,x,n):

    low = 0

    high = n - 1

    res = -1  

    while (low <= high):

        mid = (low + high) // 2 

        if arr[mid] > x:

            high = mid - 1

        elif arr[mid] < x:

            low = mid + 1

        else:

            res = mid

            low = mid + 1

    return res


# ---- Function from line 794 ----
import re

def text_starta_endb(text):

        patterns = 'a.*?b$'

        if re.search(patterns,  text):

                return 'Found a match!'

        else:

                return('Not matched!')


# ---- Function from line 795 ----
import heapq

def cheap_items(items,n):

  cheap_items = heapq.nsmallest(n, items, key=lambda s: s['price'])

  return cheap_items


# ---- Function from line 796 ----
def return_sum(dict):

  sum = 0

  for i in dict.values():

    sum = sum + i

  return sum


# ---- Function from line 797 ----
def sum_Odd(n): 

    terms = (n + 1)//2

    sum1 = terms * terms 

    return sum1  

def sum_in_Range(l,r): 

    return sum_Odd(r) - sum_Odd(l - 1)


# ---- Function from line 798 ----
def _sum(arr):  

    sum=0

    for i in arr: 

        sum = sum + i      

    return(sum)


# ---- Function from line 799 ----
INT_BITS = 32

def left_Rotate(n,d):   

    return (n << d)|(n >> (INT_BITS - d))


# ---- Function from line 800 ----
import re

def remove_all_spaces(text):

 return (re.sub(r'\s+', '',text))


# ---- Function from line 801 ----
def test_three_equal(x,y,z):

  result= set([x,y,z])

  if len(result)==3:

    return 0

  else:

    return (4-len(result))


# ---- Function from line 802 ----
def count_Rotation(arr,n):   

    for i in range (1,n): 

        if (arr[i] < arr[i - 1]): 

            return i  

    return 0


# ---- Function from line 803 ----
def is_Perfect_Square(n) :

    i = 1

    while (i * i<= n):

        if ((n % i == 0) and (n / i == i)):

            return True     

        i = i + 1

    return False


# ---- Function from line 804 ----
def is_Product_Even(arr,n): 

    for i in range(0,n): 

        if ((arr[i] & 1) == 0): 

            return True

    return False


# ---- Function from line 805 ----
def max_sum_list(lists):

 return max(lists, key=sum)


# ---- Function from line 806 ----
def max_run_uppercase(test_str):

  cnt = 0

  res = 0

  for idx in range(0, len(test_str)):

    if test_str[idx].isupper():

      cnt += 1

    else:

      res = cnt

      cnt = 0

  if test_str[len(test_str) - 1].isupper():

    res = cnt

  return (res)


# ---- Function from line 807 ----
def first_odd(nums):

  first_odd = next((el for el in nums if el%2!=0),-1)

  return first_odd


# ---- Function from line 808 ----
def check_K(test_tup, K):

  res = False

  for ele in test_tup:

    if ele == K:

      res = True

      break

  return (res)


# ---- Function from line 809 ----
def check_smaller(test_tup1, test_tup2):

  res = all(x > y for x, y in zip(test_tup1, test_tup2))

  return (res)


# ---- Function from line 810 ----
from collections import Counter

def count_variable(a,b,c,d):

  c = Counter(p=a, q=b, r=c, s=d)

  return list(c.elements())


# ---- Function from line 811 ----
def check_identical(test_list1, test_list2):

  res = test_list1 == test_list2

  return (res)


# ---- Function from line 812 ----
import re

def road_rd(street):

  return (re.sub('Road$', 'Rd.', street))


# ---- Function from line 813 ----
def string_length(str1):

    count = 0

    for char in str1:

        count += 1

    return count


# ---- Function from line 814 ----
def rombus_area(p,q):

  area=(p*q)/2

  return area


# ---- Function from line 815 ----
def sort_by_dnf(arr, n):

  low=0

  mid=0

  high=n-1

  while mid <= high:

    if arr[mid] == 0:

      arr[low], arr[mid] = arr[mid], arr[low]

      low = low + 1

      mid = mid + 1

    elif arr[mid] == 1:

      mid = mid + 1

    else:

      arr[mid], arr[high] = arr[high], arr[mid]

      high = high - 1

  return arr


# ---- Function from line 816 ----
def clear_tuple(test_tup):

  temp = list(test_tup)

  temp.clear()

  test_tup = tuple(temp)

  return (test_tup)


# ---- Function from line 817 ----
def div_of_nums(nums,m,n):

 result = list(filter(lambda x: (x % m == 0 or x % n == 0), nums)) 

 return result


# ---- Function from line 818 ----
def lower_ctr(str):

      lower_ctr= 0

      for i in range(len(str)):

          if str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1     

      return  lower_ctr


# ---- Function from line 819 ----
def count_duplic(lists):

    element = []

    frequency = []

    if not lists:

        return element

    running_count = 1

    for i in range(len(lists)-1):

        if lists[i] == lists[i+1]:

            running_count += 1

        else:

            frequency.append(running_count)

            element.append(lists[i])

            running_count = 1

    frequency.append(running_count)

    element.append(lists[i+1])

    return element,frequency


# ---- Function from line 820 ----
def check_monthnum_number(monthnum1):

  if monthnum1 == 2:

    return True

  else:

    return False


# ---- Function from line 821 ----
import collections as ct

def merge_dictionaries(dict1,dict2):

    merged_dict = dict(ct.ChainMap({}, dict1, dict2))

    return merged_dict


# ---- Function from line 822 ----
import re

def pass_validity(p):

 x = True

 while x:  

    if (len(p)<6 or len(p)>12):

        break

    elif not re.search("[a-z]",p):

        break

    elif not re.search("[0-9]",p):

        break

    elif not re.search("[A-Z]",p):

        break

    elif not re.search("[$#@]",p):

        break

    elif re.search("\s",p):

        break

    else:

        return True

        x=False

        break


 if x:

    return False


# ---- Function from line 823 ----
import re 

def check_substring(string, sample) : 

  if (sample in string): 

      y = "\A" + sample 

      x = re.search(y, string) 

      if x : 

          return ("string starts with the given substring") 

      else : 

          return ("string doesnt start with the given substring") 

  else : 

      return ("entered string isnt a substring")


# ---- Function from line 824 ----
def remove_even(l):

    for i in l:

        if i % 2 == 0:

            l.remove(i)

    return l


# ---- Function from line 825 ----
def access_elements(nums, list_index):

    result = [nums[i] for i in list_index]

    return result


# ---- Function from line 826 ----
def check_Type_Of_Triangle(a,b,c): 

    sqa = pow(a,2) 

    sqb = pow(b,2) 

    sqc = pow(c,2) 

    if (sqa == sqa + sqb or sqb == sqa + sqc or sqc == sqa + sqb): 

        return ("Right-angled Triangle") 

    elif (sqa > sqc + sqb or sqb > sqa + sqc or sqc > sqa + sqb): 

        return ("Obtuse-angled Triangle") 

    else: 

        return ("Acute-angled Triangle")


# ---- Function from line 827 ----
def sum_column(list1, C):

    result = sum(row[C] for row in list1)

    return result


# ---- Function from line 828 ----
def count_alpha_dig_spl(string):

  alphabets=digits = special = 0

  for i in range(len(string)):

    if(string[i].isalpha()):

        alphabets = alphabets + 1

    elif(string[i].isdigit()):

        digits = digits + 1

    else:

        special = special + 1

  return (alphabets,digits,special)


# ---- Function from line 829 ----
from collections import Counter 


def second_frequent(input): 

	dict = Counter(input) 

	value = sorted(dict.values(), reverse=True)  

	second_large = value[1] 

	for (key, val) in dict.items(): 

		if val == second_large: 

			return (key)


# ---- Function from line 830 ----
import math

def round_up(a, digits):

    n = 10**-digits

    return round(math.ceil(a / n) * n, digits)


# ---- Function from line 831 ----
def count_Pairs(arr,n): 

    cnt = 0; 

    for i in range(n): 

        for j in range(i + 1,n): 

            if (arr[i] == arr[j]): 

                cnt += 1; 

    return cnt;


# ---- Function from line 832 ----
import re 

def extract_max(input): 

	numbers = re.findall('\d+',input) 

	numbers = map(int,numbers) 

	return max(numbers)


# ---- Function from line 833 ----
def get_key(dict): 

    list = [] 

    for key in dict.keys(): 

        list.append(key)           

    return list


# ---- Function from line 834 ----
def generate_matrix(n):

        if n<=0:

            return [] 

        matrix=[row[:] for row in [[0]*n]*n]        

        row_st=0

        row_ed=n-1        

        col_st=0

        col_ed=n-1

        current=1        

        while (True):

            if current>n*n:

                break

            for c in range (col_st, col_ed+1):

                matrix[row_st][c]=current

                current+=1

            row_st+=1

            for r in range (row_st, row_ed+1):

                matrix[r][col_ed]=current

                current+=1

            col_ed-=1

            for c in range (col_ed, col_st-1, -1):

                matrix[row_ed][c]=current

                current+=1

            row_ed-=1

            for r in range (row_ed, row_st-1, -1):

                matrix[r][col_st]=current

                current+=1

            col_st+=1

        return matrix


# ---- Function from line 835 ----
def slope(x1,y1,x2,y2): 

    return (float)(y2-y1)/(x2-x1)


# ---- Function from line 836 ----
from sys import maxsize 

def max_sub_array_sum(a,size): 

	max_so_far = -maxsize - 1

	max_ending_here = 0

	start = 0

	end = 0

	s = 0

	for i in range(0,size): 

		max_ending_here += a[i] 

		if max_so_far < max_ending_here: 

			max_so_far = max_ending_here 

			start = s 

			end = i 

		if max_ending_here < 0: 

			max_ending_here = 0

			s = i+1

	return (end - start + 1)


# ---- Function from line 837 ----
def cube_Sum(n): 

    sum = 0   

    for i in range(0,n) : 

        sum += (2*i+1)*(2*i+1)*(2*i+1) 

    return sum


# ---- Function from line 838 ----
def min_Swaps(s1,s2) :  

    c0 = 0; c1 = 0;  

    for i in range(len(s1)) :  

        if (s1[i] == '0' and s2[i] == '1') : 

            c0 += 1;    

        elif (s1[i] == '1' and s2[i] == '0') : 

            c1 += 1;  

    result = c0 // 2 + c1 // 2;  

    if (c0 % 2 == 0 and c1 % 2 == 0) : 

        return result;  

    elif ((c0 + c1) % 2 == 0) : 

        return result + 2;  

    else : 

        return -1;


# ---- Function from line 839 ----
def sort_tuple(tup): 

	n = len(tup) 

	for i in range(n): 

		for j in range(n-i-1): 

			if tup[j][0] > tup[j + 1][0]: 

				tup[j], tup[j + 1] = tup[j + 1], tup[j] 

	return tup


# ---- Function from line 840 ----
def Check_Solution(a,b,c):  

    if b == 0:  

        return ("Yes")  

    else: 

        return ("No")


# ---- Function from line 841 ----
def get_inv_count(arr, n): 

	inv_count = 0

	for i in range(n): 

		for j in range(i + 1, n): 

			if (arr[i] > arr[j]): 

				inv_count += 1

	return inv_count


# ---- Function from line 842 ----
def get_odd_occurence(arr, arr_size):

  for i in range(0, arr_size):

    count = 0

    for j in range(0, arr_size):

      if arr[i] == arr[j]:

        count += 1

    if (count % 2 != 0):

      return arr[i]

  return -1


# ---- Function from line 843 ----
import heapq

def nth_super_ugly_number(n, primes):

    uglies = [1]

    def gen(prime):

        for ugly in uglies:

            yield ugly * prime

    merged = heapq.merge(*map(gen, primes))

    while len(uglies) < n:

        ugly = next(merged)

        if ugly != uglies[-1]:

            uglies.append(ugly)

    return uglies[-1]


# ---- Function from line 844 ----
def get_Number(n, k): 

    arr = [0] * n; 

    i = 0; 

    odd = 1; 

    while (odd <= n):   

        arr[i] = odd; 

        i += 1; 

        odd += 2;

    even = 2; 

    while (even <= n): 

        arr[i] = even; 

        i += 1;

        even += 2; 

    return arr[k - 1];


# ---- Function from line 845 ----
import math 

def find_Digits(n): 

    if (n < 0): 

        return 0;

    if (n <= 1): 

        return 1; 

    x = ((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) /2.0)); 

    return math.floor(x) + 1;


# ---- Function from line 846 ----
def find_platform(arr, dep, n): 

    arr.sort() 

    dep.sort() 

    plat_needed = 1

    result = 1

    i = 1

    j = 0

    while (i < n and j < n): 

        if (arr[i] <= dep[j]):           

            plat_needed+= 1

            i+= 1

        elif (arr[i] > dep[j]):           

            plat_needed-= 1

            j+= 1

        if (plat_needed > result):  

            result = plat_needed           

    return result


# ---- Function from line 847 ----
def lcopy(xs):
  return xs[:]


# ---- Function from line 848 ----
def area_trapezium(base1,base2,height):

 area = 0.5 * (base1 + base2) * height

 return area


# ---- Function from line 849 ----
def Sum(N): 

    SumOfPrimeDivisors = [0]*(N + 1)   

    for i in range(2,N + 1) : 

        if (SumOfPrimeDivisors[i] == 0) : 

            for j in range(i,N + 1,i) : 

                SumOfPrimeDivisors[j] += i           

    return SumOfPrimeDivisors[N]


# ---- Function from line 850 ----
def is_triangleexists(a,b,c): 

    if(a != 0 and b != 0 and c != 0 and (a + b + c)== 180): 

        if((a + b)>= c or (b + c)>= a or (a + c)>= b): 

            return True 

        else:

            return False

    else:

        return False
