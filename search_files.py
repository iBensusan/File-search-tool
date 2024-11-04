import os
import fnmatch

def search_files(directory, search_term):
    # Search for files recursively to handle nested directories
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if fnmatch.fnmatch(filename, f"*{search_term}"):
                matching_files.append(os.path.join(root, filename))
    
    if matching_files:
        print("\nFiles matching your search:")
        for file in matching_files:
            print(file)
    else:
        print("\nNo matching files found.")

def main():
    # Ask the user to input the directory path
    directory = input("Enter the directory to search in: ")
    
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Invalid directory path. Please try again.")
        return
    
    # Ask the user for the search term or file extension
    search_term = input("Enter the search term or file extension (e.g., '.txt'): ")
    
    # Perform the search
    search_files(directory, search_term)

if __name__ == "__main__":
    main()
