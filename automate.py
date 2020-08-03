#Program to open Google Chrome and search given keyword.
#AUTOMATION

#import the pyautogui module
import pyautogui

#pyautogui.position())   #get the position of the mouse
# pos: chrome - (698,767)
pyautogui.click(698, 767, interval = 2)
pyautogui.typewrite("facebook.com", interval=0.3)
pyautogui.typewrite(["enter"])


#pyautogui.click(1337, 7)
#




#P.S. All position are subjected to change, these positions are valid only in my PC
