#1.File Creation:
# >Create a Python script (file_handling_assignment.py) that does the following:
# >Creates a new text file named "my_file.txt" in write mode ('w').
# >Write at least three lines of text to the file, including a mix of strings and numbers.

#2.File Reading and Display:
# >Enhance your script to read the contents of "my_file.txt" and display them on the console.

#3.File Appending:
# >Modify the script to open "my_file.txt" in append mode ('a').
# >Append three additional lines of text to the existing content.

#4.Error Handling:
# >Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError)

# 1. File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("Second line: PLP\n")
        file.write("Third line: Learn Python\n")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")
else:
    print("File 'my_file.txt' created successfully.")

# 2. File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("File contents:")
        print(contents)
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# 3. File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appended line.\n")
        file.write("Week 5 assignment\n")
        file.write("File handling.\n")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
else:
    print("File appended successfully.")

    # Print the updated file contents after appending
    try:
        with open("my_file.txt", "r") as file:
            updated_contents = file.read()
            print("\nUpdated file contents:")
            print(updated_contents)
    except Exception as e:
        print(f"An error occurred while reading the updated file: {e}")

# 4. Error Handling
try:
    with open("non_existent_file.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("File 'non_existent_file.txt' not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operations completed.")