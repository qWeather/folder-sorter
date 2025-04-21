import os
import os.path
import shutil

file_types = {
    ".pdf": "PDFs",    
    ".py": "Python",    
    ".jpg": "Images",    
    ".jpeg": "Images",    
    ".png": "Images",    
}

def folder_sorter(folder_path: str, dry_run: bool) -> None:
    moved = 0

    for folder in ("PDFs", "Python", "Images"):
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    if dry_run:
        for file in os.listdir(folder_path):
            if not os.path.isfile(os.path.join(folder_path, file)):
                continue
            ext = os.path.splitext(file)[1].lower()
            if ext in file_types:
                moved += 1
                dest_folder = file_types[ext]
                print(f"Would move {file} to folder {dest_folder}")
    else:
        for file in os.listdir(folder_path):
            if not os.path.isfile(os.path.join(folder_path, file)):
                continue
            ext = os.path.splitext(file)[1].lower()
            if ext in file_types:
                moved += 1
                dest_folder = file_types[ext]
                shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, dest_folder))
                print(f"Moved {file} to folder {dest_folder}")

    print(f"{'Would have moved' if dry_run else 'Moved'} {moved} file(s) in total.")
