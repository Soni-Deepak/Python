import os

# Enter the directory path
path = input("Enter directory path: ")

# Get the list of files and folders
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)