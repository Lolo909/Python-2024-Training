
# Task 2: Create a Python script that does the following:

# a. Open a text file called "notes.txt" in write mode ('w') and write the following content:
# Line 1: This is a note.
# Line 2: Another note.
# Line 3: Final note.

# b. Close the file.
# c. Reopen the same file in read mode ('r') and read its content into a list, where each line is a separate element in the list.
# d. Use the seek() function to move the file pointer to the beginning of the second line (i.e., after "Line 1: This is a note.").
# e. Modify the second line to say "Line 2: Updated note."
# f. Reopen the file in write mode ('w') again and write the modified list of lines back to the file.


try:
    with open("Files17\\notes.txt", 'w') as file:
        textToWrite = ["Line 1: This is a note.", "Line 2: Another note.","Line 3: Final note."]
        for line in textToWrite:            
            file.write(line + "\n")
        file.close()
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

text =""
try:
    with open('Files17\\notes.txt', 'r') as file:
        text = file.readlines()
        file.seek(23)
        text[1] = "Line 2: Updated note.\n"
        file.close()
        # Process the text data here
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")


try:
    with open("Files17\\notes.txt", 'w') as file:
        for line in text:
            file.write(line)
        file.close()
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")