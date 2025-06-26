import os
import shutil

def clean_folder(root_path):
    print(f"Cleaning folder: {root_path}")
    
    # Root-only files/folders to delete
    root_files_to_delete = ['.gitignore', '.gitattributes']
    root_dirs_to_delete = ['.github']

    # Recursively deleted file extensions
    extensions_to_delete = {'.md', '.png', '.jpeg', '.jpg', '.json', '.csv','.'}

    # Delete from root
    for item in root_files_to_delete:
        path = os.path.join(root_path, item)
        if os.path.isfile(path):
            os.remove(path)
            print(f"Removed file: {path}")

    for item in root_dirs_to_delete:
        path = os.path.join(root_path, item)
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Removed folder: {path}")

    # Walk recursively
    for dirpath, dirnames, filenames in os.walk(root_path):
        for file in filenames:
            ext = os.path.splitext(file)[1].lower()
            if ext in extensions_to_delete:
                full_path = os.path.join(dirpath, file)
                os.remove(full_path)
                print(f"Removed file: {full_path}")

folder = input("Enter the fullpath to your local IRDB folder (unzipped):\n")
clean_folder(folder)