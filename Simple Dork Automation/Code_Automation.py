
import time

# Library for mouse, keyboard
import pyautogui as pya


# Time with pause
pya.PAUSE = 1


# Open Browser
pya.press ("win")
pya.write ("chrome")
pya.press ("enter")
pya.write ("insite:cpf filetype:pdf")
pya.press ("enter")
pya.press ("win")
pya.write ("chrome")
pya.press ("enter")
pya.write ("intitle: index of document*.pdf")
pya.press ("enter")






