import os

source_folder = r"./"

print('Enter your name of file: ')
name = input()
print('Enter your new name of file: ')
new_name = input()
print('Enter your file extension: ')
extension = input()

for filename in os.listdir(source_folder):
    # check if any of the files are extension
    if os.path.isfile(os.path.join(source_folder, filename)) and filename.endswith(extension):
        # if yes, rename the file
        os.rename(os.path.join(source_folder, filename), os.path.join(
            source_folder, filename.replace(name, new_name)))
