import requests
import ctypes
import os
import time


# Set Image Folder you are going to use
cwd = os.getcwd()
ImageFolder = f"{cwd}\\Files\\Images"


# Function to Add Image into the IMG list
def AddIMG():
    global img
    url = 'https://picsum.photos/1920/1080'
    r = requests.get(url)
    open(f'{ImageFolder}\\img.jpg','wb').write(r.content)
    img = f"{ImageFolder}\\img.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0) 


AddIMG()

time.sleep(2)

os.remove(img)