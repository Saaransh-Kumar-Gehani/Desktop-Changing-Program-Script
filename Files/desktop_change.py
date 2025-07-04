# Importing required modules
import keyboard
import requests
import ctypes
import os


# Variables
IMG : list[str] = []
c = -1
CurrentImg = ""
ButtonToShiftNext = "up"
ButtonToShiftPrevious = "down"
ButtonToSave = "space"
ButtonToExit = "esc"
# Set Image Folder you are going to use
cwd = os.getcwd()
ImageFolder = f"{cwd}\\Files\\Images"
SaveLoco = f"{cwd}\\Files\\SavedImages"
if os.path.exists(ImageFolder):
    pass
else:
    os.mkdir(ImageFolder)
if os.path.exists(SaveLoco):
    pass
else:
    os.mkdir(SaveLoco)


# Function to Add Image into the IMG list
def AddIMG(c):
    url = 'https://picsum.photos/1920/1080'
    r = requests.get(url)
    open(f'{ImageFolder}\\img-{c}.jpg','wb').write(r.content)
    img = f"{ImageFolder}\\img-{c}.jpg"
    IMG.append(img)


# Function that sets your wallpaper to given Image using IMG list index
def SetIMG(n):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, IMG[n], 0)
    return IMG[n]    


# Main Function that does most stuff.
def Main(st):
    global c
    global CurrentImg
    if st == 'Next':
        if c+1 == len(IMG):
            c+=1
            AddIMG(c)
            CurrentImg = SetIMG(c)
        elif 0 < c+1 < len(IMG):
            c+=1
            CurrentImg = SetIMG(c)
    elif st == 'Back':
        if c-1 > -1:
            c-=1
            CurrentImg = SetIMG(c)


# Function to save Image
s = len(os.listdir(SaveLoco)) + 1
# if os.path.exists(f"{ImageFolder}\\CurrentImg.jpg"):
#     x = True
def Save(): 
    global s
    with open(f'{ImageFolder}\\img-{c}.jpg','rb') as file:
        content = file.read()
        open(f'{SaveLoco}\\SavedImage-{s}.jpg','wb').write(content)
        s+=1
 
 
# You can set your key to change the Image
keyboard.add_hotkey(ButtonToShiftNext, Main, args=['Next'])
keyboard.add_hotkey(ButtonToShiftPrevious, Main, args=['Back'])

# Key save your favorite Image
keyboard.add_hotkey(ButtonToSave, Save)

# Key to break the program
keyboard.wait(ButtonToExit)


# This part of the code just deletes all the Images so that you don't occupy space
for i in IMG:
    if i != CurrentImg:
        os.remove(i)
os.remove(f"{ImageFolder}\\CurrentImg.jpg")
os.rename(CurrentImg, f"{ImageFolder}\\CurrentImg.jpg")





