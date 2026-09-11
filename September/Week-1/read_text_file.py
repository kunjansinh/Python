# Create a text file
text_file = open("notes.txt", "w")

text_file.write("Python is easy to learn.\n")
text_file.write("Functions help organise programs.\n")
text_file.write("Files can store information.\n")

text_file.close()


# Read the text file
text_file = open("notes.txt", "r")

for line in text_file:
    print(line.strip())

text_file.close()
