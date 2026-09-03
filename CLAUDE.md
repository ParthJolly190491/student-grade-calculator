# CLAUDE.md — Student Grade Calculator

## Project Overview
A Python library for calculating student grades, GPA,
and academic performance summaries.
Used by a fictional online learning platform.

## Coding Standards
- Use Python 3.10+
- Follow PEP 8 style guidelines
- snake_case for all names
- Docstrings on every function
- Type hints on all parameters and return values
- f-strings for all string formatting
- Raise ValueError with a clear message for invalid inputs
- No global variables

## Testing Standards
- Use pytest for all tests
- Test file: tests/test_grades.py
- Run with: pytest tests/ -v
- Every function must have:
    - At least one happy path test
    - At least one edge case test
    - At least one error test using pytest.raises()

## CI/CD Rules (enforced by GitHub Actions)
- All PRs must pass automated Claude Code review before merge
- Claude Code will BLOCK merge if it finds:
    - Missing type hints on any function
    - Missing docstring on any function
    - No tests for a new function
    - A function longer than 20 lines
- Claude Code will WARN (but not block) if it finds:
    - Magic numbers without named constants
    - More than 3 parameters on a function
    - Missing edge case test

## Project Structure
```
student_grade_calculator/
├── CLAUDE.md
├── grades.py               ← Core grading logic
├── tests/
│   └── test_grades.py      ← pytest test suite
└── .github/
    └── workflows/
        └── claude_review.yml  ← GitHub Actions CI workflow
```

## Off-Limits
- Do NOT modify CLAUDE.md
- Do NOT modify claude_review.yml without team approval
