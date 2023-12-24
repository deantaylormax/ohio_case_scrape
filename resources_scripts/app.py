# %%
import requests
import os
import re
import glob
with open('year.txt', 'r') as year_file:
    year = int(year_file.read())

from highest_case_num import find_highest_case_number
root_directory = '/Users/deantaylor/ohio_case_scrape' # Replace with your directory path
case_number = find_highest_case_number(year)
# case_number = 6870
# %%
# def find_lowest_year(root_dir):
#     min_year = float('inf')
#     pattern = os.path.join(root_dir, '**/*-Ohio-*.pdf')

#     for filename in glob.glob(pattern, recursive=True):
#         parts = os.path.basename(filename).split('-')
#         if parts and parts[0].isdigit():
#             year = int(parts[0])
#             min_year = min(min_year, year)

#     return min_year if min_year != float('inf') else None

# %%
# def find_next_case_number(directory, year):
#     highest_case_number = 0
#     # year = find_lowest_year(directory)
#     # year=2018
#     # Regular expression to extract the case number
#     pattern = re.compile(rf"{year}-Ohio-(\d+)\.pdf")

#     # Iterate through all files in all subdirectories
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             match = pattern.match(file)
#             if match:
#                 case_number = int(match.group(1))
#                 if case_number > highest_case_number:
#                     highest_case_number = case_number

#     # Increment the highest case number by one
#     return highest_case_number + 1

# # Usage example
# directory_path = '/Users/deantaylor/ohio_case_scrape'
# # year = find_lowest_year(directory_path)
# case_no = find_next_case_number(directory_path, year)
# print(f"Next Case Number: {year}-Ohio-{case_no}")

# %%
def download_pdf(district, case_number, year):
    url = f"https://www.supremecourt.ohio.gov/rod/docs/pdf/{district}/{year}/{year}-Ohio-{case_number}.pdf"
    # url = base_url.format(district=district, case_number=case_number)
    response = requests.get(url)
    
    # Check if the response is successful (PDF exists)
    if response.status_code == 200:
        folder_name = f"District_{district}/{str(year)}"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        file_path = os.path.join(folder_name, f"{str(year)}-Ohio-{case_number}.pdf")
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return True
    return False

# Main loop to iterate through districts and case numbers
error = 0
# case_number = find_next_case_number(directory_path, year)

# case_number = 3099
while True:
    for district in range(1, 13):
        if download_pdf(district, case_number, year):
            print(f"Downloaded: District {district} - {year}-Ohio-{case_number}.pdf")
            case_number += 1
            error=0
            break
    else:
        # Break the while loop if the case number is not found in any district
        print(f"Case number {case_number} not found in any district.")
        error +=1
        if error > 20:
            case_number = (case_number // 1000) * 1000 + 1000 #round case number to the next thousand
            error = 0
        if case_number >= 9000: #indicates no more case numbers for this year.
        #round case number to the next thousand
            print(f'done with year {year}')
            # break
            year = int(year) - 1
            #write year to to year.txt file
            with open('year.txt', 'w') as f:
                f.write(str(year))
            print(f'year written to file is {year}')
            error = 0
            case_number = 1
            continue
        case_number += 1
        print(f'error count: {error}')
        continue