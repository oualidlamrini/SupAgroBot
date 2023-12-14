import constants as const
import os
import shutil

os.makedirs(const.OUTPUT_DIRECTORY, exist_ok=True)

# List all files in the source directory
files = os.listdir(const.SOURCE_DIRECTORY)
files = [file for file in files if file.endswith('.jpg') or file.endswith('.png')]  # Filter only image files

# Split files into 6 groups of 20
images_per_directory = 20
num_directories = 6

for i in range(num_directories):
    batch = files[i * images_per_directory: (i + 1) * images_per_directory]
    batch_output_directory = os.path.join(const.OUTPUT_DIRECTORY, f'batch_{i + 1}')
    os.makedirs(batch_output_directory, exist_ok=True)
    for file in batch:
        source_file = os.path.join(const.SOURCE_DIRECTORY, file)
        shutil.copy(source_file, batch_output_directory)
    
