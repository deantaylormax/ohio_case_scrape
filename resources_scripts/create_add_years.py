import os

# Directory path where the District directories are located
base_directory = "/Users/deantaylor/ohio_case_scrape"  # Replace with the actual directory path

# Years to create as subdirectories
years = range(2002, 1999, -1)  # 2012 down to 2003

# Loop through each district and create year subdirectories
for district_number in range(1, 13):  # District_1 through District_12
    district_path = os.path.join(base_directory, f"District_{district_number}")
    for year in years:
        year_path = os.path.join(district_path, str(year))
        os.makedirs(year_path, exist_ok=True)

# This is a confirmation message
print("Subdirectories for years 2012 to 2003 have been created in each District directory.")

# def round_down_to_previous_thousand(n):
#     return (n // 1000) * 1000 + 1000

# # Test the function
# number = 1345
# rounded_number = round_down_to_previous_thousand(number)
# print(rounded_number)

