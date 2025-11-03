def write_to_file(filename, lines):
    """Creates or overwrites a file and writes the given lines."""
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
    print(f"Successfully wrote {len(lines)} lines to {filename}")


def append_to_file(filename, lines):
    """Appends lines to an existing file."""
    with open(filename, 'a') as f:
        for line in lines:
            f.write(line + '\n')
    print(f"Successfully appended {len(lines)} lines to {filename}")
