# Remove Background
from Supagro.imageJFunc import ImageJ 
import Supagro.constants as const
import os
from pathlib import Path
import ntpath
for filename in os.listdir(const.DIRECTORY):
    file_path = os.path.join(const.DIRECTORY, filename)
    # checking if it is a file
    if os.path.isfile(file_path):
        with ImageJ(teardown=False,file_path=file_path,file_name=filename) as bot:
            bot.Remove_background()