#!/usr/bin/python3

import os

print()
def list_files(directory):
    try:
        # Get the list of files in the specified directory
        files = os.listdir(directory)

        # Print the list of files
        print("The list of records of patients is :\n")
        for file in files:
            print(file)

    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except PermissionError:
        print(f"Permission error accessing directory '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory name
directory_name = "health_reports"

# Call the function to list files in the specified directory
list_files(directory_name)
