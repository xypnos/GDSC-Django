import os
import shutil
from datetime import datetime, timedelta

def list_files(directory="."):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def is_modified_within_24_hours(file_path):
    now = datetime.now()
    file_stat = os.stat(file_path)
    modified_time = datetime.fromtimestamp(file_stat.st_mtime)
    created_time = datetime.fromtimestamp(file_stat.st_ctime)

    return now - modified_time < timedelta(hours=24) or now - created_time < timedelta(hours=24)

def update_files(files):
    for file in files:
        with open(file, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\nUpdated at {timestamp}")

def create_last_24hours_folder(folder_name="last_24hours"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def move_files_to_last_24hours(files, destination_folder="last_24hours"):
    for file in files:
        shutil.move(file, os.path.join(destination_folder, file))

if __name__ == "__main__":
    current_directory = os.getcwd()

    # List all files in the current directory
    files_in_directory = list_files(current_directory)

    # Identify files modified or created in the last 24 hours
    recent_files = [file for file in files_in_directory if is_modified_within_24_hours(file)]

    if recent_files:
        # Update the identified files
        update_files(recent_files)

        # Create "last_24hours" folder if it doesn't exist
        create_last_24hours_folder()

        # Move the updated files to the "last_24hours" folder
        move_files_to_last_24hours(recent_files)

        print("Files updated and moved to 'last_24hours' folder.")
    else:
        print("No files modified or created in the last 24 hours.")

Updated at 2023-12-12 17:13:47