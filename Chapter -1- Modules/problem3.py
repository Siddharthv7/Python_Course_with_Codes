import os
# select the directory whose content you want to list
directory_path = '/'
# use the os module to list the directory contents
contents = os.listdir(directory_path)

print(contents)