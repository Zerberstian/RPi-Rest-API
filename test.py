from pathlib import Path

file_path = Path(__file__).parent / "x-api_key.txt"

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()
print(f"\n Key:\n")
print(read_text_file(file_path))