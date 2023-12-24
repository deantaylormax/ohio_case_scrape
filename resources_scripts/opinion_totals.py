import os
import pandas as pd

root_dir = '/Users/deantaylor/ohio_case_scrape' # Replace with your directory path
def count_cases():
    # Prepare a list to hold the counts
    counts = []

    for district in range(1, 13):
        for year in range(2003, 2024):
            # Path to the year subdirectory in each district
            path = os.path.join(root_dir, f"District_{district}", str(year))

            if os.path.exists(path):
                # Counting the number of case files
                case_count = len([file for file in os.listdir(path) if file.endswith('.pdf')])
                counts.append({'District': district, 'Year': year, 'Case Count': case_count})

    # Creating a DataFrame
    df = pd.DataFrame(counts)
    return df

# Replace 'path_to_directory' with the path to the directory containing the District folders
df = count_cases()
# Display the DataFrame
print(df)