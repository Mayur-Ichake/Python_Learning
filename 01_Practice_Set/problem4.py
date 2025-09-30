import os

# Get the path of the directory (you can change it to any other path)
directory_path = "/python"

# Print the contents of the directory
print(f"Contents of directory '{directory_path}':")
for item in os.listdir(directory_path):
    print(item)
