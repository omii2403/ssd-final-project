# Task 974: Buggy version (off-by-one DP transition)

def min_sum_path(A):
    memo = [None] * len(A)
    n = len(A) - 1

    # Initialize bottom row
    for i in range(len(A[n])):
        memo[i] = A[n][i]

    # BUG HERE ↓ uses memo[j - 1] instead of memo[j + 1]
    for i in range(len(A) - 2, -1, -1):
        for j in range(len(A[i])):
            if j == 0:
                memo[j] = A[i][j] + memo[j]  # avoid j-1 at index 0
            else:
                memo[j] = A[i][j] + min(memo[j], memo[j - 1])

    return memo[0]
