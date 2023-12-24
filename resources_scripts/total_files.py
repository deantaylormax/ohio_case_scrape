import os

def count_pdf_files(directory):
    """
    Count the total number of PDF files in a given directory and all its subdirectories.
    """
    total_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                total_count += 1
    return total_count

# Example usage
directory_path = '/Users/deantaylor/ohio_case_scrape/District_1'  # Replace with your directory path
total_pdf_count = count_pdf_files(directory_path)
print(f"Total number of PDF files: {total_pdf_count}")

avg_tokens_per_file = 6000
#multiply the result of teh function by the average number of tokens per file.
total_tokens = total_pdf_count * avg_tokens_per_file
print(f'total tokens is {total_tokens} with an average of {avg_tokens_per_file} tokens per file')
total_cost = (total_tokens/1000) * .0001

print(f'total cost is {total_cost}')