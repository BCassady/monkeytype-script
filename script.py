from bs4 import BeautifulSoup
import pyautogui 
import time


pyautogui.keyDown('command')
time.sleep(.1)  
pyautogui.press('tab')
time.sleep(.1)
pyautogui.keyUp('command')
time.sleep(.2)
pyautogui.rightClick()

pyautogui.moveRel(50, 85, 0.25)
time.sleep(0.1)
pyautogui.click()
time.sleep(0.1)

pyautogui.moveTo(1100, 670, 0.25)
time.sleep(0.1)
pyautogui.click()

pyautogui.moveTo(780, 570, 0.25)
time.sleep(0.1)
pyautogui.click()
time.sleep(0.25)
pyautogui.press('a')

time.sleep(3)

file = open('Monkeytype.html', 'r')
html_doc = file.read() 

soup = BeautifulSoup(html_doc, 'html.parser')

words = soup.find_all("div", {"class": "word"})

result = ""

for word in words:
    letters = word.find_all("letter")
    for letter in letters:
        result += str(letter)[8]
    result += " "



pyautogui.write(result, interval = 0.005)

