__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil


def clean_cache():
    path_current_dir = os.path.dirname(__file__)
    new_folder = 'cache'
    path_new_folder = os.path.join(path_current_dir, new_folder)
    
    if not os.path.exists(path_new_folder):
        os.makedirs(path_new_folder)
    elif os.path.exists(path_new_folder):
        shutil.rmtree(path_new_folder)
        os.makedirs(path_new_folder)

def cache_zip(zip_path, cache_path):
    clean_cache()
    shutil.unpack_archive(zip_path, cache_path)

def cached_files():
    path = os.path.join(os.path.dirname(__file__), 'cache')
    list_files = os.listdir(path)
    list_files_paths = []

    for file in list_files:
        list_files_paths.append(os.path.join(path, file))
    return list_files_paths

def find_password(list):
    for item in list:
        file = open(item)

        for line in file:
            if 'password' in line:
                return line[line.find(' ') + 1: -1]
        file.close()






    









