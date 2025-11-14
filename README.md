# The Testing Showdown: Humans vs. LLMs in Bug Detection

**TEAM 19 — SSD Final Project**  
Software Engineering Research Centre (SERC), IIIT Hyderabad

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![pytest](https://img.shields.io/badge/testing-pytest-green.svg)](https://pytest.org/)
[![hypothesis](https://img.shields.io/badge/testing-hypothesis-orange.svg)](https://hypothesis.readthedocs.io/)

---

## Project Overview

This project empirically compares **LLM-generated unit tests** versus **human-written property-based tests** for bug detection effectiveness. We curate a "Bug Portfolio" of 25-30 intentionally buggy Python functions from the MBPP (Most Basic Programming Problems) dataset and evaluate which testing strategy finds more bugs.

### Research Question
**Which testing strategy is more effective at finding subtle bugs—automated LLM-generated tests or human-crafted property-based tests?**

---

## Team Members

- Om Mehra - 2025201008
- Hardik Kothari - 2025201046
- Ankit Chavda - 2025201045
- M V Ramana Murthy - 2025204034
- P Chaitanya Pavan Kumar - 2025204023

Advisor: Abhishek Singh


---

## Project Objectives

1. **Bug Portfolio Creation:** Select functions from MBPP and create buggy versions with single, minimal, plausible bugs
2. **Dual Testing Strategy:**
   - **LLM Challenger:** Generate comprehensive example-based `pytest` suites using LLMs (DeepSeek/ChatGPT)
   - **Human Defender:** Write `hypothesis`-based property tests that verify invariants
3. **Comparative Analysis:** Run both test suites and analyze which approach detects more bugs

---

## Repository Structure

```
ssd-final-project/
├── bug_portfolio/              # Curated buggy & correct implementations
│   ├── *_buggy.py             # Intentionally buggy versions
│   ├── *_correct.py           # Original correct implementations
│   └── metadata.jsonl         # Function specs & bug descriptions
│
├── human_tests/               # Human-written hypothesis-based tests
│   └── test_*.py             # Property-based test files
│
├── llm_tests/
│   ├── generated_tests/      # LLM-generated pytest suites
│   │   └── test_*.py
│   └── prompts/              # Prompt templates for LLM test generation
│       └── *.txt
│
├── Report.ipynb              # Main analysis notebook (run this!)
├── mbpp.jsonl                # MBPP dataset subset
├── helper.py                 # Utility functions
├── humanvsllm.md             # Original project specification
│
├── results_summary.csv       # Per-function test results
├── final_scorecard.csv       # Aggregate metrics
│
├── TEAM_19_REPORT.pdf        # Phase 1 report
├── TEAM_19_PHASE2_REPORT.md  # Phase 2 report (this deliverable)
└── README.md                 # This file
```

---

## Quick Start

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/omii2403/ssd-final-project.git
   cd ssd-final-project
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas matplotlib pytest hypothesis tabulate
   ```

3. **Verify installation:**
   ```bash
   pytest --version
   python -c "import hypothesis; print(hypothesis.__version__)"
   ```

### Running the Analysis

**Option 1: Jupyter Notebook (Recommended)**
```bash
jupyter notebook Report.ipynb
# Run all cells to execute tests and generate results
```

**Option 2: VS Code**
```bash
# Open Report.ipynb in VS Code
# Click "Run All" in the notebook toolbar
```

**Option 3: Run Tests Manually**
```bash
# Run LLM tests for a specific function
pytest llm_tests/generated_tests/test_bell_Number.py -v

# Run human tests for a specific function
pytest human_tests/test_bell_Number.py -v

# Run all tests
pytest human_tests/ -v
pytest llm_tests/generated_tests/ -v
```

---

## Analysis Workflow

### Step 1: Load Bug Portfolio
The notebook loads function metadata from `bug_portfolio/metadata.jsonl`:
```python
import json
metadata = []
with open("bug_portfolio/metadata.jsonl", "r") as f:
    for line in f:
        if line.strip() and line.strip().endswith("}"):
            metadata.append(json.loads(line.strip()))

functions = [item["name"] for item in metadata]
```

### Step 2: Automated Test Execution
For each function, run both test suites:
```python
import subprocess

# Run LLM tests
result_llm = subprocess.run(
    ["pytest", "-q", f"llm_tests/generated_tests/test_{func}.py"],
    capture_output=True, text=True
)

# Run Human tests
result_human = subprocess.run(
    ["pytest", "-q", f"human_tests/test_{func}.py"],
    capture_output=True, text=True
)
```

### Step 3: Generate Comparative Metrics
```python
scorecard = {
    "Bugs found only by LLM tests": count_llm_only,
    "Bugs found only by Human properties": count_human_only,
    "Bugs found by both": count_both,
    "Bugs found by neither": count_neither
}
```

### Step 4: Visualization
Bar charts and tables show comparative effectiveness:
```python
plt.bar(scorecard.keys(), scorecard.values())
plt.title("Bug Detection Summary (LLM vs Human)")
plt.show()
```

---

## Bug Portfolio Examples

### Example 1: `set_Right_most_Unset_Bit`
**Specification:** Set the rightmost unset (0) bit to 1  
**Bug:** When `n = 0`, returns `0` instead of `1`  
**Type:** Edge case handling error

**Buggy Implementation:**
```python
def set_Right_most_Unset_Bit(n):
    if n == 0:
        return 0  # BUG: should return 1
    return n | (n + 1)
```

**Human Test (Hypothesis):**
```python
@given(st.integers(min_value=0, max_value=1000))
def test_rightmost_bit_property(n):
    result = set_Right_most_Unset_Bit(n)
    assert result > n or result == n + 1
```

---

### Example 2: `find_Max`
**Specification:** Find maximum in a rotated sorted array  
**Bug:** Incorrect comparison operator (`>=` instead of `>`)  
**Type:** Logic error

**Buggy Implementation:**
```python
def find_Max(arr, low, high):
    if high == low:
        return arr[low]
    mid = (low + high) // 2
    if arr[low] >= arr[mid]:  # BUG: should be >
        return find_Max(arr, low, mid)
    return find_Max(arr, mid + 1, high)
```

---

## Results

After completing the analysis in `Report.ipynb`, you'll find:

- **`results_summary.csv`** — Per-function breakdown (which method found each bug)
- **`final_scorecard.csv`** — Aggregate counts of detection effectiveness
- **Charts** — Visual comparison of LLM vs Human detection rates

### Sample Scorecard Output
| Metric | Count |
|--------|-------|
| Bugs found only by LLM tests | X |
| Bugs found only by Human properties | Y |
| Bugs found by both | Z |
| Bugs found by neither | W |

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.10+ |
| **Testing** | pytest, hypothesis |
| **Analysis** | pandas, matplotlib |
| **Notebook** | Jupyter / VS Code |
| **LLM** | DeepSeek, ChatGPT |
| **Dataset** | MBPP (Google Research) |

---

## Key Insights (Phase 2)

### LLM Test Strengths
- Excellent coverage of common input cases
- Fast generation of comprehensive example-based tests
- Good at catching bugs that violate explicit specifications

### Human Property Test Strengths
- Better at discovering edge cases (empty inputs, zero, boundaries)
- Generative approach finds unexpected failure modes
- Tests encode domain knowledge and invariants

### Complementary Nature
Some bugs are only found when **both approaches are combined**, suggesting a hybrid testing strategy may be optimal.

---

## Project Phases

### Phase 1: Bug Factory
- Selected 25-30 functions from MBPP dataset
- Created buggy versions with minimal, plausible bugs
- Documented bug descriptions in `metadata.jsonl`
- **Deliverable:** Phase 1 report (`TEAM_19_REPORT.pdf`)

### Phase 2: Testing Arena (Current)
- Generated LLM test suites using structured prompts
- Wrote human property-based tests with hypothesis
- Built automated evaluation pipeline in `Report.ipynb`
- **Deliverable:** Phase 2 report (`TEAM_19_PHASE2_REPORT.md`)

### Phase 3: Final Analysis
- Complete 25-30 function portfolio
- Run full evaluation and generate final metrics
- Write comprehensive analysis report
- **Deliverable:** Final project report with conclusions

---

## References

- **MBPP Dataset:** [Google Research GitHub](https://github.com/google-research/google-research/tree/master/mbpp)
- **pytest Documentation:** [pytest.org](https://pytest.org/)
- **Hypothesis Documentation:** [hypothesis.readthedocs.io](https://hypothesis.readthedocs.io/)
- **Project Specification:** See `humanvsllm.md`

---

## Links

- **Repository:** [https://github.com/omii2403/ssd-final-project](https://github.com/omii2403/ssd-final-project)
- **Phase 1 Report:** `TEAM_19_REPORT.pdf`
- **Phase 2 Report:** `TEAM_19_PHASE2_REPORT.md`
- **Analysis Notebook:** `Report.ipynb`

---

**Last Updated:** November 14, 2025  
**Status:** Phase 2 Complete (15/30 functions) — Expanding to 25-30 for Phase 3
