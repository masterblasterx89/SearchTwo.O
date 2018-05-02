import os
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter
from tkinter import IntVar
from tkinter import Checkbutton

dir_list = []
path = os.getcwd()

def checkboxcheck():
    global dir_list
    global path
    if checkBoxYes.get() == 1:
        for path, dirs, files in os.walk(path):
            for x in files:
                dir_list.append(x)
                return dir_list
    elif checkBoxYes.get() <= 2:
        dir_list = [f for f in os.listdir('.') if os.path.isfile(f)]
        return dir_list


root = tkinter.Tk()
root.wm_title('Servo Control')
checkBoxYes = IntVar()
motorsCheck=Checkbutton(root,
    text="Motors ON(checked)/OFF(unchecked)",
    variable=checkBoxYes,
    command=checkboxcheck)
motorsCheck.pack()
scale = Scale(root, from_=0, to=180,
              orient=HORIZONTAL,label="Motor #",state=DISABLED)
scale.pack()
root.mainloop()