import glob, os
file_lst = []
os.chdir("C:\\D\\Temp\\COMPARE-STUDY\\01_HardnessStudy_BVM_Stamp")
for file in glob.glob("*.erfh5"):
    file_lst.append(file)
print(file_lst)

# import OS module
import os

# Get the list of all files and directories
path = "C:\\D\\Temp\\COMPARE-STUDY\\01_HardnessStudy_BVM_Stamp"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)

import os

for x in os.listdir():
    if x.endswith(".eprf"):
        # Prints only text file present in My Folder
        print(x)


import os

# folder path
dir_path = "C:\\D\\Temp\\COMPARE-STUDY\\01_HardnessStudy_BVM_Stamp"

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

from os import walk

# folder path
dir_path = "C:\\D\\Temp\\COMPARE-STUDY\\01_HardnessStudy_BVM_Stamp"

# list to store files name
res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
print(res)

import glob
print(glob.glob("C:\\D\\Temp\\COMPARE-STUDY\\01_HardnessStudy_BVM_Stamp\\*\\*\\*\\*"))

import os
res1 = []
for root, dirs, files in os.walk("C:\\D\\Temp\\COMPARE-STUDY\\01_HardnessStudy_BVM_Stamp"):
    for file in files:
        if file.endswith('.erfh5'):
            res.extend((os.path.join(root,file)))
            print(res1)


import os
# list to store txt files
res2 = []
# os.walk() returns subdirectories, file from current directory and
# And follow next directory from subdirectory list recursively until last directory
for root, dirs, files in os.walk(r"C:\\D\\Temp\\COMPARE-STUDY\\01_HardnessStudy_BVM_Stamp"):
    for file in files:
        if file.endswith(".log"):
            res.append(os.path.join(root, file))
print(res2)