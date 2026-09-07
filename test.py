from pathlib import Path

file_path = Path(__file__).parent / "x-api_key.txt"

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

x_api_key = read_text_file(file_path)
print(f"\nKey: {x_api_key}\n")
