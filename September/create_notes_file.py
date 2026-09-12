notes = [
    "Learn Python",
    "Practice functions",
    "Practice file handling",
    "Build small programs"
]

with open("notes.txt", "w") as file:
    for note in notes:
        file.write(note + "\n")

print("Notes saved successfully.")
