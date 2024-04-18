import os
import shutil

def clean_folder(folder_path):
    # Get all Entry (File and Subfolder) inside folder_path
    for entry_name in os.listdir(folder_path):
        # Get Full Path
        entry_path = os.path.join(folder_path, entry_name)
        
        # Check File or Folder
        if os.path.isfile(entry_path):
            # If File, delete
            os.remove(entry_path)
            print(f"File {entry_name} has been deleted.")
        elif os.path.isdir(entry_path):
            # If Folder, Delete that folder and it's content inside
            shutil.rmtree(entry_path)
            print(f"Folder {entry_name} and all its contents have been deleted.")

clean_folder('folder_path')
