from os import walk
import os
import hashlib
from collections import defaultdict

def hash_file(file_path, algo='sha256'):
    hasher = hashlib.new(algo)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicate_value_keys(original_dict):
    
    values_to_keys = defaultdict(list)
    
    for key, value in original_dict.items():
        if isinstance(value, list):
            value = tuple(value)
        values_to_keys[value].append(key)
        
    duplicate_values_info = {
        value: keys for value, keys in values_to_keys.items() if len(keys) > 1
    }
    return duplicate_values_info

def find_duplicates(dir_path: str):
    
    f = []
    for (dirpath, dirnames, filenames) in walk(dir_path):
        f.extend(filenames)
        break
    
    data = {}
    for file in f:
        file_path = os.path.join(dir_path, file)
        file_hash = hash_file(file_path)
        data[file_path] = file_hash
    duplicate_files = list(find_duplicate_value_keys(data).values())
    
    return duplicate_files

if __name__ == "__main__":
    
    find_duplicates("./tmp")
    find_duplicates("./unique_files")
    find_duplicates("./logs")