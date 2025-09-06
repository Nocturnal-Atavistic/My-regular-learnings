import os
import time
import shutil

path = input("Enter path C: " )
os.chdir(path)
destination = "C:\\python project\\License"

def subfolder_copy():
    filetype = input("Filetype: ")

    for folder, subfolders, files in os.walk(path):
        for file in files:
            if file.startswith(filetype):
                shutil.copy(os.path.join(folder, file), destination)
                print(f"{file} copied")
            else:
                print("error copying")

subfolder_copy()
