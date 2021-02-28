import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
from PIL import Image

def sign_in(meeting_id, meeting_password):

    # Open Zoom application on Mac OS
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])

    time.sleep(3)

    #click join button once zoom opens

    join_button = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_button)
    pyautogui.click()

    # Enter the meeting id in the meeting id box

    meet_id_box = pyautogui.locateCenterOnScreen('meet_id_box.png')
    pyautogui.moveTo(meet_id_box)
    pyautogui.click()
    pyautogui.write(meeting_id)

    # Click the join button 

    join_bn = pyautogui.locateCenterOnScreen('join_bn.png')
    pyautogui.moveTo(join_bn)
    pyautogui.click()

    # Short pause allowing the program to open the enter password box

    time.sleep(3)

    password_box = pyautogui.locateCenterOnScreen('password_box.png')
    pyautogui.moveTo(password_box)
    pyautogui.click()
    pyautogui.write(meeting_password)
    pyautogui.press('enter')
    
# Read the csv file

df = pd.read_csv('timings.csv')


while True:

    #check if the time at current instant exists in our excel sheet
    
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

        row  = df.loc[df['timings']== now]
        zm_id = str(row.iloc[0,1])
        zm_pwd = str(row.iloc[0,2])

        sign_in(zm_id, zm_pwd)

        print('You have signed in')



     


        




