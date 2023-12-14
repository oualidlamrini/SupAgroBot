import constants as const
import os
import shutil


# Ensure the Images directory exists, create if not
os.makedirs(const.IMAGES_DIRECTORY, exist_ok=True)

# Loop through the Downloads directory
for filename in os.listdir(const.DOWLOADS_DIRECTORY):
    if filename.endswith('.csv'):
        file_path = os.path.join(const.DOWLOADS_DIRECTORY, filename)
        # Move the PNG file to the Images directory
        shutil.move(file_path,const.IMAGES_DIRECTORY)