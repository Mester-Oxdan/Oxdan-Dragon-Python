import imports.own.start_start
import os

def contains_spaces(text):
    return ' ' in text

file_path = os.path.dirname(__file__)
directories = file_path.split("\\")
file_name = directories[-1]
directories = directories[:-1]

# Keep track of the first and last words with spaces
first_space_word = None
last_space_word = None

# Detect first and last words with spaces
for directory in directories:
    if contains_spaces(directory):
        if first_space_word is None:
            first_space_word = directory
        last_space_word = directory

# Print the first and last words with spaces
if first_space_word is not None:
    if first_space_word == last_space_word:
        # Replace spaces within the first and last words with double quotes
        modified_path = file_path.replace(first_space_word, f'"{first_space_word}"')
    else:
        # Replace spaces within the first and last words with double quotes
        modified_path = file_path.replace(first_space_word, f'"{first_space_word}"')
        modified_path = modified_path.replace(last_space_word, f'"{last_space_word}"')

    os.environ["OXDAN-DRAGON-PYTHON"] = modified_path
    # Print the modified path
    #print("Modified Path:", modified_path)

    # Launch the modified file path (for Windows)
    #os.system("start " + modified_path)
#else:
    #print("No words with spaces found.")
#path_to_png = os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"..","IMAGES","ALL","icon.png")
os.environ["OXDAN-DRAGON-PYTHON"] = file_path

imports.own.start_start.start_start() 
