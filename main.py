__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile


def clean_cache():
    cache_path = os.path.join(os.getcwd(), "cache") 
    if os.path.isdir(cache_path):
        for file in os.listdir(cache_path):
            os.remove(os.path.join(cache_path, file))
    else:
        os.mkdir(cache_path)


def cache_zip(zip_path, cache_path):
    clean_cache()
    with ZipFile(zip_path, mode="r") as zf:
        zf.extractall(cache_path)


def cached_files():
    cache_path = os.path.abspath('files/cache') 
    # cache_path = os.path.join(os.getcwd(), "cache") wordt niet goedgekeurd door wincpy check
    file_list = []
    for entry in os.scandir(cache_path):
        if entry.is_file():
            file_list.append(entry.path)
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
    cache_zip("data.zip", "cache")
    print(cached_files())
    print(find_password(cached_files()))


if __name__ == "__main__":
    main()
