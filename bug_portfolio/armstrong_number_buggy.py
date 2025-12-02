def armstrong_number(number):
 sum = 0
 times = 0  
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 100  # Changed from 10 to 100 to correctly reduce the number of digits  2
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:  
    return True
 else:
    return False