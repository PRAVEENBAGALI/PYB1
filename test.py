import os
current_directory = os.getcwd()
print(current_directory)
folder_name = os.path.basename(current_directory)
print(folder_name)

if os.path.exists(folder_name+'.'+".eprf"):
    print("EPRF File Exists")
else:
    print("EPRF file doesnot exists")
    
print("chnages")