import os
import shutil

def copy_file_with_path(source_file, destination_path):
    if not os.path.exists(source_file):
        print(f"copy_file_with_path: {source_file} does not exists")
        return
    
    # Check if the destination directory exists, create it if it doesn't
    destination_dir = os.path.dirname(destination_path)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Copy the file to the destination path
    shutil.copy(source_file, destination_path)
    
def change_extension(file_path, new_extension):
    # Split the file path into root and extension
    root, _ = os.path.splitext(file_path)
    
    # Concatenate the new extension onto the root
    new_file_path = root + new_extension
    
    return new_file_path


def write_list_to_file(lst, file_path):
    with open(file_path, "w") as f:
        for item in lst:
            f.write(str(item) + "\n")
            
def get_immediate_parent(file_path):
    return os.path.basename(os.path.dirname(file_path))