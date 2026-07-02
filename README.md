# LeetCode Solutions

Python solutions to LeetCode problems, solved as part of my software development training.

Each problem has its own folder containing:
- `solution.py` — the solution with type hints and docstrings
- `test_solution.py` — pytest tests covering examples and edge cases

## Problems

| # | Problem | Difficulty | Folder |
|---|---------|-----------|--------|
| 1 | Two Sum | Easy | [`two-sum/`](./two-sum) |

## Running tests

```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install pytest
cd <problem-folder>
pytest test_solution.py -v
```