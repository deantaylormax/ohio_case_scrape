from subprocess import Popen
import sys
import os

filename = sys.argv[1]
with open('checkpoint.txt', 'r') as case_file:
        case = case_file.read() # Replace with your initial year value

while case != '/Users/deantaylor/ohio_case_scrape/District_10/2023/2023-Ohio-944.pdf':
    print("\nStarting " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()

    # Read the 'year' value from a file created by the script being restarted
    with open('checkpoint.txt', 'r') as case_file:
        case = case_file.read()

print(f"case is {case}, Script Stopped")