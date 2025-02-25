import os

# Define the path to the folder containing the files
FOLDER_PATH = "../Files"

# List all files in the folder
files = sorted(os.listdir(FOLDER_PATH))

# Rename files sequentially
for i, file_name in enumerate(files, start=1):
    old_path = os.path.join(FOLDER_PATH, file_name)

    # Get the file extension
    file_extension = os.path.splitext(file_name)[1]

    # Define the new file name
    new_name = f"{i}{file_extension}"

    new_path = os.path.join(FOLDER_PATH, new_name)

    # Rename the file
    os.rename(old_path, new_path)

print("Files successfully renamed!")
