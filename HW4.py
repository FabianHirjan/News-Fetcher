import os
import sys


def get_unique_extensions(directory):
    extensions = set()
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            _, ext = os.path.splitext(item)
            if ext:
                extensions.add(ext.lstrip('.'))
    return sorted(extensions)


def write_files_starting_with_A(directory, file_path):
    with open(file_path, 'w') as f:
        for item in os.listdir(directory):
            abs_path = os.path.join(directory, item)
            if os.path.isfile(abs_path) and item.startswith('A'):
                f.write(abs_path + '\n')


def process_path(my_path):
    if os.path.isfile(my_path):
        with open(my_path, 'r') as f:
            content = f.read()
        return content[-20:]
    elif os.path.isdir(my_path):
        extensions_count = {}
        for root, _, files in os.walk(my_path):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext:
                    ext = ext.lstrip('.')
                    extensions_count[ext] = extensions_count.get(ext, 0) + 1
        return sorted(extensions_count.items(), key=lambda x: -x[1])
    else:
        raise ValueError("Invalid path")


def get_unique_extensions_cli(directory):
    extensions = set()
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            _, ext = os.path.splitext(item)
            if ext:
                extensions.add(ext.lstrip('.'))
    return sorted(extensions)


def search_files(target, to_search):
    results = []
    if os.path.isfile(target):
        with open(target, 'r') as f:
            if to_search in f.read():
                results.append(target)
    elif os.path.isdir(target):
        for root, _, files in os.walk(target):
            for file in files:
                try:
                    with open(os.path.join(root, file), 'r') as f:
                        if to_search in f.read():
                            results.append(os.path.join(root, file))
                except Exception as e:
                    pass
    else:
        raise ValueError("Target must be a file or directory")
    return results


def search_files_with_callback(target, to_search, callback):
    results = []
    if os.path.isfile(target):
        with open(target, 'r') as f:
            if to_search in f.read():
                results.append(target)
    elif os.path.isdir(target):
        for root, _, files in os.walk(target):
            for file in files:
                try:
                    with open(os.path.join(root, file), 'r') as f:
                        if to_search in f.read():
                            results.append(os.path.join(root, file))
                except Exception as e:
                    callback(e)
    else:
        raise ValueError("Target must be a file or directory")
    return results


def get_file_info(file_path):
    if not os.path.isfile(file_path):
        raise ValueError("Provided path is not a file")
    return {
        "full_path": os.path.abspath(file_path),
        "file_size": os.path.getsize(file_path),
        "file_extension": os.path.splitext(file_path)[1].lstrip('.'),
        "can_read": os.access(file_path, os.R_OK),
        "can_write": os.access(file_path, os.W_OK)
    }


def list_files_in_directory(dir_path):
    if not os.path.isdir(dir_path):
        raise ValueError("Provided path is not a directory")
    return [
        os.path.join(dir_path, item)
        for item in os.listdir(dir_path)
        if os.path.isfile(os.path.join(dir_path, item))
    ]


if __name__ == "__main__":
    directory = "./example_directory"
    file_path = "./output.txt"

 