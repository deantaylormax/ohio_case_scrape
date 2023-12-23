import os
import glob

def find_lowest_year(root_dir):
    min_year = float('inf')
    pattern = os.path.join(root_dir, '**/*-Ohio-*.pdf')

    for filename in glob.glob(pattern, recursive=True):
        parts = os.path.basename(filename).split('-')
        if parts and parts[0].isdigit():
            year = int(parts[0])
            min_year = min(min_year, year)

    return min_year if min_year != float('inf') else None

# Replace 'your_directory_path' with the path to the root directory containing the subdirectories
root_directory = '/Users/deantaylor/ohio_case_scrape'
year = find_lowest_year(root_directory)
print(f"The lowest year is: {year}")
