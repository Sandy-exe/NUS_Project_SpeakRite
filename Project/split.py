import os
import shutil

source_folder = 'C:/Users/santosh kumar/Downloads/Indian Accent/Indian_accent/audio'
output_folder = 'C:/Users/santosh kumar/Downloads/Indian Accent/Indian_accent/audio/Indian_accent'
# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Sort the files in the source folder
file_list = sorted(os.listdir(source_folder))


# Split the files into subfolders
num_files_per_subfolder = 50
num_subfolders = len(file_list) // num_files_per_subfolder

for i in range(num_subfolders):
    print(f'Processing subfolder {i+1}/{num_subfolders}')
    subfolder_path = os.path.join(output_folder, f'subfolder_{i+1}')
    os.makedirs(subfolder_path, exist_ok=True)

    start_index = i * num_files_per_subfolder
    end_index = start_index + num_files_per_subfolder
    files_to_copy = file_list[start_index:end_index]

    for file_name in files_to_copy:
        source_file_path = os.path.join(source_folder, file_name)
        destination_file_path = os.path.join(subfolder_path, file_name)
        shutil.copy(source_file_path, destination_file_path)

print("Files split into subfolders.")
