def read_notes(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())


read_notes("notes.txt")
