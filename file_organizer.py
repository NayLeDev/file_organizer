import os
import shutil

def get_user_path():
    """
    Asks the user if they want to use the base path or specify a different path.
    Returns the chosen path.
    """
    use_base_path = input("Do you want to use the base path? (yes/no): ").lower()
    if use_base_path == 'yes':
        return os.getcwd()
    elif use_base_path == 'no':
        return input("Enter the path (e.g., 'C:\\Users\\<USERNAME>\\Downloads'): ")
    else:
        print("Invalid input. Using the base path by default.")
        return os.getcwd()

def organize_files_by_extension(src_path, num_files_to_exclude):
    """
    Organizes files in the source directory based on their extensions.
    Creates directories for each unique extension and moves files accordingly.
    Files without extensions are moved to a directory named "None".
    """
    # Check if the source path exists
    if not os.path.exists(src_path):
        print(f"The specified path '{src_path}' does not exist.")
        return
    
    # Get the list of files in the source directory
    file_list = os.listdir(src_path)

    # Ask the user for the names of files to exclude from organization
    files_to_exclude = []
    for _ in range(num_files_to_exclude):
        file_name = input("Enter the name of the file to exclude from organization (e.g., 'example.txt'): ")
        files_to_exclude.append(file_name)

    # Traverse each file in the source directory
    for file_name in file_list:
        file_path = os.path.join(src_path, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Extract file name and extension
        name, ext = os.path.splitext(file_name)

        # Create a directory for the extension if it doesn't exist
        ext_directory = os.path.join(src_path, ext[1:])
        os.makedirs(ext_directory, exist_ok=True)

        # Handle files without extensions
        if not ext and file_name not in files_to_exclude:
            none_directory = os.path.join(src_path, 'None')
            os.makedirs(none_directory, exist_ok=True)
            shutil.move(file_path, os.path.join(none_directory, file_name))
            print(f"File '{file_name}' moved to 'None' directory.")
        elif ext and file_name not in files_to_exclude:
            # Move the file to the corresponding extension directory
            shutil.move(file_path, os.path.join(ext_directory, file_name))
            print(f"File '{file_name}' moved to '{ext}' directory.")

    print("File organization completed successfully.")

if __name__ == "__main__":
    # Get the path from the user
    path = get_user_path()

    # Input the number of files to exclude from organization
    num_files_to_exclude = int(input("Enter the number of files you do not want to organize: "))
    
    # Organize files in the specified directory
    organize_files_by_extension(path, num_files_to_exclude)
