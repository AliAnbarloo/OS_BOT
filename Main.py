import os , time , sys
import subprocess , platform
from pathlib import Path
"""This is a simple robot (maybe it can't even be called a robot) 
to show the contents of a folder along with its files and you can search in your chosen folder.
The only available commands are exit and cls.
In most cases, you have to enter the address of your folder
then a list of the contents of the folder will be displayed.
You will need subprocess and platform and pathlib .
to install them, type the following commands in the CMD environment

pip3 install platform

pip3 install subprocess

pip3 install pathlib"""
def cls():
    os.system("clear") and os.system("cls")
def sprint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
def print_tree(directory_path, indent=""):
    directory = Path(directory_path)
    if directory.is_dir():
        print(indent + f"<--Folder--> {directory.name}")
        for item in directory.iterdir():
            if item.is_dir():
                print_tree(item, indent + "  |")
            else:
                print(indent + "  |" + item.name)
    else:
        print("Invalid directory path")
def search_file(directory_path, file_name):
    directory = Path(directory_path)
    if directory.is_dir():
        for item in directory.iterdir():
            if item.is_file() and item.name == file_name:
                return True
            elif item.is_dir():
                if search_file(item, file_name):
                    return True
    return False

cls()
def dir():
    global System
    System = platform.system()
    if System == 'Linux':
        output = subprocess.check_output(['lsblk']).decode('utf-8')
        sprint("Your drives:\n\n")
        sprint(output)
    else:
        drives = [drive for drive in os.listdir('/') if os.path.isdir(os.path.join('/', drive))]
        sprint(f'Number of your drives: {len(drives)}\n')
        for drive in drives:
            sprint(f'Drives Name: {drive}\n')
counter = []
if __name__ =="__main__":
    while True:
        if len(counter) == 0:
            dir()
            counter.append(1)
        else:
            if System == 'Linux':
                sprint("Linux path example : /home/ubuntu/\n")
            else:
                sprint("Windows path example : C:\Windows\n")
            directory_path = input("Enter the desired folder name (Enter ex to exit) : ")
            if directory_path == 'ex' or directory_path =="exit":
                exit()
            elif directory_path == 'cls':
                cls()
            else:
                print_tree(directory_path)
                file_name_to_search = input("Are you looking for a specific file? (enter file name): ")
                if file_name_to_search=="n" or file_name_to_search=="no":
                    pass
                else:
                    if search_file(directory_path, file_name_to_search):
                        print(f"The file '{file_name_to_search}' exists in the directory.")
                    else:
                        print(f"The file '{file_name_to_search}' does not exist in the directory.")

