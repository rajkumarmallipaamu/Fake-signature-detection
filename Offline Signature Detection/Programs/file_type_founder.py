import os

def list_unique_file_types(directory):
    file_types = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_type = file.split('.')[-1] if '.' in file else 'No extension'
            file_types.add(file_type)
    return file_types

# Specify the directory path
directory_path = "C:\\signatures\\test\\full_forg"

# List unique file types
unique_file_types = list_unique_file_types(directory_path)

# Display the unique file types
print("Unique file types in the directory:")
for file_type in unique_file_types:
    print(file_type)
