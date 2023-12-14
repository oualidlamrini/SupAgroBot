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
import os
from pathlib import Path
import ntpath

import subprocess

class ImageJ(webdriver.Chrome):
    def __init__(self,teardown=False, file_path=" ", file_name=" "):
        self.teardown = teardown
        self.file_path = file_path
        self.file_name = file_name
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

    def Upload_file(self):
        file = WebDriverWait(self, 240).until(
        EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'File')]")
        ))
        file .click()

        openn = WebDriverWait(self, 10).until(
        EC.element_to_be_clickable((By.XPATH,f"//label[contains(text(),'Open...')]")
        ))

        openn.click()

        self.implicitly_wait(40)
        select_file = self.find_element(By.ID,'open-file-modal-select')
        select_file.click()

        
        applescript_code = f'''
        tell application "System Events"
        keystroke "G" using {{command down, shift down}}
        delay 1
        keystroke "{self.file_path}"  # Replace with the path to your file
        delay 1
        keystroke return
        delay 1
        keystroke return
        end tell
        '''
        time.sleep(2)
        # Execute AppleScript using subprocess
        subprocess.run(['osascript', '-e', applescript_code])
        time.sleep(3)
        

    def Image_Adjust_Threshold(self):
        image = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[1]/div[4]/ul/li[3]')))
        image.click()

        type = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[1]/div[4]/ul/li[3]/ul/li[1]/a/label')))
        type.click()

        gray = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[1]/div[4]/ul/li[3]/ul/li[1]/ul/li[1]/a/label')))
        gray.click()

        image = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[1]/div[4]/ul/li[3]')))
        image .click()

        adjust = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[1]/div[4]/ul/li[3]/ul/li[3]/a')))
        adjust.click()

        threshold = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[1]/div[4]/ul/li[3]/ul/li[3]/ul/li[4]/a')))
        threshold.click() 

        input_threshold = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,' //*[@id="cheerpjDisplay"]/div[3]/div[1]/input[1]')))
        input_threshold.clear()
        time.sleep(2)
        input_threshold.send_keys("100")         
        #time.sleep(5)
        apply = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[3]/div[1]/div[1]/div/input[3]')))
        apply.click() 

        dissmos = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[3]/div[2]/a[2]')))
        dissmos.click()         


        

    def Analyse_set_Mesurments_Mesure(self):
        analyse = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[1]/div[4]/ul/li[5]/a/label')))
        analyse.click()

        set_mesurments = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[1]/div[4]/ul/li[5]/ul/li[7]/a/label')))
        set_mesurments.click()    

        # chacke_boxes
        check = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[3]/div[1]/div[5]/div/div[14]/div/div/input'))).is_selected()
        minmax = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[3]/div[1]/div[5]/div/div[14]/div/div/input')))
        if check==True:
            minmax.click()

        display = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[3]/div[1]/div[4]/div/div[5]/div/div/input')))
        display.click()

        checkbox1 = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[3]/div[1]/div[5]/div/div[2]/div/div/input')))
        checkbox1.click()

        checkbox2 = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[3]/div[1]/div[4]/div/div[6]/div/div/input')))
        checkbox2.click()

        ok = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,' //*[@id="cheerpjDisplay"]/div[3]/div[1]/div[1]/div/input[1]')))
        ok.click()  


    def Analyse_Mesure(self):
        analyse = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[1]/div[4]/ul/li[5]/a/label')))
        analyse.click()

        mesure = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[1]/div[4]/ul/li[5]/ul/li[1]/a/label')))
        mesure.click()

    def save(self):
        file = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[3]/div[4]/ul/li[1]/a/label')))
        file.click()  
        save_as = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="cheerpjDisplay"]/div[3]/div[4]/ul/li[1]/ul/li[1]/a/label')))
        save_as.click()  

        time.sleep(2)
        alert = alt.Alert(self)
        alert.send_keys(self.file_name +  ".csv")
        alert.accept()
        time.sleep(3)

    def Remove_background(self):
        self.get(const.REMOVE_BACKGROUND)
        time.sleep(2)
        upload = WebDriverWait(self, 60).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="page-content"]/div[2]/div[1]/div/div/div/div[2]/div[2]/button')))
        upload.click()

        applescript_code = f'''
            tell application "System Events"
            keystroke "G" using {{command down, shift down}}
            delay 1
            keystroke "{self.file_path}"  # Replace with the path to your file
            delay 1
            keystroke return
            delay 1
            keystroke return
            end tell
            '''

        # Execute AppleScript using subprocess
        subprocess.run(['osascript', '-e', applescript_code])
        time.sleep(7)

        download = self.find_element(By.XPATH,"//*[@id='page-content']/div/div/div/div/div[2]/div[2]/div[2]/button")

        download .click()



             


            



             


        

        





        



        

       

        

      
  
       
        



        

        

         

 

