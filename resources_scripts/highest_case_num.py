import os

def find_highest_case_number(year):
    root_dir = '/Users/deantaylor/ohio_case_scrape'
    
    """
    Finds and prints the highest case number for files in the given year across all district subdirectories.
    
    :param year: The year to match in the subdirectory names.
    :param root_dir: The root directory to start the search. Defaults to the current directory.
    """
    highest_case_number = None
    year_str = str(year)

    for district in range(1, 13):
        # Path to the year subdirectory in each district
        year_dir = os.path.join(root_dir, f"District_{district}", year_str)

        for file in os.listdir(year_dir):
            if file.endswith('.pdf') and file.startswith(year_str):
                # Extracting the case number part of the filename
                parts = file.split('-')
                case_number = int(parts[2].split('.')[0])  # Assuming the format is 'YYYY-Ohio-XXX.pdf'
                highest_case_number = max(highest_case_number, case_number) if highest_case_number else case_number
    if highest_case_number == None:
        return 1
    return highest_case_number
  
# # root_directory = '/Users/deantaylor/ohio_case_scrape' # Replace with your directory path
# start_case_num = find_highest_case_number(2012)
# print(f'start case num: {start_case_num}')
