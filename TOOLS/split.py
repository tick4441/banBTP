import os

def split_large_txt(file_path, chunk_size_kb=300):
    chunk_size = chunk_size_kb * 1024  # Convert KB to bytes
    base_name = os.path.basename(file_path)
    base_name_no_ext = os.path.splitext(base_name)[0]
    
    with open(file_path, 'r', encoding='utf-8') as infile:
        part_num = 1
        out_file = open(f"{base_name_no_ext}_part{part_num}.txt", 'w', encoding='utf-8')
        current_size = 0

        for line in infile:
            line_size = len(line.encode('utf-8'))
            if current_size + line_size > chunk_size:
                out_file.close()
                part_num += 1
                out_file = open(f"{base_name_no_ext}_part{part_num}.txt", 'w', encoding='utf-8')
                current_size = 0

            out_file.write(line)
            current_size += line_size

        out_file.close()
    print(f"Split complete: {part_num} file(s) created.")

# Example usage
split_large_txt("000.txt")
