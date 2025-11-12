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
    raw_code = r'''def check_Validity(a,b,c):  \r\n    if (a + b <= c) or (a + c <= b) or (b + c <= a) : \r\n        return False\r\n    else: \r\n        return True   '''

    formatted_code = format_escaped_code(raw_code)
    open("./bug_portfolio/Traingle_valid_correct.py", "w").write(formatted_code)

