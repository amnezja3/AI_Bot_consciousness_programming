import pyautogui as pa
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import sys
import time
from time import sleep
import virtualPC as vpc
from virtualPC import VirtualData as VD


minShot = pa.locateCenterOnScreen('minShot.png')
minOnShot = pa.locateCenterOnScreen('minOnShot.png')

if minShot:
    pa.moveTo(minShot)
    pa.click()
if minOnShot:
    pa.moveTo(minOnShot)
    pa.click()
sleep(1)

class MainProcess:
    def __init__(self, root):      
        screenSize = pa.size()
        self.sWidth = screenSize[0]
        self.sHeight = screenSize[1]

        sScale = 2
        rezW = int(self.sWidth / sScale)
        rezH = int(self.sHeight / sScale - 20)
        posW = rezW - 40

        self.root = root
        self.root.title("VirtualPC")
        self.root.geometry(f"{rezW}x{rezH}+{posW}+20")         
        self.root.resizable(True, True)        
        # self.root.attributes('-alpha', 0.95)        
        self.bg=ImageTk.PhotoImage(file="curScrMain.png")
        
        self.mainGui = Frame(root)
        self.mainGui.pack(side="top", expand=True, fill="both")
        
        Label(self.mainGui, text=" ", font=("Consolas", 36, "bold"), fg="white", bg="#131313", justify="left").place(x=0, y=0, width=2840, height=2460)
        Label(self.mainGui, text="Welcome to Virtual PC", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=400, y=185, height=20)

        Button(self.mainGui, text="new project", command=self.newProject, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=400, y=210, width=230, height=20)
        Button(self.mainGui, text="open project", command=self.openProject, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=400, y=240, width=230, height=20)
    
    def newProject(self):
        for widgets in self.mainGui.winfo_children():
            widgets.destroy()      
        
        self.bg_image=Label(self.mainGui) 
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.mainGui, text=" ", font=("Consolas", 36, "bold"), fg="white", bg="#131313", justify="left").place(x=0, y=0, width=2840, height=2460)

        Label(self.mainGui, text="Name of project", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=400, y=185, height=20)

        self.setNameOfProject = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.setNameOfProject.insert(END, "NewProject") 
        self.setNameOfProject.place(x=400, y=210, width=320, )

        Button(self.mainGui, text="create", command=self.setProjectName, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=400, y=240, width=320)

    def setProjectName(self):
        n = self.setNameOfProject.get()
        n = n.strip()
        name = ""
        for nn in n:
            if nn != ' ' and nn != '.' and nn != ',' and nn != '~' and nn != '`' and nn != '|' and nn != '@' and nn != '#' and nn != '$' and nn != '%' and nn != '^' and nn != '&' and nn != '*' and nn != '(' and nn != ')' and nn != '+' and nn != '/' and nn != '?':
                name += nn
        ext = "Pro is good"
        for item in os.listdir('./dataProjects'):            
            if item == name:
                ext = 'Project already exist for this name'           
        if ext != 'Project already exist for this name' and name !="":
            self.projectName = name
            try:os.mkdir(f'./dataProjects/{name}/')
            except:pass
            f = open(f'./dataProjects/{name}/{name}.vpc', 'w+')
            ti = time.strftime("%B %d %Y %H:%M:%S", time.localtime())
            f.write(f'#$%^&*(st)HEADER|||TAB1|||TAB2|||TAB3|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')            
            f.write(f'h1:#$%^&*(st)|||Title|||{self.projectName}|||{ti}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.write(f'#$%^&*(st)PRE_LOADER|||TAB1|||TAB2|||TAB3|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')            
            f.write(f'#$%^&*(gg)PRO_GENERAL|||TAB1|||TAB2|||TAB3|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.write(f'#$%^&*(st)LOG_SESSION|||TAB1|||TAB2|||TAB3|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()            
            
            for widgets in self.mainGui.winfo_children():
                widgets.destroy()   
            
            self.bg_image=Label(self.mainGui) 
            self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

            Label(self.mainGui, text=" ", font=("Consolas", 36, "bold"), fg="white", bg="#131313", justify="left").place(x=0, y=0, width=2840, height=2460)
            Label(self.mainGui, text="You need to set your own flags ..", font=("Consolas", 10, "normal"), fg="gray", bg="#131313", justify="left").place(x=370, y=165, width=340, height=20)
            
            Label(self.mainGui, text="Author", font=("Consolas", 7, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=397, y=185, height=20)  
            self.setFlagW = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
            self.setFlagW.insert(END, "Anonymous") 
            self.setFlagW.place(x=402, y=210, width=80)

            Label(self.mainGui, text="License", font=("Consolas", 7, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=487, y=185, height=20)  
            self.setFlagH = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
            self.setFlagH.insert(END, "GPL") 
            self.setFlagH.place(x=492, y=210, width=80)            

            Button(self.mainGui, text="setFlag", command=self.createNewProject, font=("Consolas", 10, "normal"), fg="yellow", bg="#131313", bd=0, justify="left").place(x=547, y=207)
        else:
            Label(self.mainGui, text=f"{name} : {ext}", font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=400, y=265, width=340, height=20)
            Button(self.mainGui, text=f"open {name}", command=self.openProject, font=("Consolas", 8, "normal"), fg="#d2ff00", bg="#131313", bd=0, justify="left").place(x=400, y=295) 

    def createNewProject(self):
        flagW = self.setFlagW.get()
        flagH = self.setFlagH.get()

        # try:int(flagW)
        # except:flagW = 150
        # try:int(flagH)
        # except:flagH = 50

        f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
        f.write(f'h2:#$%^&*(st)|||Descriptions|||{flagW}|||{flagH}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
        f.write(f'#$%^&*(st)SEQUENCES|||TAB1|||TAB2|||TAB3|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
        f.close()        
        for widgets in self.mainGui.winfo_children():
            widgets.destroy()  
  
        self.bg_image=Label(self.mainGui)  
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.mainGui, text=" ", font=("Consolas", 36, "bold"), fg="white", bg="#131313", justify="left").place(x=0, y=0, width=2840, height=2460)
        Label(self.mainGui, text="Congratulations!! You have created a new project ..", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=400, y=185, height=20)
        Button(self.mainGui, text=f"start {self.projectName}", command=self.openNewProject, font=("Consolas", 10, "normal"), fg="yellow", bg="#131313", bd=0, justify="left").place(x=410, y=210, height=20)

    def openProject(self):        
        for widgets in self.mainGui.winfo_children():
            widgets.destroy()  
        
        self.bg_image=Label(self.mainGui) 
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.mainGui, text=" ", font=("Consolas", 36, "bold"), fg="white", bg="#131313", justify="left").place(x=0, y=0, width=2840, height=2460)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#1b1b1b", justify="left").place(x=65, y=100, width=425, height=375)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#1b1b1b", justify="left").place(x=495, y=100, width=400, height=110)

        Label(self.mainGui, text=f"List of projects", font=("Consolas", 10, "normal"), fg="#91856c", bg="#131313", justify="left").place(x=65, y=70, height=20)
        Label(self.mainGui, text='Other options', font=("Consolas", 10, "normal"), fg="#91856c", bg="#131313", justify="left").place(x=495, y=70, height=20)
        
        Label(self.mainGui, text="Select project", font=("Consolas", 10, "normal"), fg="#5ea146", bg="#1b1b1b", justify="left").place(x=65, y=105, height=20)
        self.my_listBoxProjects = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", justify="left")
        self.my_listBoxProjects.place(x=85, y=125, width=380, height=345)

        Label(self.mainGui, text='Opening a project', font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=65, y=25, height=20)

        Button(self.mainGui, text="exit", command=self.restart, font=("Consolas", 8, "normal"), fg="#c65f5f", bg="#131313", bd=0, justify="left").place(x=860, y=27, height=20)
         
        Button(self.mainGui, text="open", command=self.openProjectFromList, font=("Consolas", 8, "normal"), fg="#d2ff00", bg="#1b1b1b", bd=0, justify="left").place(x=455, y=105, height=16)   

        Button(self.mainGui, text="Create a new project..", command=self.newProject, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=105, height=16)         
        
        projectList = os.listdir('./dataProjects')      
        for i in projectList:            
            self.my_listBoxProjects.insert(END, i)

    def openProjectFromList(self):
        choice = self.my_listBoxProjects.get(ANCHOR)
        if choice != "":            
            self.projectName = choice    
            os.system(f'start python workspace.py -p {choice}')  
            sys.exit()
        else: Label(self.mainGui, text="Select project !!!", font=("Consolas", 10, "normal"), fg="red", bg="#1b1b1b", justify="left").place(x=65, y=105, height=20)

    def openNewProject(self):       
        os.system(f'start python workspace.py -p {self.projectName}') 
        sys.exit()

    def restart(self):
        os.system('start python constructor.py')
        sys.exit()


root = tkinter.Tk()
area = MainProcess(root)
root.mainloop()