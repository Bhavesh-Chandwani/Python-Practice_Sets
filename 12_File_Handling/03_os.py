import os 
current_directory = os.getcwd()
print(f"The Current Working Directory is : {current_directory}")

directory_list = os.listdir(current_directory)
print(f"The list of directory is : {directory_list}")

new_folder_path = os.path.join(current_directory, "my_folder")
os.makedirs(new_folder_path, exist_ok=True)
print(f"The folder created at : {new_folder_path}")