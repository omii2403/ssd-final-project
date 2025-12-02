import json

input_path = "/Users/hardikkothari/ssd-final-project/sample.jsonl"
output_path = "/Users/hardikkothari/ssd-final-project/combined_mbpp_code.py"

with open(input_path, 'r', encoding='utf-8') as infile, \
     open(output_path, 'w', encoding='utf-8') as outfile:

    for line_num, line in enumerate(infile, start=1):
        try:
            data = json.loads(line)
        except:
            print(f"Skipping invalid JSON on line {line_num}")
            continue

        code = data.get("code", "").strip()
        task_id = data.get("task_id", "")
        description = data.get("text", "")

        if not code:
            continue

        outfile.write(f"\n# Task {task_id}: {description}\n")
        outfile.write(code)
        outfile.write("\n")
