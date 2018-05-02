try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import os
import re
from tkinter import IntVar
from tkinter import Checkbutton

resultTextLabel = None
folderPath = None
mainWindow = tkinter.Tk()
recursive_check = IntVar()


def info_window():
    '''
        Will prompt the user to select a folder with a window screen. 
    '''

    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Search", "Please select the folder you want to search. ")
    root.destroy()
    get_dict()


def get_dict():
    '''
        Browser window opens to have the user select a folder.
    '''
    global mainWindow
    global folderPath
    root = tkinter.Tk()
    root.withdraw()
    folderPath = askdirectory()
    root.destroy()
    folderLabel = tkinter.Label(mainWindow, text=get_users_directory(folderPath), background='gray24', foreground="Orange", font='bold')
    folderLabel.grid(row=1, column=1, sticky='s')


def get_search_string():
    '''
        Will grab what is in the SearchString Entry and return it. 
    '''
    # print(stringEntry.get())
    string = stringEntry.get()
    return string


def get_users_directory(path):
    '''
        Will take the users path and split it to pull out the folder the user wants to search, to prompt them the folder
        name in the main function. 
    '''
    user_path = path.split('/')
    user_dir = user_path[-1]
    return user_dir


def open_dir():
    '''
        Will open the folder the user picked in with get_dict()
    :return: 
    '''
    global folderPath
    os.startfile(folderPath + "\\" "NEW")


def get_directory_list(rootDir):
    dir_list = []
    if recursive_check.get() == 1:
        folder_list = os.walk(rootDir)
        for path, dirs, files in folder_list:
            for x in files:
                dir_list.append(x)
            print(dir_list)

    else:
        dir_list = [f for f in os.listdir('.') if os.path.isfile(f)]
        print("Root Dir")

    return dir_list


def get_search_results():
    '''
        This will search the directory the user passed in the get_users_directory funcation and search for the 
        string the user specified. 
        :return: 
    '''
    global mainWindow
    global resultTextLabel
    count = 0
    os.chdir(folderPath)
    cwd = os.getcwd()
    # dir_list = [f for f in os.listdir('.') if os.path.isfile(f)]
    list = get_directory_list(folderPath)
    for fileName in list:
        file = open(fileName, 'r')
        text = file.read()
        find_data = re.findall(get_search_string(), text)
        file.close()
        if len(find_data) > 0 and fileName != "SearchOMatic.py":
            if (os.path.isdir("NEW")) is True:
                pass
            else:
                os.makedirs("NEW")
            os.rename(cwd + "\\" + fileName, cwd + "\\" "NEW" + "\\" + fileName)
            count = count + 1
        else:
            pass
    resultTextLabel.grid_forget()
    resultTextLabel = tkinter.Label(mainWindow, text="Results:" + str(count), highlightbackground='gray24', background='gray24', foreground="Orange", font='bold')
    resultTextLabel.grid(row=3, column=2, sticky='w')


backgroundImage = tkinter.PhotoImage(file='image.gif')
backgroundImageLabel = tkinter.Label(mainWindow, image=backgroundImage)
backgroundImageLabel.place(x=0, y=0)
mainWindow.title("SearchOMatic")
mainWindow.geometry('605x325-8-200')

# folderLabel = tkinter.Label(text="Test Folder", background='gray24', font='bold')
# folderLabel.grid(row=1, column=1, sticky='s')

browseButton = tkinter.Button(text="Browse Folder", highlightbackground='gray24', width=12, command=info_window)
browseButton.grid(row=2, column=1, sticky='n')
checkBox = tkinter.Checkbutton(text="Recursively", variable=recursive_check)
checkBox.grid(row=2, column=1, sticky='s')
searchStringLabel = tkinter.Label(text="Search String", background='gray24', foreground="Orange", font='bold')
searchStringLabel.grid(row=1, column=2, sticky='s')
stringEntry = tkinter.Entry(mainWindow, width=22, highlightbackground='gray24')
stringEntry.grid(row=2, column=2, sticky='n')
searchButton = tkinter.Button(text="Search", highlightbackground='gray24', width=12, command=get_search_results)
searchButton.grid(row=2, column=3, sticky='n')

resultTextLabel = tkinter.Label(mainWindow, text="Results:", highlightbackground='gray24', background='gray24', foreground="Orange", font='bold' )
resultTextLabel.grid(row=3, column=2, sticky='w')
openDirButton = tkinter.Button(text="Open Folder", highlightbackground='gray24', width=12, command=open_dir)
openDirButton.grid(row=3, column=2, sticky='e')


cancelButton = tkinter.Button(text='Cancel', highlightbackground='gray24', width=12, command=mainWindow.destroy)
cancelButton.grid(row=4, column=3, sticky='e')


mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)

mainWindow.resizable(False, False)
mainWindow.iconbitmap('icon.ico')
mainWindow.mainloop()
