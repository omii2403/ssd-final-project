import json

import re

def format_escaped_code(raw_code: str) -> str:
    """
    Converts escaped \\r\\n and \\t into real formatted Python code
    and normalizes multiple blank lines.
    """
    # Replace escaped sequences
    formatted = (
        raw_code.replace("\\r", "")
                .replace("\\n", "\n")
                .replace("\\t", "\t")
    )

    # Strip edges
    formatted = formatted.strip()

    # Collapse multiple blank lines into a single blank line
    formatted = re.sub(r"\n\s*\n+", "\n\n", formatted)

    return formatted


def extract_and_format(input_path, output_path, start_line=450, end_line=850):
    """
    Read mbpp.jsonl, extract code from specified lines,
    format them, and store all into a single output file.
    """
    formatted_blocks = []

    with open(input_path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            if line_number < start_line:
                continue
            if line_number > end_line:
                break

            try:
                data = json.loads(line)
                raw_code = data.get("code", "")
                description = data.get("text", "")
                formatted_code = format_escaped_code(raw_code)
                formatted_blocks.append(f"# ---- Description from line {line_number} ----\n# {description}\n")
                formatted_blocks.append(f"# ---- Function from line {line_number} ----\n{formatted_code}\n")
            except json.JSONDecodeError:
                print(f"Skipping malformed JSON at line {line_number}")
                continue

    # Write to output file
    with open(output_path, "w", encoding="utf-8") as out:
        out.write("\n\n".join(formatted_blocks))


if __name__ == "__main__":
    extract_and_format(
        input_path="mbpp.jsonl",
        output_path="formatted_mbpp_450_850.py",
        start_line=450,
        end_line=850
    )

    print("Done. Output saved to formatted_mbpp_450_850.py")
