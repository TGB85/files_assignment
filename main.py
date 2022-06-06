__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile


def clean_cache():
    # temp_path = r"Wincpy\files\cache"
    temp_path = r"C:\Users\tammi\Documents\Winc\Wincpy\files\cache"
    # try:
    #     os.mkdir(temp_path)
    #     print("directory created")
    # except FileExistsError:
    #     print("directory already exists")
    if os.path.exists(temp_path):
        for file in os.listdir(temp_path):
            file_path = os.path.join(temp_path, file)
            # print(file_path)
            os.unlink(file_path)
        # print("directory cleared")
    else:
        os.mkdir(temp_path)
        # print("directory created")


# print(os.getcwd())
# clean_cache()


def cache_zip(zip_path, cache_path):
    if os.path.exists(cache_path):
        for file in os.listdir(cache_path):
            file_path = os.path.join(cache_path, file)
            os.unlink(file_path)
    else:
        os.mkdir(cache_path)
    with ZipFile(zip_path, mode="r") as zf:
        zf.extractall(cache_path)


# cache_zip("Wincpy\\files\\data.zip", "Wincpy\\files\\cache")


def cached_files():
    # cache_path = r"C:\Users\tammi\Documents\Winc\Wincpy\files\Temp"
    cache_path = r"C:\Users\tammi\Documents\Winc\Wincpy\files\cache"
    file_list = []
    # print(os.listdir(cache_path))
    for item in os.listdir(cache_path):
        item_path = os.path.join(cache_path, item)
        if os.path.isfile(item_path):
            file_list.append(item_path)
    return file_list


# print(cached_files())


def find_password(file_list):
    password_file = ""
    for item in file_list:
        # with open(r'c:\Users\tammi\Documents\Winc\Wincpy\files\Temp\new_file.txt', 'r') as f:
        with open(item, "r", errors="ignore") as f:
            for line in f.readlines():
                if "password" in line:
                    password_file += line
    return password_file[password_file.find(": ") + 2:].rstrip("\n")


# print(find_password(cached_files()))
