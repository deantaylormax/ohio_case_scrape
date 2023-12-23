import os
from pathlib import Path

def remove_str_from_filenames(directory, string_to_remove):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if string_to_remove in filename:
                old_file = Path(root) / filename
                new_file = Path(root) / filename.replace(string_to_remove, '')
                os.rename(old_file, new_file)
                print(f"Renamed '{old_file}' to '{new_file}'")

# Replace 'your_directory_path' with the path to your target directory
directory_path = '/Users/deantaylor/ohio_case_scrape'
string_to_remove = 'str'
remove_str_from_filenames(directory_path, string_to_remove)
