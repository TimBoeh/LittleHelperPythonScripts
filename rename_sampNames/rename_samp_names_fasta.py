import os
import shutil

def change_sample_names(directory):
    # Create the "cleanedSampNames" subdirectory
    cleaned_directory = os.path.join(directory, "cleanedSampNames")
    os.makedirs(cleaned_directory, exist_ok=True)

    # Find all FASTA files in the given directory
    fasta_files = [f for f in os.listdir(directory) if f.endswith(".fasta") or f.endswith(".fna")]

    # Check if there are any FASTA files in the directory
    if not fasta_files:
        print("No FASTA files found in the directory.")
        return

    for fasta_file in fasta_files:
        file_path = os.path.join(directory, fasta_file)

        # Read the contents of the original file
        with open(file_path, 'r') as file:
            original_content = file.readlines()

        # Generate the new file name
        new_file_name = fasta_file

        # Generate the path for the cleaned file
        cleaned_file_path = os.path.join(cleaned_directory, new_file_name)

        # Create the cleaned file with modified sample names
        with open(cleaned_file_path, 'w') as cleaned_file:
            for line in original_content:
                if line.startswith(">"):
                    line = line.strip()  # Remove leading/trailing whitespace
                    sequence_name = line[1:]  # Remove the '>'
                    modified_name = sequence_name.split(" ", 1)[0]  # Keep only the first word
                    cleaned_file.write(">" + modified_name + "\n")
                else:
                    cleaned_file.write(line)

    print(f"Processed {len(fasta_files)} FASTA files. Sample names have been cleaned and files saved in the 'cleanedSampNames' directory.")

# Provide the directory path where your FASTA files are located
directory_path = '.'

# Call the function to change the sample names
change_sample_names(directory_path)
