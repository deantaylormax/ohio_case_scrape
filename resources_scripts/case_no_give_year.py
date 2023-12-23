import os

def print_highest_case_number(year, root_dir='.'):
    """
    Prints the highest case number for files matching the given year in all subdirectories.
    
    :param year: The year to match in the file names.
    :param root_dir: The root directory to start the search. Defaults to the current directory.
    """
    year_prefix = f"{year}-Ohio-"
    highest_case_number = None

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.startswith(year_prefix):
                # Extracting the case number
                case_number_str = file[len(year_prefix):].split('.')[0]  # Removing file extension if any
                try:
                    case_number = int(case_number_str)
                    if highest_case_number is None or case_number > highest_case_number:
                        highest_case_number = case_number
                except ValueError:
                    # Handle the case where the extracted part is not a number
                    continue

    if highest_case_number is not None:
        print(f"Highest Case Number for {year}: {highest_case_number}")
    else:
        print(f"No cases found for year {year}")

# Example usage
case_num = print_highest_case_number(2017, '/Users/deantaylor/ohio_case_scrape')
print(case_num)
