def format_escaped_code(raw_code):
    """
    Takes a string of code with escaped \\r\\n and returns properly formatted Python code.
    """
    # Replace escaped line breaks, carriage returns, and tabs with real characters
    formatted = raw_code.replace("\\r", "").replace("\\n", "\n").replace("\\t", "\t")

    # Optional: strip leading/trailing whitespace
    formatted = formatted.strip()

    return formatted

if __name__ == "__main__":
    raw_code = r'''def get_maxgold(gold, m, n): \r\n    goldTable = [[0 for i in range(n)] \r\n                        for j in range(m)]   \r\n    for col in range(n-1, -1, -1): \r\n        for row in range(m):  \r\n            if (col == n-1): \r\n                right = 0\r\n            else: \r\n                right = goldTable[row][col+1] \r\n            if (row == 0 or col == n-1): \r\n                right_up = 0\r\n            else: \r\n                right_up = goldTable[row-1][col+1] \r\n            if (row == m-1 or col == n-1): \r\n                right_down = 0\r\n            else: \r\n                right_down = goldTable[row+1][col+1] \r\n            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down) \r\n    res = goldTable[0][0] \r\n    for i in range(1, m): \r\n        res = max(res, goldTable[i][0])  \r\n    return res '''

    formatted_code = format_escaped_code(raw_code)
    open("./bug_portfolio/get_max_gold_correct.py", "w").write(formatted_code)

