import os
import shutil
import sys

def rename_files(original_text, new_text):
    # Get the current directory
    current_dir = os.getcwd()
    
    # Create a new subfolder named "Rename" if it doesn't exist
    new_folder_path = os.path.join(current_dir, "Rename")
    os.makedirs(new_folder_path, exist_ok=True)
    
    # Get a list of files in the current directory
    files = os.listdir(current_dir)
    # Filter only files (excluding directories) that match the criteria
    files_to_rename = [f for f in files if os.path.isfile(os.path.join(current_dir, f)) and original_text in f]
    
    if not files_to_rename:
        print("No files matching the criteria found.")
        return
    
    # Find the first file for example purposes
    example_file = files_to_rename[0]
    
    # Generate the new filename based on the user's input
    new_filename = example_file.replace(original_text, new_text)
    
    # Print the example filenames
    print("Example:")
    print(f"Original file name: {example_file}")
    print(f"New file name: {new_filename}")
    
    # Prompt the user for confirmation
    choice = input("Does the change look correct? (y/n): ")
    if choice.lower() != "y":
        print("No changes were made.")
        return
    
    # Rename and copy selected files
    for filename in files_to_rename:
        # Generate the new filename
        new_filename = filename.replace(original_text, new_text)
        # Create the path for the new file in the "Rename" subfolder
        new_filepath = os.path.join(new_folder_path, new_filename)
        # Copy the original file to the new subfolder with the new name
        shutil.copy2(os.path.join(current_dir, filename), new_filepath)
    
    print("File names have been changed and copied to the 'Rename' subfolder.")

# Check if the --help flag is specified or if there are not enough arguments
if "--help" in sys.argv or len(sys.argv) < 2:
    print("Usage: python rename_files.py [original_text] [new_text]")
    print("Arguments:")
    print("  [original_text]: Combination of letters and/or numbers within the file name to be changed (mandatory)")
    print("  [new_text]: Combination of letters and/or numbers to replace the original_text in the file name (optional)")
    sys.exit(0)

original_text = sys.argv[1]

# Check if the second argument is provided
if len(sys.argv) >= 3:
    new_text = sys.argv[2]
else:
    new_text = ""

# Call the rename_files function
rename_files(original_text, new_text)
