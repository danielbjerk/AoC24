from pathlib import Path

for i in range(1, 24 + 1):
    top = Path(f"day{i:02}")
    top.mkdir()
    (top / "input.txt").touch()
    (top / "solution.py").touch()
