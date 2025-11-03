from file_writer import write_to_file, append_to_file

def main():
    filename = input("Enter filename: ").strip()
    mode = input("Do you want to write or append? ").strip().lower()
    count = int(input("How many lines? "))

    lines = []
    for i in range(1, count + 1):
        line = input(f"Enter line {i}: ")
        lines.append(line)

    if mode == 'write':
        write_to_file(filename, lines)
    elif mode == 'append':
        append_to_file(filename, lines)
    else:
        print("Invalid option. Please enter 'write' or 'append'.")

if __name__ == "__main__":
    main()
