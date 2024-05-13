import os
import shutil

def delete_ipynb_checkpoints(root_dir):
    """
    Deletes files and directories containing '.ipynb_checkpoints' in their names
    within the specified root directory.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Check each file in directory
        for filename in filenames:
            if '.ipynb_checkpoints' in filename:
                file_path = os.path.join(dirpath, filename)
                print(f"Deleting file: {file_path}")
                os.remove(file_path)
        
        # Check each directory in directory
        for dirname in dirnames:
            if '.ipynb_checkpoints' in dirname:
                folder_path = os.path.join(dirpath, dirname)
                print(f"Deleting directory and contents: {folder_path}")
                shutil.rmtree(folder_path)

# Specify the root directory to search from
root_directory = '/path/to/search/directory'
delete_ipynb_checkpoints(root_directory)
