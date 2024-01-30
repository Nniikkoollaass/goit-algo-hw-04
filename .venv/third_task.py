import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def display_directory_structure(directory_path, indent=0):

    try:
        path=Path(directory_path)
        if not path.exists() or not path.is_dir():
            print(f"{Fore.RED}Error: The specified path is not a valid directory.")
            return
        
        for item in path.iterdir():
            if item.is_dir():
                print(f"{Fore.CYAN}{'  '*indent} 🗁 {item.name}")
                display_directory_structure(item, indent+1)
            else:
                print(f"{Fore.GREEN}{'  '*indent} ✉️ {item.name}")

    except Exception as e:
        print(f"{Fore.RED} An error occured: {e}")

if __name__=="__main__":
    if len(sys.argv)!=2:
        print(f"{Fore.RED}Please use correct quantity of arguments")
    else:
        direcroty_path=sys.argv[1]
        display_directory_structure(direcroty_path)
  