import os

folder_path = './'

for i in range(29):
    file_name = f"{i}-answer.txt"
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, 'w') as file:
        file.write("")

print("Files created successfully!")
