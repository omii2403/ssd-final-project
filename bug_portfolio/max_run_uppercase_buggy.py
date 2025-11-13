def max_run_uppercase(test_str):
    cnt = 0
    res = 0
    for idx in range(len(test_str)):
        if test_str[idx].isupper():
            cnt += 1
        else:
            if cnt > res:   
                res = cnt
            cnt = -1 # bug here, should be cnt = 0
    if cnt > res:            
        res = cnt
    return res