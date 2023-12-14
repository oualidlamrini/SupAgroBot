# ImageJ
from Supagro.imageJFunc import ImageJ 
import Supagro.constants as const
import os
import sys
from pathlib import Path
import time
arg = sys.argv[1]
directory = os.path.join(const.BACH, arg)
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    file_name=Path(file_path).stem
    # checking if it is a file
    if os.path.isfile(file_path):
        with ImageJ(teardown=True,file_path=file_path,file_name=file_name) as bot:
            bot.land_first_page()
            time.sleep(2)
            bot.Upload_file()
            bot.Image_Adjust_Threshold()
 
            bot.Analyse_set_Mesurments_Mesure()
     
            bot.Analyse_Mesure()
            bot.save()
        os.remove(file_path)

