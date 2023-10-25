#------------------------------------------]
def split_string(input_string, max_length=95):
    # Split the input string into words
    words = input_string.split()

    # Initialize variables
    lines = []
    current_line = ""

    # Iterate through the words and create lines
    for word in words:
        if len(current_line) + len(word) + 1 <= max_length:
            # If adding the word does not exceed the max length, add it to the current line
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            # If adding the word would exceed the max length, start a new line
            lines.append(current_line)
            current_line = word

    # Append the last line
    if current_line:
        lines.append(current_line)

    return lines
#--------------------------------------------]