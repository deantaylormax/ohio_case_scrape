import os
import shutil

def create_and_move_files(root_dir='.'):
    years = [str(year) for year in range(2013, 2024)]  # List of years from 2013 to 2023

    for district in range(1, 13):  # For each district
        district_dir = os.path.join(root_dir, f"District_{district}")
        
        if not os.path.exists(district_dir):
            continue  # Skip if the district directory doesn't exist

        # Create year subdirectories in each district directory
        for year in years:
            year_dir = os.path.join(district_dir, year)
            os.makedirs(year_dir, exist_ok=True)

        # Move files to corresponding year directories
        for file in os.listdir(district_dir):
            if file.endswith('.pdf') and file[:4] in years:
                src = os.path.join(district_dir, file)
                dest = os.path.join(district_dir, file[:4], file)
                shutil.move(src, dest)

# Example usage
create_and_move_files('/Users/deantaylor/ohio_case_scrape')
