def read_file(filename):
    lines = []
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped:  # skip empty lines
                count += 1
                print(f"Line {count}: {stripped}")
                lines.append(stripped)
    return lines