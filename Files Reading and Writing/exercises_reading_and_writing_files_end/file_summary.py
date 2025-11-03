from file_reader import read_file

def main():
    filename = input("Enter filename: ")
    lines = read_file(filename)
    print(f"Total non-empty lines: {len(lines)}")

if __name__ == "__main__": 
    main()