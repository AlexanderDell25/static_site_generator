import os
import shutil

def copy_delete_folder(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination)
    #print(f"{destination} got deleted and recreated.")
    
    for item in os.listdir(source):
        item_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination_path)
            #print(f"{item_path} copied to {destination_path}")
        else:
            os.makedirs(destination_path, exist_ok=True)  # Ensure the subdirectory exists
            #print(f"new folder created at {destination_path}")
            copy_delete_folder(item_path, destination_path) # Recursively copy subfolders

# Adjust paths to expand user home -> test stuff
#source = os.path.expanduser("~/workspace/github.com/AlexanderDell25/static_site_generator/static")
#destination = os.path.expanduser("~/workspace/github.com/AlexanderDell25/static_site_generator/public")

#copy_delete_folder(source, destination)