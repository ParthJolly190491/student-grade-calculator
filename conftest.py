# conftest.py — pytest configuration for student-grade-calculator
# Ensures the repo root is on sys.path so grades_6_12 can be imported.

import sys
from pathlib import Path

# Add the repo root (parent of tests/) to sys.path
repo_root = Path(__file__).parent.resolve()
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))
