import sys
from pathlib import Path
from colorama import Fore, init

# Initialize colorama with autoreset set to True. This means that every print statement will be in default color.
init(autoreset=True)

def print_dir(path, prefix=''):
    """
    This function prints the directory structure for the given path.
    """
    # Convert the path to a Path object
    path = Path(path)
    
    # Get a list of all items in the directory
    contents = list(path.iterdir())
    
    # Create a list of pointers. If the item is not the last one, use '┣ ', else use '┗ '
    pointers = ['┣ ' if i != len(contents) - 1 else '┗ ' for i in range(len(contents))]

    # Loop through each item in the directory
    for pointer, sub_path in zip(pointers, contents):
        
        # If the item is a directory, print it with the '📂' emoji and recurse into this directory
        if sub_path.is_dir():
            print(prefix + pointer + Fore.GREEN + '📂 ' + sub_path.name)
            new_prefix = prefix + ('┃ ' if pointer == '┣ ' else '  ')
            print_dir(sub_path, new_prefix)
            
        # If the item is a file, print it with the '📄' emoji
        else:
            print(prefix + pointer + Fore.WHITE + '📄 ' + sub_path.name)

if __name__ == "__main__":
    try:
        # Print the root directory with the '📦' emoji
        print(Fore.GREEN + '📦' + sys.argv[1])
        # Call the print_dir function to print the directory structure
        print_dir(sys.argv[1])
    except IndexError:
        # If no directory path is provided as an argument, print an error message
        print(Fore.RED + 'Please provide a directory path as an argument.(e.g. python task_3.py C:\\Users\\User\\Desktop\\folder_name)')