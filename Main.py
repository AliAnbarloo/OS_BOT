import os , time , sys
from pathlib import Path
def cls():
    os.system("clear") and os.system("cls")
def sprint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.002)
cls()

def count_and_list_subdirectories(directory_path):
    directory = Path(directory_path)
    if directory.is_dir():
        subdirectories = [subdir for subdir in directory.iterdir() if subdir.is_dir()]
        subdirectory_names = [subdir.name for subdir in subdirectories]
        return len(subdirectories), subdirectory_names
    else:
        return 0, []

directory_path = '/path/to/directory'
num_subdirectories, subdirectory_names = count_and_list_subdirectories(directory_path)

print(f"تعداد دایرکتوری‌ها: {num_subdirectories}")
print(f"نام دایرکتوری‌ها: {', '.join(subdirectory_names)}")

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

# مسیر دایرکتوری مورد نظر را وارد کنید:
directory_path = '/home/ubuntu/بارگیری‌ها'
print_tree(directory_path)
file_name_to_search = input("آیا به دنبال یک فایل خاص هستید؟ (نام فایل را وارد کنید): ")

if search_file(directory_path, file_name_to_search):
    print(f"فایل '{file_name_to_search}' در دایرکتوری وجود دارد.")
else:
    print(f"فایل '{file_name_to_search}' در دایرکتوری موجود نیست.")

