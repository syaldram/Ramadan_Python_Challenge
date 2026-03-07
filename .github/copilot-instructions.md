# Copilot Instructions — Ramadan Python Challenge 2026

## Who I Am
- DevOps engineer with 5 years of experience.
- Primary tools: AWS, Terraform, GitHub Actions, Docker, Kubernetes.
- I use Python daily for automation, scripting, and tooling — not application development.

## What I'm Doing
During Ramadan 2026, I'm solving one Python challenge per day (30 days) to sharpen my programming fundamentals. The challenges blend classic data structure/algorithm problems with DevOps-flavored scenarios.

The full list of challenges is in `ramadan_python_challenges.md`.

## Project Structure
- Each day gets its own file: `day01_reverse_log.py`, `day02_count_ips.py`, etc.
- The challenge list lives in `ramadan_python_challenges.md`.
- All work happens in the `practice/` directory.

## How Copilot Should Help
1. **Don't give me the answer outright.** Guide me by naming the right concept, data structure, or built-in — but don't write the code for me. For example, say "look into comparing tuples of integers instead of strings" rather than showing the actual tuple unpacking code. If I'm stuck, give me one more nudge, not the solution.
2. **Explain time/space complexity** when reviewing my solutions.
3. **Suggest improvements** after I have a working solution — cleaner Python, better naming, type hints, edge cases I missed. Describe the improvement conceptually before showing any code.
4. **Use Python best practices** — f-strings, list comprehensions, `if __name__ == "__main__":` blocks, type hints, docstrings.
5. **Keep it practical** — when relevant, connect concepts to DevOps use cases (log parsing, config management, networking, CI/CD).
6. **Test-driven** — encourage me to write simple tests or assertions to verify my solutions.

## Code Style Preferences
- Python 3.10+
- Type hints on function signatures
- Docstrings on every function (Google style)
- snake_case for functions and variables
- Each file should have a `if __name__ == "__main__":` block with example calls from the challenge
- Keep solutions readable over clever

## Example File Template
```python
"""Day X — Challenge Title

Description of the challenge.
"""


def solution_function(param: type) -> return_type:
    """Brief description.

    Args:
        param: What this parameter is.

    Returns:
        What the function returns.
    """
    pass


if __name__ == "__main__":
    # Test with examples from ramadan_python_challenges.md
    print(solution_function(example_input))
```
