import constants as const
import os
from pathlib import Path
import ntpath
import pandas as pd  

df = pd.DataFrame()
#df.loc[0,] = [0,0] 
for filename in os.listdir(const.IMAGES_DIRECTORY):
    file_path = os.path.join(const.IMAGES_DIRECTORY, filename)
    #file_name=Path(file_path).stem
    # checking if it is a file
    if os.path.isfile(file_path):
        temp = pd.read_csv(file_path)
        df = pd.concat([df,temp.iloc[:,1:-1]], ignore_index = True)

df.to_csv(const.SAVE, index=False)
