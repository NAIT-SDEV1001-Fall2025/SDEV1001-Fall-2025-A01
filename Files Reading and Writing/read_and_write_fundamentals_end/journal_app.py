# Journal Application

def read_journal(file_path):
    """Read the journal entries from a file."""
    try:
        with open(file_path, 'r') as file:
            # option 1: read all of the file at once
            entries = file.readlines()
        return [entry.strip() for entry in entries if entry.strip()]
    except FileNotFoundError:
        return ["Error: The file does not exist. Please check the file path."]

def write_journal(file_path, entry):
    """Write a journal entry to a file."""
    with open(file_path, 'a') as file:  # 'a' mode to append
        file.write(F"{entry}\n")

def main():
    file_path = 'journal.txt'
    while True:
        action = input("Do you want to (r)ead the journal or (w)rite a new entry? (q to quit): ").strip().lower()
        if action == 'r':
            entries = read_journal(file_path)
            print(F"Journal Entries of {file_path}:\n")
            for index, entry in enumerate(entries):
                print(entry)
        elif action == 'w':
            new_entry = input("Enter your journal entry: ")
            write_journal(file_path, new_entry)
            print("Entry added to the journal.")
        elif action == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()












'''
    try:
        with open(file_path, 'r') as file:
            # option 1: read all of the file at once
            entries = file.readlines()
        return [entry.strip() for entry in entries if entry.strip()]
    except FileNotFoundError:
        return []

'''