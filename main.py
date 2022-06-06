__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile


def clean_cache():
    # temp_path = r"Wincpy\files\cache"
    cache_path = r"C:\Users\tammi\Documents\Winc\Wincpy\files\cache"
    if os.path.exists(cache_path):
        for file in os.listdir(cache_path):
            file_path = os.path.join(cache_path, file)
            os.unlink(file_path)
        # print("directory cleared")
    else:
        os.mkdir(cache_path)
        # print("directory created")


def cache_zip(zip_path, cache_path):
    clean_cache()
    with ZipFile(zip_path, mode="r") as zf:
        zf.extractall(cache_path)


def cached_files():
    cache_path = r"C:\Users\tammi\Documents\Winc\Wincpy\files\cache"
    file_list = []
    for item in os.listdir(cache_path):
        item_path = os.path.join(cache_path, item)
        if os.path.isfile(item_path):
            file_list.append(item_path)
    return file_list


def find_password(file_list):
    password_file = ""
    for item in file_list:
        with open(item, "r", errors="ignore") as f:
            for line in f.readlines():
                if "password" in line:
                    password_file += line
    return password_file[password_file.find(": ") + 2 :].rstrip("\n")

def main():
    print(os.getcwd())
    clean_cache()
    cache_zip("Wincpy\\files\\data.zip", "Wincpy\\files\\cache")
    print(cached_files())
    print(find_password(cached_files()))

if __name__ == "__main__":
    main()
