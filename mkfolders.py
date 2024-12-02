from pathlib import Path

for i in range(1, 24 + 1):
    top = Path(f"day{i:02}")
    top.mkdir()
    (top / "input1.txt").touch()
    (top / "solution1.py").touch()
    (top / "input2.txt").touch()
    (top / "solution2.py").touch()
