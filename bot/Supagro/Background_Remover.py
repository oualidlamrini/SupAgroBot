from selenium import webdriver
import Supagro.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import selenium.webdriver.common.alert as alt

from pynput.keyboard import Key,Controller
#from pynput.mouse import Button,Controller
import time 

from pathlib import Path
import ntpath

import subprocess

class ImageJ(webdriver.Chrome):
    def __init__(self,teardown=False):
        self.teardown = teardown
        options = Options()
        options.add_experimental_option("detach",True)
        super(ImageJ,self).__init__(options=options)
        self.implicitly_wait(40)
        self.maximize_window()
         

    def land_first_page(self):
        self.get(const.BASE_URL) 

    def __exit__(self, exc_type, exc_value, traceback):
        if self.teardown:
            self.quit()  
    
    #def cookies(self):
        #cookie = WebDriverWait(self, 10).until(
        #EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Accept')]")))
        #cookie.click() 

    def Upload_file(self,file_path):
        upload = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id='page-content']/div[2]/div[1]/div/div/div/div[2]/div[2]/button")
        ))
        upload .click()

        applescript_code = f'''
            tell application "System Events"
            keystroke "G" using {{command down, shift down}}
            delay 1
            keystroke "{file_path}"  # Replace with the path to your file
            delay 1
            keystroke return
            delay 1
            keystroke return
            end tell
            '''

        # Execute AppleScript using subprocess
        subprocess.run(['osascript', '-e', applescript_code])
        time.sleep(3)
        download = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id='page-content']/div/div/div/div/div[2]/div[2]/div[2]/button")
        ))
        download .click()

        applescript_code2 = f'''
            tell application "System Events"
            keystroke "{file_path}"  # Replace with the path to your file
            delay 1
            keystroke return
            end tell
            '''

        # Execute AppleScript using subprocess
        subprocess.run(['osascript', '-e', applescript_code2])






  


        
        



       