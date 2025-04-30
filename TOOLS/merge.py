import os
from pathlib import Path

def merge_txt_files(output_file="output.txt"):
    txt_files = sorted(Path('.').glob("*.txt"))
    with open(output_file, 'wb') as outfile:
        for file in txt_files:
            if file.name == output_file:
                continue  # Skip the output file if it already exists
            with open(file, 'rb') as infile:
                content = infile.read()
                outfile.write(content)
    print(f"Merged {len(txt_files)} into {output_file}")

if __name__ == "__main__":
    merge_txt_files()
