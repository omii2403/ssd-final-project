def format_escaped_code(raw_code):
    """
    Takes a string of code with escaped \\r\\n and returns properly formatted Python code.
    """
    # Replace escaped line breaks and carriage returns with real newlines
    formatted = raw_code.replace("\\r", "").replace("\\n", "\n")

    # Optional: strip leading/trailing whitespace
    formatted = formatted.strip()

    return formatted

if __name__ == "__main__":
    raw_code = r'''import math \r\ndef get_Pos_Of_Right_most_Set_Bit(n): \r\n    return int(math.log2(n&-n)+1)   \r\ndef set_Right_most_Unset_Bit(n): \r\n    if (n == 0): \r\n        return 1\r\n    if ((n & (n + 1)) == 0):     \r\n        return n \r\n    pos = get_Pos_Of_Right_most_Set_Bit(~n)      \r\n    return ((1 << (pos - 1)) | n) '''

    formatted_code = format_escaped_code(raw_code)
    open("formatted_code.py", "w").write(formatted_code)