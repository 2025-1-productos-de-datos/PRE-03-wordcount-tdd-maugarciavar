import os


def read_all_lines(input_folder):
    lines = []
    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith(".txt"):
                with open(os.path.join(root, filename), "r", encoding="utf-8") as f:
                    lines.extend(f.readlines())
    return lines