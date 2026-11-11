# Project 5: Large File Renamer

# Often, we have a large number of files in a directory with names that do not follow a specific pattern 
# or are not easy to understand. Renaming each file manually can be time-consuming and error-prone. To 
# solve this problem, we need a program that can rename a large number of files in bulk, based on a 
# specified pattern.

# Can you develop a Python program that takes a directory path and a pattern as input, and renames all 
# the files in the directory that match the pattern to a new name that follows the specified pattern?

import os
import re
from collections import Counter


# Setting up the directory and file paths
directory = r"path/to/your/folder"  # change to the folder you want to rename files in
files = os.listdir(directory)

pattern = r"([a-zA-Z]+)([-_]?)(\d+)"

# --- Pass 1: work out the structure of every file, collect the separators ---
parsed_files = []       # will hold (old_name, word, separator, number, ext) for each file
all_separators = []     # just the separators, so we can count them

# Loop through each file in the directory and parse its name based on the specified pattern.
for old_name in files:
    name, ext = os.path.splitext(old_name)
    match = re.match(pattern, name)

    # If the file name matches the expected structure, extract the word, separator, and number,
    # and store them in the parsed_files list. Also, collect the separators for later analysis.
    if match:
        word, separator, number = match.group(1), match.group(2), match.group(3)
        parsed_files.append((old_name, word, separator, number, ext))
        all_separators.append(separator)
    else:
        print(f"Skipping {old_name}, doesn't match expected structure")

# --- Work out the most common separator ---
if all_separators:
    counts = Counter(all_separators)
    winning_separator, count = counts.most_common(1)[0]
    print(f"Most common separator: {winning_separator!r} (used {count} times)")
else:
    winning_separator = ""
    print("No files matched the pattern, nothing to rename.")

# --- Pass 2: rename any file that doesn't already use the winning separator ---
for old_name, word, separator, number, ext in parsed_files:
    if separator == winning_separator:
        continue  # already matches the winning structure, leave it alone

    new_name = f"{word}{winning_separator}{number}{ext}"

    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed {old_name} -> {new_name}")