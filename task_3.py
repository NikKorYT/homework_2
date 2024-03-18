import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def print_dir(path, prefix=''):
    path = Path(path)
    contents = list(path.iterdir())
    pointers = ['┣ ' if i != len(contents) - 1 else '┗ ' for i in range(len(contents))]

    for pointer, sub_path in zip(pointers, contents):
        if sub_path.is_dir():
            print(prefix + pointer + Fore.GREEN + '📂 ' + sub_path.name)
            new_prefix = prefix + ('┃ ' if pointer == '┣ ' else '  ')
            print_dir(sub_path, new_prefix)
        else:
            print(prefix + pointer + Fore.WHITE + '📄 ' + sub_path.name)

if __name__ == "__main__":
    try:
        print(Fore.GREEN + '📦' + sys.argv[1])
        print_dir(sys.argv[1])
    except IndexError:
        print(Fore.RED + 'Please provide a directory path as an argument.(e.g. python task_3.py C:\\Users\\User\\Desktop\\folder_name)')