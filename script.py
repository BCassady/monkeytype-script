from bs4 import BeautifulSoup
import pyautogui 
import time


# Download the html of the page
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

# Wait for the page to download
time.sleep(3)

# Read the file
file = open('Monkeytype.html', 'r')
html_doc = file.read() 

soup = BeautifulSoup(html_doc, 'html.parser')

# Read the words
words = soup.find_all("div", {"class": "word"})

result = ""

for word in words:
    # Read the letters and store
    letters = word.find_all("letter")
    for letter in letters:
        result += str(letter)[8]
    result += " "


# Write the words
pyautogui.write(result, interval = 0.005)

