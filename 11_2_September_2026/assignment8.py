# Read all lines from the input file
with open("file.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))

# first two lines
first_two = lines[:2]

with open("output.txt", "w") as file:
    file.writelines(first_two)

print("First two lines written to output.txt")