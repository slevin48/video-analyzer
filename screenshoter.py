import os
import datetime
import keyboard
import pyautogui

try:
    os.mkdir('screenshots')
except OSError as error:
    print(error)

k = 0
now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M")
os.mkdir("screenshots/screenshot_"+now)

region = [
  368,
  107,
  1530,
  867
]

while True:   
    if keyboard.read_key() == "p":
        # st.write("You pressed p")
        img = pyautogui.screenshot()
        # img = pyautogui.screenshot(region=region)
        img.save(f'screenshots/screenshot_{now}/screenshot_{k}.png')
        k+=1
    if keyboard.read_key() == "esc":
        break