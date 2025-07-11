# Open the file nl2.txt and read each line
with open('nl2.txt', 'r') as file:
    lines = file.readlines()

# Creating an empty list to store modified lines
modified_lines = []

# Iterate through each line and replace letters
for line in lines:
    modified_line = line

    # carry out the replacement
    if 'A' in line:
        modified_line = modified_line.replace('A', 'A:')
    if 'e' in line:
        modified_line = modified_line.replace('e', 'EI')
    if 'r' in line:
        modified_line = modified_line.replace('r', 'r=')
    if 'x' in line:
        modified_line = modified_line.replace('x', 'k')
    if 'Y' in line:
        modified_line = modified_line.replace('Y', 'U')
    if 'G' in line:
        modified_line = modified_line.replace('G', 'g')
    if 'L' in line:
        modified_line = modified_line.replace('L', 'l')
    if 'a' in line:
        modified_line = modified_line.replace('a', '{')
    if 'o' in line:
        modified_line = modified_line.replace('o', 'V')
    # Add the modified rows to the list, with or without changes
    modified_lines.append(modified_line)

# Write the modified content to a new file
with open('modified_nl2.txt', 'w') as file:
    file.writelines(modified_lines)

print("The file has been successfully modified and saved as modified_nl2.txt")
