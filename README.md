# File Search Tool

An intermediate-level Python tool designed to search for files within a specified directory based on a search term or file extension and display matching results with their full file paths. This tool is ideal for learners who know Python fundamentals and are looking to practice building complete and practical programs.

## Features

- **Recursive Search**: Searches for files within the specified directory and all its subdirectories.
- **Pattern Matching**: Supports searching by filename patterns or extensions (e.g., `.txt`, `.png`).
- **Cross-Platform Compatibility**: Works seamlessly on Windows, macOS, and Linux.
- **User-Friendly Prompts**: Guides the user through the search process with clear input prompts.

## Requirements

- Python 3.x
- Standard Python libraries (`os`, `fnmatch`)

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/username/file-search-tool.git
    cd file-search-tool
    ```

2. Ensure Python 3 is installed on your system:
    ```bash
    python --version
    ```

## Usage

1. Run the `file_search_tool.py` script:
    ```bash
    python file_search_tool.py
    ```

2. Enter the directory path to search in when prompted.
3. Enter the search term or file extension (e.g., `.txt`).
4. View the list of matching files and their full paths in the console.

## Example Workflow

1. Start the script and input `/Users/yourusername/Documents` as the directory path.
2. Enter `.pdf` as the search term.
3. The script outputs all `.pdf` files in the specified directory and its subdirectories:
    ```
    Files matching your search:
    /Users/yourusername/Documents/file1.pdf
    /Users/yourusername/Documents/notes/file2.pdf
    ```

## Files

- `file_search_tool.py`: The main Python script implementing the file search functionality.
- `README.md`: Project description and usage instructions.

## License

This project is licensed under the MIT License.
