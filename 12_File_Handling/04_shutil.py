import shutil
import os
file_copy = shutil.copy("tasks.txt", "xyz_tasks.txt")
print(f"File Copied Successfully.")

os.makedirs("my_folder", exist_ok=True)
shutil.move("xyz_tasks.txt", "my_folder/")
print(f"File Moved Successfully.")

#shutil.rmtree("my_folder")
#print("Folder Deleted Permanently.")