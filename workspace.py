import pyautogui as pa
import tkinter
from tkinter import *

import tkinter.filedialog
from tkinter.filedialog import askopenfile, askdirectory
from PIL import Image, ImageTk
import argparse
import os
import sys
import time
from shutil import copyfile
from time import sleep
import virtualPC as vpc
from virtualPC import VirtualData as VD
import editorVPC as ev


#####################################        ARGUMETOWANIE SKRYPTU     #####################################
parser = argparse.ArgumentParser(description="Hacker GRA cRPG v1")
parser.add_argument("-p", "--project", type=str, help="Enter the name in the command line, if there are spaces use quotation marks")
args = parser.parse_args()
project = args.project
##################################### ARGUMETOWANIE SKRYPTU ZAKONCZONE #####################################


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

        proName = project #'NewProject' #self.projectName
        self.projectName = proName
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
        # self.root.resizable(False, False)   
        # self.root.overrideredirect(True)  
        # self.root.attributes('-alpha', 0.95)        
        self.bg=ImageTk.PhotoImage(file="curScrMain.png")
        
        self.mainGui = Frame(root)
        self.mainGui.pack(side="top", expand=True, fill="both")

        self.screen = Image.open('curScrMain.png')
        self.resized = self.screen.resize((rezW,rezH), Image.ANTIALIAS)
        self.newScreen = ImageTk.PhotoImage(self.resized)
        self.bg_image=Label(self.mainGui, image=self.newScreen, width=rezW, height=rezH) 
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)
        

        # MISC FUNCTIONS
        self.coords = {'mouseClickButton': 'one', 'mouseClickScr': 'left', 'locateOnScreen': (0,0,0,0) }

        self.locateOnScreenDict = {
                        'Center' : 'Center_NO', 'Flag' : (100, 100), 'GoAnd' : 'GoAnd_Click', 'Wait' : 'Wait_NO',  'Tolerance' : 'Tolerance_90'
                                    }
        self.checkFlagOnScreenDict = {
                        'Command' : 'stop', 'Message' : "message", 'SequenceFile' : "None:///12345667876!@#$%^&*().1234342323fdsfsdfsdfsd", 'Tolerance' : 'Tolerance_90'
                                    }
        self.checkPixelOnScreenDict = {
                        'Command' : 'stop', 'Message' : "message", 'SequenceFile' : "None:///12345667876!@#$%^&*().1234342323fdsfsdfsdfsd", 'Tolerance' : 'Tolerance_90', 'RGB' : (0,0,0), 'Locate' : (100,100)
                                    }
        self.checkRaportDict = {
                        'Dir' : './', 'Raport' : "raport", 'Tolerance' : 'Tolerance_90'
                                    }
        #EDITORS
        self.editorCommand = False
        self.editorLine = ''
        self.fileNameLocateOn = 'flag_id'

        #PLAY EXCALIBURE
        self.playExcalibureLoop = 1

        # Remover Lines
        self.removeLineProject = None

        # iserter line before
        self.insertCommand = False
        self.insertbeforeLine = ''

        self.bg_image=Label(self.mainGui, image=self.newScreen, width=rezW, height=rezH) 
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.mainGui, text=" ", font=("Consolas", 36, "bold"), fg="white", bg="#131313", justify="left").place(x=0, y=0, width=2840, height=2460)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#1b1b1b", justify="left").place(x=65, y=100, width=425, height=375)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#1b1b1b", justify="left").place(x=495, y=100, width=400, height=110)

        Label(self.mainGui, text=f"Name of project: {proName}", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=65, y=25, height=20)
        Label(self.mainGui, text=f'dataProjects/{proName}/{proName}.vpc', font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=65, y=45, height=20)
        Label(self.mainGui, text=f"Task list", font=("Consolas", 10, "normal"), fg="#91856c", bg="#131313", justify="left").place(x=65, y=70, height=20)
        Label(self.mainGui, text='Add task to list', font=("Consolas", 10, "normal"), fg="#91856c", bg="#131313", justify="left").place(x=495, y=70, height=20)
        
        V = VD(f'dataProjects/{proName}/{proName}.vpc')
        HEADER = V.header()
        SEP = "</>"
        TITLE = vpc.idSectionBack(HEADER, 1)[0]+" "+vpc.idSectionBack(HEADER, 2)[0]+" "+vpc.idSectionBack(HEADER, 3)[0]
        FLAGS = vpc.idSectionBack(HEADER, 1)[1]+":"+vpc.idSectionBack(HEADER, 2)[1]+" // "+vpc.idSectionBack(HEADER, 3)[1]        
    
        Label(self.mainGui, text=f"(st)HEADER", font=("Consolas", 10, "normal"), fg="#872119", bg="#1b1b1b", justify="left").place(x=65, y=100, height=20)
        Label(self.mainGui, text=TITLE, font=("Consolas", 10, "normal"), fg="#76af7a", bg="#1b1b1b", justify="left").place(x=85, y=125)
        Label(self.mainGui, text=FLAGS, font=("Consolas", 10, "normal"), fg="#76af7a", bg="#1b1b1b", justify="left").place(x=85, y=145)
        

        Button(self.mainGui, text="edit", command=self.editLineProject, font=("Consolas", 8, "normal"), fg="#d2ff00", bg="#1b1b1b", bd=0, justify="left").place(x=450, y=165, height=16)
        Button(self.mainGui, text="insert", command=self.insertLineProject, font=("Consolas", 8, "normal"), fg="#00edf0", bg="#1b1b1b", bd=0, justify="left").place(x=405, y=165, height=16)
        Button(self.mainGui, text="remove", command=self.removerLineProject, font=("Consolas", 8, "normal"), fg="orange", bg="#1b1b1b", bd=0, justify="left").place(x=360, y=165, height=16)

        SEQ = V.proSequence()
        Label(self.mainGui, text=f"(st)SEQUENCES", font=("Consolas", 10, "normal"), fg="#5ea146", bg="#1b1b1b", justify="left").place(x=65, y=165, height=20)
        self.my_listBoxSequence = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 7, "normal"), fg="#648c70", bg="#1b1b1b", justify="left")
        self.my_listBoxSequence.place(x=85, y=185, width=380, height=275)
        
        lenSeq = len(vpc.idSectionBack(SEQ, 1))
        
        if lenSeq > 0:
            for i in range(lenSeq):
                item = vpc.idSectionBack(SEQ, 0)[i]+SEP+vpc.idSectionBack(SEQ, 1)[i]+SEP+vpc.idSectionBack(SEQ, 2)[i]+SEP+vpc.idSectionBack(SEQ, 3)[i]+SEP+vpc.idSectionBack(SEQ, 4)[i]+SEP+vpc.idSectionBack(SEQ, 5)[i]+SEP+vpc.idSectionBack(SEQ, 6)[i]+SEP+vpc.idSectionBack(SEQ, 7)[i]+SEP+vpc.idSectionBack(SEQ, 8)[i]+SEP+vpc.idSectionBack(SEQ, 9)[i]
                self.my_listBoxSequence.insert(END, item)

        Button(self.mainGui, text="exit", command=self.exitProgram, font=("Consolas", 8, "normal"), fg="#3f6a6e", bg="#131313", bd=0, justify="left").place(x=860, y=27, height=20)
        Button(self.mainGui, text="reload", command=self.restart, font=("Consolas", 8, "normal"), fg="#e2cf63", bg="#131313", bd=0, justify="left").place(x=810, y=27, height=20)
        Button(self.mainGui, text="delete", command=self.delProject, font=("Consolas", 8, "normal"), fg="#c65f5f", bg="#131313", bd=0, justify="left").place(x=765, y=27, height=20)
        Button(self.mainGui, text="constructor", command=self.openConstructor, font=("Consolas", 8, "normal"), fg="#e2cf63", bg="#131313", bd=0, justify="left").place(x=690, y=27, height=20)
        Button(self.mainGui, text="play", command=self.playExcalibure, font=("Consolas", 8, "normal"), fg="#84e263", bg="#131313", bd=0, justify="left").place(x=660, y=27, height=20)
        
        Button(self.mainGui, text="osSystem", command=self.osSystem, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=105, height=16)
        Button(self.mainGui, text="SleepNow", command=self.sleepNow, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=125, height=16)
        Button(self.mainGui, text="OnScreen", command=self.locateOnScreen, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=145, height=16)
        Button(self.mainGui, text="DictWrite", command=self.dictWrite, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=165, height=16)
        Button(self.mainGui, text="TypeWrite", command=self.typeWrite, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=185, height=16)

        Button(self.mainGui, text="keyPress", command=self.keyPress, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=105, height=16)
        Button(self.mainGui, text="mouseJump", command=self.mouseJump, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=125, height=16)
        Button(self.mainGui, text="mouseDown", command=self.mouseDown, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=145, height=16)
        Button(self.mainGui, text="mouseUp", command=self.mouseUp, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=165, height=16)        
        Button(self.mainGui, text="stiffMouse", command=self.stiffMouse, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=185, height=16)

        Button(self.mainGui, text="mouseDrag", command=self.mouseDrag, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=105, height=16)
        Button(self.mainGui, text="mouseScroll", command=self.mouseScroll, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=125, height=16)
        Button(self.mainGui, text="mouseClick", command=self.mouseClick, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=145, height=16)
        Button(self.mainGui, text="keyHold", command=self.keyHold, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=165, height=16)
        Button(self.mainGui, text="keyDown", command=self.keyDown, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=185, height=16)

        Button(self.mainGui, text="keyUp", command=self.keyUp, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=105, height=16)
        Button(self.mainGui, text="hotKey", command=self.hotKey, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=125, height=16)
        Button(self.mainGui, text="checkFlag", command=self.checkFlagOnScreen, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=145, height=16)
        Button(self.mainGui, text="checkPixel", command=self.checkPixelOnScreen, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=165, height=16)
        Button(self.mainGui, text="checkRaport", command=self.checkRaport, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=185, height=16)

    def workSpace(self):
        proName = self.projectName

        
        # MISC FUNCTIONS
        self.coords = {'mouseClickButton': 'one', 'mouseClickScr': 'left', 'locateOnScreen': (0,0,0,0) }

        self.locateOnScreenDict = {
                        'Center' : 'Center_NO', 'Flag' : (100, 100), 'GoAnd' : 'GoAnd_Click', 'Wait' : 'Wait_NO',  'Tolerance' : 'Tolerance_90'
                                    }
        self.checkFlagOnScreenDict = {
                        'Command' : 'stop', 'Message' : "message", 'SequenceFile' : "None:///12345667876!@#$%^&*().1234342323fdsfsdfsdfsd", 'Tolerance' : 'Tolerance_90'
                                    }
        self.checkPixelOnScreenDict = {
                        'Command' : 'stop', 'Message' : "message", 'SequenceFile' : "None:///12345667876!@#$%^&*().1234342323fdsfsdfsdfsd", 'Tolerance' : 'Tolerance_90', 'RGB' : (0,0,0), 'Locate' : (100,100)
                                    }
        self.checkRaportDict = {
                        'Dir' : './', 'Raport' : "raport", 'Tolerance' : 'Tolerance_90'
                                    }
        #EDITORS
        self.editorCommand = False
        self.editorLine = ''
        self.fileNameLocateOn = 'flag_id'

        #PLAY EXCALIBURE
        self.playExcalibureLoop = 1

        # Remover Lines
        self.removeLineProject = None
        

        for widgets in self.mainGui.winfo_children():
            widgets.destroy()  
        sScale = 2
        rezW = int(self.sWidth / sScale)
        rezH = int(self.sHeight / sScale - 20)
        
        self.bg_image=Label(self.mainGui, image=self.newScreen, width=rezW, height=rezH) 
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.mainGui, text=" ", font=("Consolas", 36, "bold"), fg="white", bg="#131313", justify="left").place(x=0, y=0, width=2840, height=2460)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#1b1b1b", justify="left").place(x=65, y=100, width=425, height=375)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#1b1b1b", justify="left").place(x=495, y=100, width=400, height=110)

        Label(self.mainGui, text=f"Name of project: {proName}", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=65, y=25, height=20)
        Label(self.mainGui, text=f'dataProjects/{proName}/{proName}.vpc', font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=65, y=45, height=20)
        Label(self.mainGui, text=f"Task list", font=("Consolas", 10, "normal"), fg="#91856c", bg="#131313", justify="left").place(x=65, y=70, height=20)

        # warunek dla insert
        if self.insertCommand == True:
            Label(self.mainGui, text='Insert task into list', font=("Consolas", 10, "normal"), fg="#00edf0", bg="#131313", justify="left").place(x=495, y=70, height=20)
            Button(self.mainGui, text=" Cancel inserting ", command=self.insertCancel, font=("Consolas", 8, "bold"), fg="#91856c", bg="#1b1b1b", bd=0, justify="left").place(x=660, y=70)
        else:
            Label(self.mainGui, text='Add task to list', font=("Consolas", 10, "normal"), fg="#91856c", bg="#131313", justify="left").place(x=495, y=70, height=20)

        V = VD(f'dataProjects/{proName}/{proName}.vpc')
        HEADER = V.header()
        SEP = "</>"
        TITLE = vpc.idSectionBack(HEADER, 1)[0]+" "+vpc.idSectionBack(HEADER, 2)[0]+" "+vpc.idSectionBack(HEADER, 3)[0]
        FLAGS = vpc.idSectionBack(HEADER, 1)[1]+" "+vpc.idSectionBack(HEADER, 2)[1]+"x"+vpc.idSectionBack(HEADER, 3)[1]        
    
        Label(self.mainGui, text=f"(st)HEADER", font=("Consolas", 10, "normal"), fg="#872119", bg="#1b1b1b", justify="left").place(x=65, y=100, height=20)
        self.my_listBoxHeader = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#76af7a", bg="#1b1b1b", justify="left")
        self.my_listBoxHeader.place(x=85, y=125, width=395, height=55)                
        self.my_listBoxHeader.insert(END, TITLE)
        self.my_listBoxHeader.insert(END, FLAGS)

        Button(self.mainGui, text="edit", command=self.editLineProject, font=("Consolas", 8, "normal"), fg="#d2ff00", bg="#1b1b1b", bd=0, justify="left").place(x=450, y=165, height=16)
        Button(self.mainGui, text="insert", command=self.insertLineProject, font=("Consolas", 8, "normal"), fg="#00edf0", bg="#1b1b1b", bd=0, justify="left").place(x=405, y=165, height=16)
        Button(self.mainGui, text="remove", command=self.removerLineProject, font=("Consolas", 8, "normal"), fg="orange", bg="#1b1b1b", bd=0, justify="left").place(x=360, y=165, height=16)

        SEQ = V.proSequence()
        Label(self.mainGui, text=f"(st)SEQUENCES", font=("Consolas", 10, "normal"), fg="#5ea146", bg="#1b1b1b", justify="left").place(x=65, y=165, height=20)
        self.my_listBoxSequence = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 7, "normal"), fg="#648c70", bg="#1b1b1b", justify="left")
        self.my_listBoxSequence.place(x=85, y=185, width=380, height=275)
        
        lenSeq = len(vpc.idSectionBack(SEQ, 1))
        
        if lenSeq > 0:
            for i in range(lenSeq):
                item = vpc.idSectionBack(SEQ, 0)[i]+SEP+vpc.idSectionBack(SEQ, 1)[i]+SEP+vpc.idSectionBack(SEQ, 2)[i]+SEP+vpc.idSectionBack(SEQ, 3)[i]+SEP+vpc.idSectionBack(SEQ, 4)[i]+SEP+vpc.idSectionBack(SEQ, 5)[i]+SEP+vpc.idSectionBack(SEQ, 6)[i]+SEP+vpc.idSectionBack(SEQ, 7)[i]+SEP+vpc.idSectionBack(SEQ, 8)[i]+SEP+vpc.idSectionBack(SEQ, 9)[i]
                self.my_listBoxSequence.insert(END, item)

        Button(self.mainGui, text="exit", command=self.exitProgram, font=("Consolas", 8, "normal"), fg="#3f6a6e", bg="#131313", bd=0, justify="left").place(x=860, y=27, height=20)
        Button(self.mainGui, text="reload", command=self.restart, font=("Consolas", 8, "normal"), fg="#e2cf63", bg="#131313", bd=0, justify="left").place(x=810, y=27, height=20)
        Button(self.mainGui, text="delete", command=self.delProject, font=("Consolas", 8, "normal"), fg="#c65f5f", bg="#131313", bd=0, justify="left").place(x=765, y=27, height=20)
        Button(self.mainGui, text="constructor", command=self.openConstructor, font=("Consolas", 8, "normal"), fg="#e2cf63", bg="#131313", bd=0, justify="left").place(x=690, y=27, height=20)
        Button(self.mainGui, text="play", command=self.playExcalibure, font=("Consolas", 8, "normal"), fg="#84e263", bg="#131313", bd=0, justify="left").place(x=660, y=27, height=20)
            
        Button(self.mainGui, text="osSystem", command=self.osSystem, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=105, height=16)
        Button(self.mainGui, text="SleepNow", command=self.sleepNow, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=125, height=16)
        Button(self.mainGui, text="OnScreen", command=self.locateOnScreen, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=145, height=16)
        Button(self.mainGui, text="DictWrite", command=self.dictWrite, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=165, height=16)
        Button(self.mainGui, text="TypeWrite", command=self.typeWrite, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=185, height=16)

        Button(self.mainGui, text="keyPress", command=self.keyPress, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=105, height=16)
        Button(self.mainGui, text="mouseJump", command=self.mouseJump, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=125, height=16)
        Button(self.mainGui, text="mouseDown", command=self.mouseDown, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=145, height=16)
        Button(self.mainGui, text="mouseUp", command=self.mouseUp, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=165, height=16)        
        Button(self.mainGui, text="stiffMouse", command=self.stiffMouse, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=185, height=16)

        Button(self.mainGui, text="mouseDrag", command=self.mouseDrag, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=105, height=16)
        Button(self.mainGui, text="mouseScroll", command=self.mouseScroll, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=125, height=16)
        Button(self.mainGui, text="mouseClick", command=self.mouseClick, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=145, height=16)
        Button(self.mainGui, text="keyHold", command=self.keyHold, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=165, height=16)
        Button(self.mainGui, text="keyDown", command=self.keyDown, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=185, height=16)

        Button(self.mainGui, text="keyUp", command=self.keyUp, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=105, height=16)
        Button(self.mainGui, text="hotKey", command=self.hotKey, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=125, height=16)
        Button(self.mainGui, text="checkFlag", command=self.checkFlagOnScreen, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=145, height=16)
        Button(self.mainGui, text="checkPixel", command=self.checkPixelOnScreen, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=165, height=16)
        Button(self.mainGui, text="checkRaport", command=self.checkRaport, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=185, height=16)




    def osSystem(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line osSystem", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        self.osSystemCommend = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.osSystemCommend.insert(END, "start ") 
        self.osSystemCommend.place(x=500, y=230, width=395)        
        Button(self.mainGui, text="Try", command=self.osSystemTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Add", command=self.osSystemAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def osSystemTryLine(self):
        prompt = self.osSystemCommend.get()
        proName = self.projectName
        V = VD(f'dataProjects/{proName}/{proName}.vpc')
        SEQ = V.proSequence()
        lenSeq = len(vpc.idSectionBack(SEQ, 1))
        curId = lenSeq + 1
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text=f"s{curId}:#$%^&*(st) osSystem {prompt}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=280, height=20)
        do = f"osSystem|||{prompt}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10"
        vpc.whatNow(do)
        Button(self.mainGui, text="Set again", command=self.osSystem, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Add", command=self.osSystemAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def osSystemAddLine(self):
        if self.editorCommand==True:
            proName = self.projectName
            editLine = self.editorLine
            prompt = self.osSystemCommend.get()

            newLine = f'osSystem|||{prompt}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)
            Label(self.mainGui, text="Edit Line osSystem", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            
            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            prompt = self.osSystemCommend.get()

            newLine = f'osSystem|||{prompt}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            # print(proName, newLine, controlID)
            ev.inserter(proName, newLine, controlID)

            Label(self.mainGui, text="Insert Line osSystem", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            
            Label(self.mainGui, text='The task has been inserted', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            prompt = self.osSystemCommend.get()
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1       
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||osSystem|||{prompt}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) osSystem {prompt}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def sleepNow(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line sleepNow", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        self.sleepNowCommend = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.sleepNowCommend.insert(END, "100")
        self.sleepNowCommend.place(x=500, y=230, width=45)        
        Button(self.mainGui, text="Add", command=self.sleepNowAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)        
        
    def sleepNowAddLine(self):
        if self.editorCommand==True:
            proName = self.projectName
            editLine = self.editorLine
            sleepTime = self.sleepNowCommend.get()

            newLine = f'SleepNow|||{sleepTime}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)

            Label(self.mainGui, text="Edit Line SleepNow", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)    

            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            sleepTime = self.sleepNowCommend.get()

            newLine = f'SleepNow|||{sleepTime}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            # print(proName, newLine, controlID)
            ev.inserter(proName, newLine, controlID)

            Label(self.mainGui, text="Insert Line SleepNow", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            
            Label(self.mainGui, text='The task has been inserted', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            sleepTime = self.sleepNowCommend.get()
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1

            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||SleepNow|||{sleepTime}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) osSystem {sleepTime}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def locateOnScreen(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line locateOnScreen", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)

        Button(self.mainGui, text="Tolerance", command=self.locateOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        Button(self.mainGui, text="Set flag", command=self.locateOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        Button(self.mainGui, text="Go and ..", command=self.locateOnGoTo, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=230, width=95)
        Button(self.mainGui, text="Wait", command=self.locateOnWait, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=230, width=95)

        Button(self.mainGui, text=" ", command=self.locateOnCenterYes, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=650, y=404, width=10, height=10)  
        Label(self.mainGui, text="Capture center", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=670, y=400, width=95)
        Button(self.mainGui, text="Capture", command=self.locateOnScreenPic, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=650, y=420, width=95)

    def locateOnTolerance(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.locateOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)

        if self.locateOnScreenDict['Tolerance'] == 'Tolerance_100':
            Button(self.mainGui, text="100%", command=self.locateOnTolerance100, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=252, width=95)
        else: Button(self.mainGui, text="100%", command=self.locateOnTolerance100, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=252, width=95)

        if self.locateOnScreenDict['Tolerance'] == 'Tolerance_90':    
            Button(self.mainGui, text="90%", command=self.locateOnTolerance90, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=274, width=95)
        else: Button(self.mainGui, text="90%", command=self.locateOnTolerance90, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=274, width=95)

        if self.locateOnScreenDict['Tolerance'] == 'Tolerance_80':    
            Button(self.mainGui, text="80%", command=self.locateOnTolerance80, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=296, width=95)
        else: Button(self.mainGui, text="80%", command=self.locateOnTolerance80, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=296, width=95)

        if self.locateOnScreenDict['Tolerance'] == 'Tolerance_70':    
            Button(self.mainGui, text="70%", command=self.locateOnTolerance70, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=318, width=95)
        else: Button(self.mainGui, text="70%", command=self.locateOnTolerance70, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=318, width=95)

        if self.locateOnScreenDict['Tolerance'] == 'Tolerance_50':    
            Button(self.mainGui, text="50%", command=self.locateOnTolerance50, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=340, width=95)
        else: Button(self.mainGui, text="50%", command=self.locateOnTolerance50, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=340, width=95)

        if self.locateOnScreenDict['Tolerance'] == 'Tolerance_30':    
            Button(self.mainGui, text="30%", command=self.locateOnTolerance30, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=362, width=95)
        else: Button(self.mainGui, text="30%", command=self.locateOnTolerance30, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=362, width=95)

    def locateOnTolerance100(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.locateOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.locateOnScreenDict['Tolerance']='Tolerance_100'        
    def locateOnTolerance90(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.locateOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.locateOnScreenDict['Tolerance']='Tolerance_90'        
    def locateOnTolerance80(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.locateOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.locateOnScreenDict['Tolerance']='Tolerance_80'        
    def locateOnTolerance70(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.locateOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.locateOnScreenDict['Tolerance']='Tolerance_70'        
    def locateOnTolerance50(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.locateOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.locateOnScreenDict['Tolerance']='Tolerance_50'        
    def locateOnTolerance30(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.locateOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.locateOnScreenDict['Tolerance']='Tolerance_30'        

    def locateOnFlag(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Set flag", command=self.locateOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)

        if self.locateOnScreenDict['Flag'] == (250,250):
            Button(self.mainGui, text="250x250", command=self.locateOnFlag250250, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=252, width=95)
        else: Button(self.mainGui, text="250x250", command=self.locateOnFlag250250, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=252, width=95)

        if self.locateOnScreenDict['Flag'] == (150,150):    
            Button(self.mainGui, text="150x150", command=self.locateOnFlag150150, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=274, width=95)
        else: Button(self.mainGui, text="150x150", command=self.locateOnFlag150150, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=274, width=95)

        if self.locateOnScreenDict['Flag'] == (100,100):    
            Button(self.mainGui, text="100x100", command=self.locateOnFlag100100, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=296, width=95)
        else: Button(self.mainGui, text="100x100", command=self.locateOnFlag100100, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=296, width=95)

        if self.locateOnScreenDict['Flag'] == (50,50):    
            Button(self.mainGui, text="50x50", command=self.locateOnFlag5050, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=318, width=95)
        else: Button(self.mainGui, text="50x50", command=self.locateOnFlag5050, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=318, width=95)

        if self.locateOnScreenDict['Flag'] == (30,30):    
            Button(self.mainGui, text="30x30", command=self.locateOnFlag3030, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=340, width=95)
        else: Button(self.mainGui, text="30x30", command=self.locateOnFlag3030, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=340, width=95)

        if self.locateOnScreenDict['Flag'] == (10,10):    
            Button(self.mainGui, text="10x10", command=self.locateOnFlag1010, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=362, width=95)
        else: Button(self.mainGui, text="10x10", command=self.locateOnFlag1010, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=362, width=95)

    def locateOnFlag250250(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Set flag", command=self.locateOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        self.locateOnScreenDict['Flag']=(250,250) 
    def locateOnFlag150150(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Set flag", command=self.locateOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        self.locateOnScreenDict['Flag']=(150,150) 
    def locateOnFlag100100(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Set flag", command=self.locateOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        self.locateOnScreenDict['Flag']=(100,100) 
    def locateOnFlag5050(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Set flag", command=self.locateOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        self.locateOnScreenDict['Flag']=(50,50) 
    def locateOnFlag3030(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Set flag", command=self.locateOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        self.locateOnScreenDict['Flag']=(30,30)      
    def locateOnFlag1010(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Set flag", command=self.locateOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        self.locateOnScreenDict['Flag']=(10,10) 

    def locateOnGoTo(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=252, width=95, height=135)
        Button(self.mainGui, text="Go and ..", command=self.locateOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=230, width=95)

        if self.locateOnScreenDict['GoAnd'] == 'GoAnd_Click':
            Button(self.mainGui, text="Click", command=self.locateOnFlagClick, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=700, y=252, width=95)
        else: Button(self.mainGui, text="Click", command=self.locateOnFlagClick, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=700, y=252, width=95)

        if self.locateOnScreenDict['GoAnd'] == 'GoAnd_DoubleClick':    
            Button(self.mainGui, text="DoubleClick", command=self.locateOnFlagDoubleClick, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=700, y=274, width=95)
        else: Button(self.mainGui, text="DoubleClick", command=self.locateOnFlagDoubleClick, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=700, y=274, width=95)

        if self.locateOnScreenDict['GoAnd'] == 'GoTo_moveTo':    
            Button(self.mainGui, text="JustMove", command=self.locateOnFlagJustMove, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=700, y=296, width=95)
        else: Button(self.mainGui, text="JustMove", command=self.locateOnFlagJustMove, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=700, y=296, width=95)

        tol = str(self.locateOnScreenDict['Tolerance']);flg = str(self.locateOnScreenDict['Flag']);gan = str(self.locateOnScreenDict['GoAnd']);wai = str(self.locateOnScreenDict['Wait'])
        Label(self.mainGui, text=f"T: {tol}, F: {flg}, G: {gan}, W: {wai}", font=("Consolas", 10, "normal"), fg="gray", bg="#131313", justify="left").place(x=500, y=455)

    def locateOnFlagClick(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=252, width=95, height=135)
        Button(self.mainGui, text="Go and ..", command=self.locateOnGoTo, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=230, width=95)
        self.locateOnScreenDict['GoAnd']='GoAnd_Click'
    def locateOnFlagDoubleClick(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=252, width=95, height=135)
        Button(self.mainGui, text="Go and ..", command=self.locateOnGoTo, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=230, width=95)
        self.locateOnScreenDict['GoAnd']='GoAnd_DoubleClick'
    def locateOnFlagJustMove(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=252, width=95, height=135)
        Button(self.mainGui, text="Go and ..", command=self.locateOnGoTo, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=230, width=95)
        self.locateOnScreenDict['GoAnd']='GoTo_moveTo'
 
    def locateOnWait(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=800, y=252, width=95, height=135)
        Button(self.mainGui, text="Wait", command=self.locateOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=230, width=95)

        if self.locateOnScreenDict['Wait'] == 'Wait_NO':
            Button(self.mainGui, text="No", command=self.locateOnWaitNo, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=800, y=252, width=95)
        else: Button(self.mainGui, text="No", command=self.locateOnWaitNo, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=800, y=252, width=95)

        if self.locateOnScreenDict['Wait'] == 'Wait_YES':    
            Button(self.mainGui, text="Yes", command=self.locateOnWaitYes, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=800, y=274, width=95)
        else: Button(self.mainGui, text="Yes", command=self.locateOnWaitYes, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=800, y=274, width=95)

        tol = str(self.locateOnScreenDict['Tolerance']);flg = str(self.locateOnScreenDict['Flag']);gan = str(self.locateOnScreenDict['GoAnd']);wai = str(self.locateOnScreenDict['Wait'])
        Label(self.mainGui, text=f"T: {tol}, F: {flg}, G: {gan}, W: {wai}", font=("Consolas", 10, "normal"), fg="gray", bg="#131313", justify="left").place(x=500, y=455)       

    def locateOnWaitNo(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=800, y=252, width=95, height=135)
        Button(self.mainGui, text="Wait", command=self.locateOnWait, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=230, width=95)
        self.locateOnScreenDict['Wait']='Wait_NO'
    def locateOnWaitYes(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=800, y=252, width=95, height=135)
        Button(self.mainGui, text="Wait", command=self.locateOnWait, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=230, width=95)
        self.locateOnScreenDict['Wait']='Wait_YES'

    def locateOnCenterNo(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=800, y=252, width=95, height=135)
        Button(self.mainGui, text=" ", command=self.locateOnCenterYes, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=650, y=404, width=10, height=10)
        self.locateOnScreenDict['Center']='Center_NO'
       
    def locateOnCenterYes(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=800, y=252, width=95, height=135)
        Button(self.mainGui, text=" ", command=self.locateOnCenterNo, font=("Consolas", 9, "normal"), fg="gray", bg="white", bd=0, justify="left").place(x=650, y=404, width=10, height=10)
        self.locateOnScreenDict['Center']='Center_YES'

    def locateOnScreenPic(self):
        ia=99
        for i in range(100):
            ix = ia / 100
            self.root.attributes('-alpha', ix)
            time.sleep(0.006)
            ia -= 1
        sleep(1)

        pro = str(self.projectName)
        ce = str(self.locateOnScreenDict['Center'])
        flaX = str(self.locateOnScreenDict['Flag'][0])
        flaY = str(self.locateOnScreenDict['Flag'][1])
        wait = str(self.locateOnScreenDict['Wait'])
        goTo = str(self.locateOnScreenDict['GoAnd'])
        tol = str(self.locateOnScreenDict['Tolerance'])
        flagId = str(self.fileNameLocateOn)
        if self.editorCommand==True:
            newLine = self.editorLine
            seqLO = str(f'LocateOnScreen|||{ce}|||{flagId}|||{flaX}|||{flaY}|||{wait}|||{goTo}|||{tol}|||{newLine}') 
        
            os.system(f'start python ctf.py -p "{pro}" -s "{seqLO}" -e True')
            sys.exit()
        elif self.insertCommand == True:           
            controlID = self.insertbeforeLine

            seqLO = str(f'LocateOnScreen|||{ce}|||flag_id.png|||{flaX}|||{flaY}|||{wait}|||{goTo}|||{tol}|||{controlID}') 
            os.system(f'start python ctf.py -p "{pro}" -s "{seqLO}" -e InsertTrue')
            self.insertCommand = False
            self.insertbeforeLine = ''
            sys.exit()     
        else:     
            seqLO = str(f'LocateOnScreen|||{ce}|||flag_id.png|||{flaX}|||{flaY}|||{wait}|||{goTo}|||{tol}|||TAB10')               
            os.system(f'start python ctf.py -p "{pro}" -s "{seqLO}"')
            sys.exit()

    def dictWrite(self):
        if self.editorCommand==True:           

            browse_text = StringVar()
            browse_text.set("Browse")
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=440, height=258)        
            Label(self.mainGui, text="Edit Line dictWrite to typeWrite", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Button(self.mainGui, textvariable=browse_text, command=lambda:dictWriteEditFile(), font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=230, width=95, height=20)

        else:
            V = VD(f'dataProjects/{self.projectName}/{self.projectName}.vpc');PRO = V.proGeneral();lenPRO = len(vpc.idSectionBack(PRO, 1))
            if lenPRO > 3:            
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
                Label(self.mainGui, text='The maximum file quantity for the project', font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=255, height=20)
                Button(self.mainGui, text="Try again", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            else:
                browse_text = StringVar()
                browse_text.set("Browse")
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=440, height=258)        
                Label(self.mainGui, text="Task Line dictWrite to typeWrite", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                Button(self.mainGui, textvariable=browse_text, command=lambda:dictWriteopenFile(), font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=230, width=95, height=20)

        def dictWriteEditFile():
            editorLine = str(self.editorLine)
            splEditorLine = editorLine.split('</>')
            
            browse_text.set("Selecting ...")
            file = askopenfile(parent=self.mainGui, mode='rb', title="Choice dict file", filetype=[("Text file", "*.txt")])            
            if file:
                kk=str(file)
                tt = kk.split(' ')
                uu = str(tt[1])
                jj = uu.split("""'""")
                pathDict = jj[1]                 
                source = str(pathDict)
                yy = source.split('/')
                for y in yy:
                    if y.endswith('.txt'):
                        fileName=y                        
                    else:
                        fileName=None
                if fileName!=None: 
                    directory=f'./dataProjects/{self.projectName}/'
                    
                    fileGood=False
                    for f in os.listdir(directory):    
                        if os.path.isfile(directory+f):          
                            if fileName==f:
                                fileGood=True

                    if splEditorLine[2]==fileName:
                        fileGood=False
                    else:
                        os.remove(directory+splEditorLine[2])

                    if fileGood:
                        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
                        Label(self.mainGui, text='A file with the given name is already loaded into \nthe project directory', font=("Consolas", 10, "normal"), fg="orange", bg="#131313", justify="left").place(x=495, y=225)
                        Button(self.mainGui, text="Try again", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
                    else:
                        browse_text.set("Loading ...")                    
                        target = f"./dataProjects/{self.projectName}/{fileName}"
                        try:
                            copyfile(source, target)
                            proName = self.projectName
                            editLine = self.editorLine

                            newLine = f'DictWrite|||{fileName}|||TypeWrite|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
                            ev.editor(proName, editLine, newLine)
                            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                          
                            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
                            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
                            self.editorCommand=False
                            self.editorLine=''                                                             
                        except:
                            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
                            Label(self.mainGui, text='Something gone wrong', font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=255, height=20)
                            Button(self.mainGui, text="Try again", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
                            self.editorCommand=False
                            self.editorLine=''

                              

        def dictWriteopenFile():           
            V = VD(f'dataProjects/{self.projectName}/{self.projectName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            PRO = V.proGeneral()
            lenPRO = len(vpc.idSectionBack(PRO, 1))
            browse_text.set("Selecting ...")
            file = askopenfile(parent=self.mainGui, mode='rb', title="Choice dict file", filetype=[("Text file", "*.txt")])
            if file:
                kk=str(file)
                tt = kk.split(' ')
                uu = str(tt[1])
                jj = uu.split("""'""")
                pathDict = jj[1]                 
                source = str(pathDict)
                yy = source.split('/')
                for y in yy:
                    if y.endswith('.txt'):
                        browse_text.set("Loading ...")
                        fileName = y
                        target = f"./dataProjects/{self.projectName}/{fileName}"
                    else:
                        fileName=None
                if fileName!=None:
                    directory=f'./dataProjects/{self.projectName}/'
                    fileGood=False
                    for f in os.listdir(directory):    
                        if os.path.isfile(directory+f):          
                            if fileName==f:
                                fileGood=True
                    if fileGood:
                        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
                        Label(self.mainGui, text='A file with the given name is already loaded into \nthe project directory', font=("Consolas", 10, "normal"), fg="orange", bg="#131313", justify="left").place(x=495, y=225)
                        Button(self.mainGui, text="Try again", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
                    else:
                        try:                            
                            if self.insertCommand == True:
                                proName = self.projectName
                                controlID = self.insertbeforeLine

                                newLine = f'DictWrite|||{fileName}|||TypeWrite|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
                                
                                ev.inserter(proName, newLine, controlID)

                                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                                Label(self.mainGui, text=f"DictWrite {fileName} TypeWrite", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
                                Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
                                Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

                                self.insertCommand = False
                                self.insertbeforeLine = ''
                            else:
                                curId = lenSeq + 1
                                f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
                                f.write(f's{curId}:#$%^&*(st)|||DictWrite|||{fileName}|||TypeWrite|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')                        
                                f.close()
                                
                                curGId = lenPRO + 1
                                f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
                                f.write(f'g{curGId}:#$%^&*(gg)|||DictWrite|||{fileName}|||TypeWrite|||s{curId}:#$%^&*(st)|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')                        
                                f.close()

                                copyfile(source, target)
                                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                                Label(self.mainGui, text=f"s{curId}:#$%^&*(gg) DictWrite {fileName} TypeWrite", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
                                Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
                                Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
                        except:
                            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
                            Label(self.mainGui, text='Something gone wrong', font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=255, height=20)
                            Button(self.mainGui, text="Try again", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
                    
 
    def typeWrite(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line typeWrite", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        self.typeWriteCommend = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.typeWriteCommend.insert(END, "hello world")
        self.typeWriteCommend.place(x=500, y=230, width=395)        
        Button(self.mainGui, text="Try", command=self.typeWriteTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Add", command=self.typeWriteAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def typeWriteTryLine(self):
        typeW = self.typeWriteCommend.get()
        proName = self.projectName
        V = VD(f'dataProjects/{proName}/{proName}.vpc')
        SEQ = V.proSequence()
        lenSeq = len(vpc.idSectionBack(SEQ, 1))
        curId = lenSeq + 1
         
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Testing typeWrite", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=395) 
        Label(self.mainGui, text=f"s{curId}:#$%^&*(st) typeWrite {typeW}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=280, height=20)        
        Button(self.mainGui, text="Set again", command=self.typeWrite, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Add", command=self.typeWriteAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
        
        pa.move(0,-23)
        pa.click(button='left')           
        pa.click(button='left')           
        pa.click(button='left')         
        do = f"typeWrite|||{typeW}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10"
        vpc.whatNow(do)

    def typeWriteAddLine(self):
        if self.editorCommand==True:
            proName = self.projectName
            editLine = self.editorLine
            typeW = self.typeWriteCommend.get()

            newLine = f'typeWrite|||{typeW}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)
            Label(self.mainGui, text="Edit Line osSystem", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            
            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            typeW = self.typeWriteCommend.get()

            newLine = f'typeWrite|||{typeW}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"typeWrite {typeW}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.insertCommand = False
            self.insertbeforeLine = ''

        else:
            typeW = self.typeWriteCommend.get()
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1       

            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||typeWrite|||{typeW}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) typeWrite {typeW}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def mouseJump(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseJump", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text="x", font=("Consolas", 10, "normal"), fg="gray", bg="#131313", justify="left").place(x=550, y=228, height=20)
        self.sleepmouseJumpX = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.sleepmouseJumpX.insert(END, "1")
        self.sleepmouseJumpX.place(x=500, y=230, width=45)        
        self.sleepmouseJumpY = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.sleepmouseJumpY.insert(END, "1")
        self.sleepmouseJumpY.place(x=570, y=230, width=45)       
        Button(self.mainGui, text="Try", command=self.mouseJumpTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Add", command=self.mouseJumpAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
            
    def mouseJumpTryLine(self):
        jumpX = self.sleepmouseJumpX.get()
        jumpY = self.sleepmouseJumpY.get()
        proName = self.projectName
        V = VD(f'dataProjects/{proName}/{proName}.vpc')
        SEQ = V.proSequence()
        lenSeq = len(vpc.idSectionBack(SEQ, 1))
        curId = lenSeq + 1
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseJump", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text=f"s{curId}:#$%^&*(st) mouseJump {jumpX} x {jumpY}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=280, height=20)
        do = f"mouseJump|||{jumpX}|||{jumpY}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10"
        vpc.whatNow(do)
        Button(self.mainGui, text="Set again", command=self.mouseJump, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Add", command=self.mouseJumpAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
                    
    def mouseJumpAddLine(self):
        if self.editorCommand==True:
            proName = self.projectName
            editLine = self.editorLine
            jumpX = self.sleepmouseJumpX.get()
            jumpY = self.sleepmouseJumpY.get()

            newLine = f'mouseJump|||{jumpX}|||{jumpY}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)

            Label(self.mainGui, text="Edit Line mouseJump", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)    

            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.editorCommand=False
            self.editorLine=''
            
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            jumpX = self.sleepmouseJumpX.get()
            jumpY = self.sleepmouseJumpY.get()

            newLine = f'mouseJump|||{jumpX}|||{jumpY}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"mouseJump {jumpX} x {jumpY}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)


            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            jumpX = self.sleepmouseJumpX.get()
            jumpY = self.sleepmouseJumpY.get()
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||mouseJump|||{jumpX}|||{jumpY}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) mouseJump {jumpX} x {jumpY}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def mouseDown(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseDown", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)        
        Button(self.mainGui, text="Left", command=self.mouseDownSetLeft, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45)        
        Button(self.mainGui, text="Middle", command=self.mouseDownSetMiddle, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=552, y=228, width=45)   
        Button(self.mainGui, text="Right", command=self.mouseDownSetRight, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=604, y=228, width=45)
        # Button(self.mainGui, text="Add", command=self.mouseDownAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
  
    def mouseDownSetLeft(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseDown", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text="Left", font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45) 
        self.mouseDownButton = 'left'
        Button(self.mainGui, text="Add", command=self.mouseDownAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Cancel", command=self.mouseDown, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def mouseDownSetMiddle(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseDown", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text="Middle", font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45) 
        self.mouseDownButton = 'middle'
        Button(self.mainGui, text="Add", command=self.mouseDownAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Cancel", command=self.mouseDown, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def mouseDownSetRight(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseDown", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text="Right", font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45) 
        self.mouseDownButton = 'right'
        Button(self.mainGui, text="Add", command=self.mouseDownAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Cancel", command=self.mouseDown, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def mouseDownAddLine(self):
        if self.editorCommand==True:
            proName = self.projectName
            editLine = self.editorLine            
            mouseButton =  self.mouseDownButton

            newLine = f'mouseDown|||{mouseButton}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)

            Label(self.mainGui, text="Edit Line mouseDown", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)    

            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            mouseButton = self.mouseDownButton

            newLine = f'mouseDown|||{mouseButton}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"mouseDown {mouseButton}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)


            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            mouseButton = self.mouseDownButton
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||mouseDown|||{mouseButton}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) mouseDown {mouseButton}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def mouseUp(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseUp", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)        
        Button(self.mainGui, text="Left", command=self.mouseUpSetLeft, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45)        
        Button(self.mainGui, text="Middle", command=self.mouseUpSetMiddle, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=552, y=228, width=45)   
        Button(self.mainGui, text="Right", command=self.mouseUpSetRight, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=604, y=228, width=45)
  
    def mouseUpSetLeft(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseUp", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text="Left", font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45) 
        self.mouseUpButton = 'left'
        Button(self.mainGui, text="Add", command=self.mouseUpAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Cancel", command=self.mouseUp, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def mouseUpSetMiddle(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseUp", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text="Middle", font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45) 
        self.mouseUpButton = 'middle'
        Button(self.mainGui, text="Add", command=self.mouseUpAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Cancel", command=self.mouseUp, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def mouseUpSetRight(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseUp", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text="Right", font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45) 
        self.mouseUpButton = 'right'
        Button(self.mainGui, text="Add", command=self.mouseUpAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Cancel", command=self.mouseUp, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def mouseUpAddLine(self):
        if self.editorCommand==True:
            proName = self.projectName
            editLine = self.editorLine            
            mouseButton =  self.mouseUpButton
            
            newLine = f'mouseUp|||{mouseButton}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)

            Label(self.mainGui, text="Edit Line mouseUp", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)    

            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            mouseButton =  self.mouseUpButton

            newLine = f'mouseUp|||{mouseButton}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"mouseUp {mouseButton}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            mouseButton =  self.mouseUpButton
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||mouseUp|||{mouseButton}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) mouseUp {mouseButton}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def stiffMouse(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line stiffMouse", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text="x", font=("Consolas", 10, "normal"), fg="gray", bg="#131313", justify="left").place(x=550, y=228, height=20)
        self.stiffMouseX = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.stiffMouseX.insert(END, "1")
        self.stiffMouseX.place(x=500, y=230, width=45)        
        self.stiffMouseY = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.stiffMouseY.insert(END, "1")
        self.stiffMouseY.place(x=570, y=230, width=45)       
        Button(self.mainGui, text="Try", command=self.stiffMouseTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Add", command=self.stiffMouseAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
            
    def stiffMouseTryLine(self):
        stiffX = self.stiffMouseX.get()
        stiffY = self.stiffMouseY.get()
        proName = self.projectName
        V = VD(f'dataProjects/{proName}/{proName}.vpc')
        SEQ = V.proSequence()
        lenSeq = len(vpc.idSectionBack(SEQ, 1))
        curId = lenSeq + 1
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line stiffMouse", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text=f"s{curId}:#$%^&*(st) mouseJump {stiffX} x {stiffY}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=280, height=20)
        do = f"stiffMouse|||{stiffX}|||{stiffY}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10"
        vpc.whatNow(do)
        Button(self.mainGui, text="Set again", command=self.stiffMouse, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Add", command=self.stiffMouseAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
                    
    def stiffMouseAddLine(self):
        if self.editorCommand==True:
            proName = self.projectName
            editLine = self.editorLine            
            stiffX = self.stiffMouseX.get()
            stiffY = self.stiffMouseY.get()
            
            newLine = f'stiffMouse|||{stiffX}|||{stiffY}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)

            Label(self.mainGui, text="Edit Line stiffMouse", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)    

            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            stiffX = self.stiffMouseX.get()
            stiffY = self.stiffMouseY.get()

            newLine = f'stiffMouse|||{stiffX}|||{stiffY}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"stiffMouse {stiffX} x {stiffY}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            stiffX = self.stiffMouseX.get()
            stiffY = self.stiffMouseY.get()
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||stiffMouse|||{stiffX}|||{stiffY}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) stiffMouse {stiffX} x {stiffY}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def mouseDrag(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseDrag", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text="x", font=("Consolas", 10, "normal"), fg="gray", bg="#131313", justify="left").place(x=550, y=228, height=20)
        self.sleepmouseDragX = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.sleepmouseDragX.insert(END, "-100")
        self.sleepmouseDragX.place(x=500, y=230, width=45)        
        self.sleepmouseDragY = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.sleepmouseDragY.insert(END, "100")
        self.sleepmouseDragY.place(x=570, y=230, width=45)  
        self.sleepmouseDragS = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.sleepmouseDragS.insert(END, "100")
        self.sleepmouseDragS.place(x=640, y=230, width=45)       
        Button(self.mainGui, text="Try", command=self.mouseDragTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Add", command=self.mouseDragAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
            
    def mouseDragTryLine(self):
        jumpX = self.sleepmouseDragX.get()
        jumpY = self.sleepmouseDragY.get()
        jumpS = self.sleepmouseDragS.get()
        proName = self.projectName
        V = VD(f'dataProjects/{proName}/{proName}.vpc')
        SEQ = V.proSequence()
        lenSeq = len(vpc.idSectionBack(SEQ, 1))
        curId = lenSeq + 1
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line osSystem", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text=f"s{curId}:#$%^&*(st) mouseDrag {jumpX} x {jumpY} cs:{jumpS}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=280, height=20)
        do = f"mouseDrag|||{jumpX}|||{jumpY}|||{jumpS}|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10"
        vpc.whatNow(do)
        Button(self.mainGui, text="Set again", command=self.mouseDrag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Add", command=self.mouseDragAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
                    
    def mouseDragAddLine(self):
        if self.editorCommand==True:
            proName = self.projectName
            editLine = self.editorLine            
            jumpX = self.sleepmouseDragX.get()
            jumpY = self.sleepmouseDragY.get()
            jumpS = self.sleepmouseDragS.get()
            
            newLine = f'mouseDrag|||{jumpX}|||{jumpY}|||{jumpS}|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)

            Label(self.mainGui, text="Edit Line mouseDrag", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)    

            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            jumpX = self.sleepmouseDragX.get()
            jumpY = self.sleepmouseDragY.get()
            jumpS = self.sleepmouseDragS.get()

            newLine = f'mouseDrag|||{jumpX}|||{jumpY}|||{jumpS}|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"mouseDrag {jumpX} x {jumpY} cs: {jumpS}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.insertCommand = False
            self.insertbeforeLine = ''

        else:
            jumpX = self.sleepmouseDragX.get()
            jumpY = self.sleepmouseDragY.get()
            jumpS = self.sleepmouseDragS.get()
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||mouseDrag|||{jumpX}|||{jumpY}|||{jumpS}|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) mouseDrag {jumpX} x {jumpY} cs: {jumpS}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def mouseClick(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseClick", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Button(self.mainGui, text="Left", command=self.mouseClickSetLeft, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=45)        
        Button(self.mainGui, text="Middle", command=self.mouseClickSetMiddle, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=552, y=250, width=45)   
        Button(self.mainGui, text="Right", command=self.mouseClickSetRight, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=604, y=250, width=45)

    def mouseClickSetLeft(self):        
        self.mouseClickButton = self.coords["mouseClickButton"]='left'
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseClick", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20) 
        Label(self.mainGui, text="Left", font=("Consolas", 8, "normal"), fg="white", bg="#1c1c1c", bd=0, justify="left").place(x=500, y=250, width=45)  
        Button(self.mainGui, text="One", command=self.mouseClickSetone, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45)        
        Button(self.mainGui, text="Double", command=self.mouseClickSetDouble, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=552, y=228, width=45)   
        Button(self.mainGui, text="Triple", command=self.mouseClickSetTriple, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=604, y=228, width=45)   
        Button(self.mainGui, text="Cancel", command=self.mouseClick, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=268, width=95)

    def mouseClickSetMiddle(self):
        self.mouseClickButton = self.coords["mouseClickButton"]='middle'
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseClick", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20) 
        Label(self.mainGui, text="Middle", font=("Consolas", 8, "normal"), fg="white", bg="#1c1c1c", bd=0, justify="left").place(x=500, y=250, width=45)  
        Button(self.mainGui, text="One", command=self.mouseClickSetone, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45)        
        Button(self.mainGui, text="Double", command=self.mouseClickSetDouble, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=552, y=228, width=45)   
        Button(self.mainGui, text="Triple", command=self.mouseClickSetTriple, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=604, y=228, width=45)   
        Button(self.mainGui, text="Cancel", command=self.mouseClick, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=268, width=95)

    def mouseClickSetRight(self):
        self.mouseClickButton = self.coords["mouseClickButton"]='right'
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseClick", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20) 
        Label(self.mainGui, text="Right", font=("Consolas", 8, "normal"), fg="white", bg="#1c1c1c", bd=0, justify="left").place(x=500, y=250, width=45)  
        Button(self.mainGui, text="One", command=self.mouseClickSetone, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45)        
        Button(self.mainGui, text="Double", command=self.mouseClickSetDouble, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=552, y=228, width=45)   
        Button(self.mainGui, text="Triple", command=self.mouseClickSetTriple, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=604, y=228, width=45)   
        Button(self.mainGui, text="Cancel", command=self.mouseClick, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=268, width=95)

    def mouseClickSetone(self):
        self.mouseClickScr = self.coords["mouseClickScr"]='one' 
        mouseClickButton = self.coords['mouseClickButton']

        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseClick", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text=f"One {mouseClickButton}", font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228)         
        Button(self.mainGui, text="Add", command=self.mouseClickAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Cancel", command=self.mouseClick, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def mouseClickSetDouble(self):
        self.mouseClickScr = self.coords["mouseClickScr"]='double' 
        mouseClickButton = self.coords['mouseClickButton']

        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseClick", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text=f"Double {mouseClickButton}", font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228)         
        Button(self.mainGui, text="Add", command=self.mouseClickAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Cancel", command=self.mouseClick, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def mouseClickSetTriple(self):
        self.mouseClickScr = self.coords["mouseClickScr"]='triple' 
        mouseClickButton = self.coords['mouseClickButton']

        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseClick", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text=f"Triple {mouseClickButton}", font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228)         
        Button(self.mainGui, text="Add", command=self.mouseClickAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Cancel", command=self.mouseClick, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def mouseClickAddLine(self):        
        if self.editorCommand==True:            
            proName = self.projectName
            editLine = self.editorLine
            mouseClickScr = self.coords['mouseClickScr']
            mouseButton =  self.coords['mouseClickButton']
            newLine = f'mouseClick|||{mouseClickScr}|||{mouseButton}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)
            Label(self.mainGui, text="Edit Line mouseClick", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            
            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            mouseClickScr = self.coords['mouseClickScr']
            mouseButton =  self.coords['mouseClickButton']

            newLine = f'mouseClick|||{mouseClickScr}|||{mouseButton}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"mouseClick {mouseClickScr} {mouseButton}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            proName = self.projectName
            mouseClickScr = self.coords['mouseClickScr']
            mouseButton =  self.coords['mouseClickButton']
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1                
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||mouseClick|||{mouseClickScr}|||{mouseButton}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()

            Label(self.mainGui, text="Task Line mouseClick", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) mouseClick {mouseClickScr} {mouseButton}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def mouseScroll(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line mouseScroll", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        
        self.sleepmouseScrollS = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.sleepmouseScrollS.insert(END, "300")
        self.sleepmouseScrollS.place(x=500, y=230, width=45)                  
        
        Button(self.mainGui, text="Add", command=self.mouseScrollAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
                    
    def mouseScrollAddLine(self):
        if self.editorCommand==True:            
            proName = self.projectName
            editLine = self.editorLine
            jumpS = self.sleepmouseScrollS.get()

            newLine = f'mouseScroll|||{jumpS}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)
            Label(self.mainGui, text="Edit Line mouseScroll", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            
            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            jumpS = self.sleepmouseScrollS.get()

            newLine = f'mouseScroll|||{jumpS}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"mouseScroll {jumpS}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            jumpS = self.sleepmouseScrollS.get()
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1

            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||mouseScroll|||{jumpS}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) mouseScroll {jumpS}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def keyPress(self):
        buttonKeys = vpc.tableChar()

        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line keyPress", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)

        self.my_listKeys = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 24, "normal"), fg="#6c7692", bg="#1b1b1b", justify="center")
        self.my_listKeys.place(x=495, y=230, width=400, height=210)

        for i in buttonKeys:            
            self.my_listKeys.insert(END, i)

        Button(self.mainGui, text="Add", command=self.keyPressAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=450, width=95)   

    def keyPressAddLine(self): 
        if self.editorCommand==True:            
            proName = self.projectName
            editLine = self.editorLine
            keyPRESS = self.my_listKeys.get(ANCHOR)

            newLine = f'keyPress|||{keyPRESS}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)
            Label(self.mainGui, text="Edit Line keyPress", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            
            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            keyPRESS = self.my_listKeys.get(ANCHOR)

            newLine = f'keyPress|||{keyPRESS}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"keyPress {keyPRESS}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.insertCommand = False
            self.insertbeforeLine = ''
        
        else:
            keyPRESS = self.my_listKeys.get(ANCHOR)
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1

            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||keyPress|||{keyPRESS}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) keyPress {keyPRESS}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def hotKey(self):
        pass

    def keyHold(self):
        buttonKeys = vpc.tableChar()
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line keyHold", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        self.my_listHoldKeys = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 24, "normal"), fg="#6c7692", bg="#1b1b1b", justify="center")
        self.my_listHoldKeys.place(x=495, y=230, width=400, height=210)
        for i in buttonKeys:            
            self.my_listHoldKeys.insert(END, i)
        Button(self.mainGui, text="Add", command=self.keyHoldAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=450, width=95)   

    def keyHoldAddLine(self): 
        if self.editorCommand==True:            
            proName = self.projectName
            editLine = self.editorLine
            keyHold = self.my_listHoldKeys.get(ANCHOR)

            newLine = f'keyHold|||{keyHold}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)
            Label(self.mainGui, text="Edit Line keyPress", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            
            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            keyHold = self.my_listHoldKeys.get(ANCHOR)

            newLine = f'keyHold|||{keyHold}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"keyHold {keyHold}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            keyHold = self.my_listHoldKeys.get(ANCHOR)
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||keyHold|||{keyHold}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) keyHold {keyHold}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def keyDown(self):
        buttonKeys = vpc.tableChar()
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line keyDown", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        self.my_listkeyDown = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 24, "normal"), fg="#6c7692", bg="#1b1b1b", justify="center")
        self.my_listkeyDown.place(x=495, y=230, width=400, height=210)
        for i in buttonKeys:            
            self.my_listkeyDown.insert(END, i)
        Button(self.mainGui, text="Add", command=self.keyDownAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=450, width=95)   

    def keyDownAddLine(self): 
        if self.editorCommand==True:            
            proName = self.projectName
            editLine = self.editorLine
            keyDown = self.my_listkeyDown.get(ANCHOR)

            newLine = f'keyDown|||{keyDown}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)
            Label(self.mainGui, text="Edit Line keyPress", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            
            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            keyDown = self.my_listkeyDown.get(ANCHOR)

            newLine = f'keyDown|||{keyDown}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"keyDown {keyDown}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            keyDown = self.my_listkeyDown.get(ANCHOR)
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||keyDown|||{keyDown}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) keyDown {keyDown}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
                
    def keyUp(self):
        buttonKeys = vpc.tableChar()
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line keyUp", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        self.my_listkeyUp = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 24, "normal"), fg="#6c7692", bg="#1b1b1b", justify="center")
        self.my_listkeyUp.place(x=495, y=230, width=400, height=210)
        for i in buttonKeys:            
            self.my_listkeyUp.insert(END, i)
        Button(self.mainGui, text="Add", command=self.keyUpAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=450, width=95)   

    def keyUpAddLine(self): 
        if self.editorCommand==True:            
            proName = self.projectName
            editLine = self.editorLine
            keyUp = self.my_listkeyUp.get(ANCHOR)

            newLine = f'keyUp|||{keyUp}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            ev.editor(proName, editLine, newLine)
            Label(self.mainGui, text="Edit Line keyPress", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            
            Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
            self.editorCommand=False
            self.editorLine=''
        elif self.insertCommand == True:
            proName = self.projectName
            controlID = self.insertbeforeLine

            keyUp = self.my_listkeyUp.get(ANCHOR)

            newLine = f'keyUp|||{keyUp}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'

            ev.inserter(proName, newLine, controlID)
            
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"keyUp {keyUp}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            self.insertCommand = False
            self.insertbeforeLine = ''
        else:
            keyUp = self.my_listkeyUp.get(ANCHOR)
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
            f.write(f's{curId}:#$%^&*(st)|||keyUp|||{keyUp}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
            f.close()
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text=f"s{curId}:#$%^&*(st) keyUp {keyUp}", font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=235, height=20)
            Label(self.mainGui, text='The task has been added to the list', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def checkRaport(self):
        browse_text = StringVar()
        browse_text.set("Browse")
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=440, height=258)        
        Label(self.mainGui, text="Task Line checkRaport to typeWrite", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Button(self.mainGui, textvariable=browse_text, command=lambda:checkRaportopenDir(), font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=230, width=95, height=20)
    
        def checkRaportopenDir(): 
            browse_text.set("Selecting ...")
            directory = askdirectory(parent=self.mainGui, title="Choice directory", initialdir='./')            
            if directory:                          
                browse_text.set("Loading ...")
                self.checkRaportDict['Dir'] = str(directory)
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=230, width=400, height=258)                            
                Label(self.mainGui, text=f'{directory}', font=("Consolas", 7, "normal"), fg="gray", bg="#131313", justify="left").place(x=495, y=255, height=20)
                Button(self.mainGui, text="Set a flag", command=self.checkRaportRaportFile, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=230, width=95, height=20)

    def checkRaportRaportFile(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=230, width=400, height=258) 
        self.checkRaportrapFile = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.checkRaportrapFile.insert(END, str(self.checkRaportDict['Raport']))
        self.checkRaportrapFile.place(x=600, y=230, width=95)
        Label(self.mainGui, text='.dat', font=("Consolas", 10, "normal"), fg="#3279bc", bg="#131313", justify="left").place(x=700, y=230)
        Button(self.mainGui, text="Tolerance", command=self.checkRaporlOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=650, y=418, width=100, height=30)
        Button(self.mainGui, text="Set name", command=self.setRaportRaportFile, font=("Consolas", 7, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=640, y=250)

    def setRaportRaportFile(self):
        self.checkRaportDict['Raport']=self.checkRaportrapFile.get()
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=230, width=200, height=58)
        Label(self.mainGui, text=str(self.checkRaportDict['Raport']), font=("Consolas", 10, "normal"), fg="gray", bg="#131313", bd=0, justify="right").place(x=600, y=230, width=95)
        Label(self.mainGui, text='.dat', font=("Consolas", 10, "normal"), fg="#3279bc", bg="#131313", justify="left").place(x=700, y=230)
        Button(self.mainGui, text="Change name", command=self.checkRaportRaportFile, font=("Consolas", 7, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=640, y=250)
        Button(self.mainGui, text="Capture", command=self.checkRaportOn, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=650, y=420, width=95)

    def checkRaporlOnTolerance(self): 
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkRaportRaportFile, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)

        if self.checkRaportDict['Tolerance'] == 'Tolerance_100':
            Button(self.mainGui, text="100%", command=self.checkRaportOnTolerance100, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=252, width=95)
        else: Button(self.mainGui, text="100%", command=self.checkRaportOnTolerance100, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=252, width=95)

        if self.checkRaportDict['Tolerance'] == 'Tolerance_90':    
            Button(self.mainGui, text="90%", command=self.checkRaportOnTolerance90, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=274, width=95)
        else: Button(self.mainGui, text="90%", command=self.checkRaportOnTolerance90, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=274, width=95)

        if self.checkRaportDict['Tolerance'] == 'Tolerance_80':    
            Button(self.mainGui, text="80%", command=self.checkRaportOnTolerance80, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=296, width=95)
        else: Button(self.mainGui, text="80%", command=self.checkRaportOnTolerance80, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=296, width=95)

        if self.checkRaportDict['Tolerance'] == 'Tolerance_70':    
            Button(self.mainGui, text="70%", command=self.checkRaportOnTolerance70, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=318, width=95)
        else: Button(self.mainGui, text="70%", command=self.checkRaportOnTolerance70, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=318, width=95)

        if self.checkRaportDict['Tolerance'] == 'Tolerance_50':    
            Button(self.mainGui, text="50%", command=self.checkRaportOnTolerance50, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=340, width=95)
        else: Button(self.mainGui, text="50%", command=self.checkRaportOnTolerance50, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=340, width=95)

        if self.checkRaportDict['Tolerance'] == 'Tolerance_30':    
            Button(self.mainGui, text="30%", command=self.checkRaportOnTolerance30, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=362, width=95)
        else: Button(self.mainGui, text="30%", command=self.checkRaportOnTolerance30, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=362, width=95)

    def checkRaportOnTolerance100(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkRaporlOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkRaportDict['Tolerance']='Tolerance_100'        
    def checkRaportOnTolerance90(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkRaporlOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkRaportDict['Tolerance']='Tolerance_90'        
    def checkRaportOnTolerance80(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkRaporlOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkRaportDict['Tolerance']='Tolerance_80'        
    def checkRaportOnTolerance70(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkRaporlOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkRaportDict['Tolerance']='Tolerance_70'        
    def checkRaportOnTolerance50(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkRaporlOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkRaportDict['Tolerance']='Tolerance_50'        
    def checkRaportOnTolerance30(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkRaporlOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkRaportDict['Tolerance']='Tolerance_30'  

    def checkRaportOn(self):
        ia=99
        for i in range(100):
            ix = ia / 100
            self.root.attributes('-alpha', ix)
            time.sleep(0.006)
            ia -= 1
        sleep(1)
        pro = str(self.projectName)     
        rapDir = str(self.checkRaportDict['Dir'])
        tol = str(self.checkRaportDict['Tolerance'])
        rapName = str(self.checkRaportDict['Raport'])
        if self.editorCommand==True:
            flagId = str(self.fileNameLocateOn)
            newLine = self.editorLine            
            rapFile = f'{rapDir}/{rapName}.dat'
            seqLO = str(f'Raport|||{flagId}|||{rapFile}|||{tol}|||TAB|||TAB|||TAB|||TAB9|||{newLine}')         
            os.system(f'start python rctf.py -p "{pro}" -s "{seqLO}" -e True')
            sys.exit()

        elif self.insertCommand == True:           
            controlID = self.insertbeforeLine
            flagId = str(self.fileNameLocateOn)

            rapFile = f'{rapDir}/{rapName}.dat'
            
            seqLO = str(f'Raport|||IMG|||{rapFile}|||{tol}|||TAB|||TAB|||TAB|||TAB9|||{controlID}') 
            os.system(f'start python rctf.py -p "{pro}" -s "{seqLO}" -e InsertTrue')
            self.insertCommand = False
            self.insertbeforeLine = ''
            sys.exit()  

        else:           
            rapFile = f'{rapDir}/{rapName}.dat'
            seqLO = str(f'Raport|||IMG|||{rapFile}|||{tol}|||TAB|||TAB|||TAB|||TAB9|||Raport') 
            os.system(f'start python rctf.py -p "{pro}" -s "{seqLO}"')
            sys.exit()

    def checkPixelOnScreen(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line checkPixelOnScreen", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)

        Button(self.mainGui, text="Tolerance", command=self.checkPixelOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        Button(self.mainGui, text="Command", command=self.checkPixelOnPixel, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        if self.checkPixelOnScreenDict['Command'] == 'alert':
            self.checkPixelOnCommend = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", bd=0, justify="left")
            if self.checkPixelOnScreenDict['Message'] =='message':
                self.checkPixelOnCommend.insert(END, "Alert text")
                Button(self.mainGui, text="Set", command=self.checkPixelOnScreenMessage, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=775, y=275) 
            else:
                curText = self.checkPixelOnScreenDict['Message']
                self.checkPixelOnCommend.insert(END, curText)
                Button(self.mainGui, text="Change", command=self.checkPixelOnScreenMessage, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=755, y=275) 

            self.checkPixelOnCommend.place(x=700, y=252, width=95)
            Label(self.mainGui, text="Set alert", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=700, y=230) 
        
        if self.checkPixelOnScreenDict['Command'] == 'sequence':
            if self.checkPixelOnScreenDict['SequenceFile'] == 'None:///12345667876!@#$%^&*().1234342323fdsfsdfsdfsd':
                self.myJoinedProject = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", justify="left")
                self.myJoinedProject.place(x=700, y=252, width=95, height=100) 
                Button(self.mainGui, text="Set", command=self.checkPixelOnScreenFromList, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=775, y=355)
            else:
                curSeqFile = self.checkPixelOnScreenDict['SequenceFile']
                Label(self.mainGui, text=curSeqFile, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=700, y=252, width=95)
                Button(self.mainGui, text="Change", command=self.changePixelOnList, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=755, y=275) 

            Label(self.mainGui, text="Set sequence", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=700, y=230, width=95)  
            projectList = os.listdir('./dataProjects')      
            for i in projectList:
                if i != self.projectName:
                    self.myJoinedProject.insert(END, i)

        Label(self.mainGui, text="R", font=("Consolas", 9, "normal"), fg="#ff0000", bg="#131313", bd=0, justify="left").place(x=500, y=400)
        
        self.setRJumpX = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="#ff0000", bg="#1b1b1b", bd=0, justify="left")
        self.setRJumpX.insert(END, self.checkPixelOnScreenDict["RGB"][0])
        self.setRJumpX.place(x=515, y=400, width=25)  

        Label(self.mainGui, text="G", font=("Consolas", 9, "normal"), fg="#2aff1a", bg="#131313", bd=0, justify="left").place(x=550, y=400)

        self.setGJumpX = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="#2aff1a", bg="#1b1b1b", bd=0, justify="left")
        self.setGJumpX.insert(END, self.checkPixelOnScreenDict["RGB"][1])
        self.setGJumpX.place(x=565, y=400, width=25)

        Label(self.mainGui, text="B", font=("Consolas", 9, "normal"), fg="#1a80ff", bg="#131313", bd=0, justify="left").place(x=600, y=400)

        self.setBJumpX = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="#1a80ff", bg="#1b1b1b", bd=0, justify="left")
        self.setBJumpX.insert(END, self.checkPixelOnScreenDict["RGB"][2])
        self.setBJumpX.place(x=610, y=400, width=25)


        self.setMouseJumpX = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.setMouseJumpX.insert(END, self.checkPixelOnScreenDict["Locate"][0])
        self.setMouseJumpX.place(x=500, y=420, width=45)  

        Label(self.mainGui, text="x", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=553, y=420)

        self.setMouseJumpY = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
        self.setMouseJumpY.insert(END, self.checkPixelOnScreenDict["Locate"][1])
        self.setMouseJumpY.place(x=570, y=420, width=45)

        Button(self.mainGui, text="Set own RGB", command=self.setPixelOnScreenTryLine, font=("Consolas", 7, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=640, y=400)
        Button(self.mainGui, text="Get RGB from", command=self.getPixelOnScreenTryLine, font=("Consolas", 7, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=640, y=415)
        Button(self.mainGui, text="Show", command=self.checkPixelOnScreenTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=440, width=55)        
        
    def setPixelOnScreenTryLine(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=400, width=134, height=20)
        cr = int(self.setRJumpX.get())
        cg = int(self.setGJumpX.get())
        cb = int(self.setBJumpX.get())
        choiceRGB = (cr, cg, cb)

        cx = int(self.setMouseJumpX.get())
        cy = int(self.setMouseJumpY.get())        
        choiceLocate = (cx, cy)
        self.checkPixelOnScreenDict['Locate']=choiceLocate
        if cr!=''and cg!=''and cb!=''and cr<256 and cg<256 and cb<256 and cx!=''and cy!=''and cx<self.sWidth and cy<self.sHeight:

            choiceRGB = (cr, cg, cb)
            choiceLocate = (cx, cy)
            self.checkPixelOnScreenDict['Locate']=choiceLocate
            self.checkPixelOnScreenDict['RGB']=choiceRGB            
            
            Label(self.mainGui, text="R", font=("Consolas", 9, "normal"), fg="#ff0000", bg="#131313", bd=0, justify="left").place(x=500, y=400)
            Label(self.mainGui, text=str(cr), font=("Consolas", 9, "normal"), fg="#ff0000", bg="#131313", bd=0, justify="left").place(x=515, y=400, width=25)

            Label(self.mainGui, text="G", font=("Consolas", 9, "normal"), fg="#2aff1a", bg="#131313", bd=0, justify="left").place(x=550, y=400)
            Label(self.mainGui, text=str(cg), font=("Consolas", 9, "normal"), fg="#2aff1a", bg="#131313", bd=0, justify="left").place(x=565, y=400, width=25)

            Label(self.mainGui, text="B", font=("Consolas", 9, "normal"), fg="#1a80ff", bg="#131313", bd=0, justify="left").place(x=600, y=400)
            Label(self.mainGui, text=str(cb), font=("Consolas", 9, "normal"), fg="#1a80ff", bg="#131313", bd=0, justify="left").place(x=610, y=400, width=25)

            Label(self.mainGui, text=choiceLocate[0], font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=500, y=420, width=45) 
            Label(self.mainGui, text="x", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=553, y=420)
            Label(self.mainGui, text=choiceLocate[1], font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=570, y=420, width=45)

            Button(self.mainGui, text="Add", command=self.checkPixelOnScreenPic, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=560, y=440, width=55)

            print(self.checkPixelOnScreenDict['RGB'])

        if cr>256 or cg>256 or cg>256:
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
            Label(self.mainGui, text='Wrong RGB', font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Try again", command=self.checkPixelOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
        if cx>self.sWidth and cy>self.sHeight:
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
            Label(self.mainGui, text='Screen Size Error', font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Try again", command=self.checkPixelOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def getPixelOnScreenTryLine(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=400, width=134, height=20)
        
        x = int(self.setMouseJumpX.get())
        y = int(self.setMouseJumpY.get())        
        pa.moveTo(x,y)
        try:pixel = pa.pixel(x, y) 
        except: pixel = (404,404,404)
        self.checkPixelOnScreenDict['RGB']=(pixel[0],pixel[1],pixel[2])
        self.checkPixelOnScreenDict['Locate']=(x,y)
        choiceLocate = self.checkPixelOnScreenDict['Locate']

        Label(self.mainGui, text="R", font=("Consolas", 9, "normal"), fg="#ff0000", bg="#131313", bd=0, justify="left").place(x=500, y=400)
        Label(self.mainGui, text=str(pixel[0]), font=("Consolas", 9, "normal"), fg="#ff0000", bg="#131313", bd=0, justify="left").place(x=515, y=400, width=25)

        Label(self.mainGui, text="G", font=("Consolas", 9, "normal"), fg="#2aff1a", bg="#131313", bd=0, justify="left").place(x=550, y=400)
        Label(self.mainGui, text=str(pixel[1]), font=("Consolas", 9, "normal"), fg="#2aff1a", bg="#131313", bd=0, justify="left").place(x=565, y=400, width=25)

        Label(self.mainGui, text="B", font=("Consolas", 9, "normal"), fg="#1a80ff", bg="#131313", bd=0, justify="left").place(x=600, y=400)
        Label(self.mainGui, text=str(pixel[1]), font=("Consolas", 9, "normal"), fg="#1a80ff", bg="#131313", bd=0, justify="left").place(x=610, y=400, width=25)

        Label(self.mainGui, text=choiceLocate[0], font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=500, y=420, width=45) 
        Label(self.mainGui, text="x", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=553, y=420)
        Label(self.mainGui, text=choiceLocate[1], font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=570, y=420, width=45)

        Button(self.mainGui, text="Add", command=self.checkPixelOnScreenPic, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=560, y=440, width=55)

        # print(self.checkPixelOnScreenDict['RGB'])
        # print(self.checkPixelOnScreenDict['Locate'])

    def checkPixelOnScreenTryLine(self):
        x = int(self.setMouseJumpX.get())
        y = int(self.setMouseJumpY.get())
        pa.moveTo(x,y)
        # pixel = pa.pixel(x, y)        
        # self.checkPixelOnScreenDict['RGB']=(pixel[0],pixel[1],pixel[2])
        self.checkPixelOnScreenDict['Locate']=(x,y)

    def checkPixelOnScreenFromList(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)    
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175) 
        choice = self.myJoinedProject.get(ANCHOR)        
        self.checkPixelOnScreenDict['SequenceFile'] = choice

    def checkPixelOnScreenMessage(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)    
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175) 
        choice = self.checkPixelOnCommend.get()
        self.checkPixelOnScreenDict['Message'] = choice

    def changePixelOnList(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)    
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175)   
        self.myJoinedProject = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", justify="left")
        self.myJoinedProject.place(x=700, y=252, width=95, height=100)         
        Button(self.mainGui, text="Set", command=self.checkPixelOnScreenFromList, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=775, y=355)  
        Label(self.mainGui, text="Set sequence", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=700, y=230, width=95) 
        projectList = os.listdir('./dataProjects')      
        for i in projectList:
            if i != self.projectName:
                self.myJoinedProject.insert(END, i)            

    def checkPixelOnTolerance(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkPixelOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)

        if self.checkPixelOnScreenDict['Tolerance'] == 'Tolerance_100':
            Button(self.mainGui, text="100%", command=self.checkPixelOnTolerance100, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=252, width=95)
        else: Button(self.mainGui, text="100%", command=self.checkPixelOnTolerance100, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=252, width=95)

        if self.checkPixelOnScreenDict['Tolerance'] == 'Tolerance_90':    
            Button(self.mainGui, text="90%", command=self.checkPixelOnTolerance90, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=274, width=95)
        else: Button(self.mainGui, text="90%", command=self.checkPixelOnTolerance90, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=274, width=95)

        if self.checkPixelOnScreenDict['Tolerance'] == 'Tolerance_80':    
            Button(self.mainGui, text="80%", command=self.checkPixelOnTolerance80, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=296, width=95)
        else: Button(self.mainGui, text="80%", command=self.checkPixelOnTolerance80, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=296, width=95)

        if self.checkPixelOnScreenDict['Tolerance'] == 'Tolerance_70':    
            Button(self.mainGui, text="70%", command=self.checkPixelOnTolerance70, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=318, width=95)
        else: Button(self.mainGui, text="70%", command=self.checkPixelOnTolerance70, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=318, width=95)

        if self.checkPixelOnScreenDict['Tolerance'] == 'Tolerance_50':    
            Button(self.mainGui, text="50%", command=self.checkPixelOnTolerance50, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=340, width=95)
        else: Button(self.mainGui, text="50%", command=self.checkPixelOnTolerance50, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=340, width=95)

        if self.checkPixelOnScreenDict['Tolerance'] == 'Tolerance_30':    
            Button(self.mainGui, text="30%", command=self.checkPixelOnTolerance30, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=362, width=95)
        else: Button(self.mainGui, text="30%", command=self.checkPixelOnTolerance30, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=362, width=95)

    def checkPixelOnTolerance100(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkPixelOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkPixelOnScreenDict['Tolerance']='Tolerance_100'        
    def checkPixelOnTolerance90(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkPixelOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkPixelOnScreenDict['Tolerance']='Tolerance_90'        
    def checkPixelOnTolerance80(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkPixelOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkPixelOnScreenDict['Tolerance']='Tolerance_80'        
    def checkPixelOnTolerance70(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkPixelOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkPixelOnScreenDict['Tolerance']='Tolerance_70'        
    def checkPixelOnTolerance50(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkPixelOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkPixelOnScreenDict['Tolerance']='Tolerance_50'        
    def checkPixelOnTolerance30(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkPixelOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkPixelOnScreenDict['Tolerance']='Tolerance_30'        

    def checkPixelOnPixel(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Command", command=self.checkPixelOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)

        if self.checkPixelOnScreenDict['Command'] == "stop":
            Button(self.mainGui, text="Stop", command=self.checkPixelOnPixelStop, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=252, width=95)
        else: Button(self.mainGui, text="Stop", command=self.checkPixelOnPixelStop, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=252, width=95)

        if self.checkPixelOnScreenDict['Command'] == "skip":    
            Button(self.mainGui, text="Skip", command=self.checkPixelOnPixelSkip, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=274, width=95)
        else: Button(self.mainGui, text="Skip", command=self.checkPixelOnPixelSkip, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=274, width=95)

        if self.checkPixelOnScreenDict['Command'] == 'alert':    
            Button(self.mainGui, text="Alert", command=self.checkPixelOnPixelAlert, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=296, width=95)
        else: Button(self.mainGui, text="Alert", command=self.checkPixelOnPixelAlert, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=296, width=95)

        if self.checkPixelOnScreenDict['Command'] == 'sequence':    
            Button(self.mainGui, text="Sequence", command=self.checkPixelOnPixelSequence, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=318, width=95)
        else: Button(self.mainGui, text="Sequence", command=self.checkPixelOnPixelSequence, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=318, width=95)

    def checkPixelOnPixelStop(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175)
        Button(self.mainGui, text="Command", command=self.checkPixelOnPixel, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        self.checkPixelOnScreenDict['Command']='stop' 
    def checkPixelOnPixelSkip(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Command", command=self.checkPixelOnPixel, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175)
        self.checkPixelOnScreenDict['Command']='skip' 
    def checkPixelOnPixelAlert(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175)
        Button(self.mainGui, text="Setting", command=self.checkPixelOnScreen, font=("Consolas", 9, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=252, width=95)
        self.checkPixelOnScreenDict['Command']="alert" 
    def checkPixelOnPixelSequence(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)    
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175)    
        Button(self.mainGui, text="Setting", command=self.checkPixelOnScreen, font=("Consolas", 9, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=252, width=95)
        self.checkPixelOnScreenDict['Command']='sequence' 

    def checkPixelOnScreenPic(self):
        cr = self.checkPixelOnScreenDict["RGB"][0]
        cg = self.checkPixelOnScreenDict["RGB"][1]
        cb = self.checkPixelOnScreenDict["RGB"][2]
        cx = self.checkPixelOnScreenDict['Locate'][0]
        cy = self.checkPixelOnScreenDict['Locate'][1]
        choiceRGB = (int(cr), int(cg), int(cb))
        choiceLocate = (int(cx), int(cy))     
        self.checkPixelOnScreenDict['Locate']=choiceLocate
        self.checkPixelOnScreenDict['RGB']=choiceRGB
        if cr!=''and cg!=''and cb!=''and cr<256 and cg<256 and cb<256 and cx!=''and cy!=''and cx<self.sWidth and cy<self.sHeight:
            comm = str(self.checkPixelOnScreenDict['Command'])
            mess = str(self.checkPixelOnScreenDict['Message'])
            seqFile = str(self.checkPixelOnScreenDict['SequenceFile'])
            tol = str(self.checkPixelOnScreenDict['Tolerance'])
            locate = str(self.checkPixelOnScreenDict['Locate'][0])+"x"+str(self.checkPixelOnScreenDict['Locate'][1])            
            r = str(self.checkPixelOnScreenDict['RGB'][0])
            g = str(self.checkPixelOnScreenDict['RGB'][1])
            b = str(self.checkPixelOnScreenDict['RGB'][2])  

            if self.editorCommand==True:            
                proName = self.projectName
                editLine = self.editorLine

                newLine = f'checkPixel|||{locate}|||{r}|||{g}|||{b}|||{tol}|||{comm}|||{seqFile}|||{mess}'
                ev.editor(proName, editLine, newLine)
                Label(self.mainGui, text="Edit Line keyPress", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                
                Label(self.mainGui, text='The task has been edited', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
                Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
                self.editorCommand=False
                self.editorLine=''
            elif self.insertCommand == True:  
                proName = self.projectName         
                controlID = self.insertbeforeLine
                newLine = str(f'checkPixel|||{locate}|||{r}|||{g}|||{b}|||{tol}|||{comm}|||{seqFile}|||{mess}') 
                ev.inserter(proName, newLine, controlID)   
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
                Label(self.mainGui, text='checkPixel Added', font=("Consolas", 10, "normal"), fg="yellow", bg="#131313", justify="left").place(x=495, y=255, height=20)
                Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)             
                self.insertCommand = False
                self.insertbeforeLine = ''                
            else:                          
                V = VD(f'dataProjects/{self.projectName}/{self.projectName}.vpc')
                SEQ = V.proSequence()
                lenSeq = len(vpc.idSectionBack(SEQ, 1))
                curId = lenSeq + 1
                f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')        
                f.write(f's{curId}:#$%^&*(st)|||checkPixel|||{locate}|||{r}|||{g}|||{b}|||{tol}|||{comm}|||{seqFile}|||{mess}\n')
                f.close()
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
                Label(self.mainGui, text='checkPixel Added', font=("Consolas", 10, "normal"), fg="yellow", bg="#131313", justify="left").place(x=495, y=255, height=20)
                Button(self.mainGui, text="Add next", command=self.workSpace, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)
        if cr>256 or cg>256 or cg>256:
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
            Label(self.mainGui, text='Wrong RGB', font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Try again", command=self.checkPixelOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)        
        if cx>self.sWidth and cy>self.sHeight:
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)                            
            Label(self.mainGui, text='Screen Size Error', font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=255, height=20)
            Button(self.mainGui, text="Try again", command=self.checkPixelOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def checkFlagOnScreen(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line checkFlagOnScreen", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Button(self.mainGui, text="Tolerance", command=self.checkFlagOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        Button(self.mainGui, text="Command", command=self.checkFlagOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        if self.checkFlagOnScreenDict['Command'] == 'alert':
            self.checkFlagOnCommend = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", bd=0, justify="left")
            if self.checkFlagOnScreenDict['Message'] =='message':
                self.checkFlagOnCommend.insert(END, "Alert text")
                Button(self.mainGui, text="Set", command=self.checkFlagOnScreenMessage, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=775, y=275) 
            else:
                curText = self.checkFlagOnScreenDict['Message']
                self.checkFlagOnCommend.insert(END, curText)
                Button(self.mainGui, text="Change", command=self.checkFlagOnScreenMessage, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=755, y=275) 

            self.checkFlagOnCommend.place(x=700, y=252, width=95)
            Label(self.mainGui, text="Set alert", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=700, y=230) 
        
        if self.checkFlagOnScreenDict['Command'] == 'sequence':
            if self.checkFlagOnScreenDict['SequenceFile'] == 'None:///12345667876!@#$%^&*().1234342323fdsfsdfsdfsd':
                self.myJoinedProject = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", justify="left")
                self.myJoinedProject.place(x=700, y=252, width=95, height=100) 
                Button(self.mainGui, text="Set", command=self.checkFlagOnScreenFromList, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=775, y=355)
            else:
                curSeqFile = self.checkFlagOnScreenDict['SequenceFile']
                Label(self.mainGui, text=curSeqFile, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=700, y=252, width=95)
                Button(self.mainGui, text="Change", command=self.changeFlagOnList, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=755, y=275) 

            Label(self.mainGui, text="Set sequence", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=700, y=230, width=95)  
            projectList = os.listdir('./dataProjects')      
            for i in projectList:
                if i != self.projectName:
                    try:self.myJoinedProject.insert(END, i)
                    except:pass

        Button(self.mainGui, text="Capture", command=self.checkFlagOnScreenPic, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=650, y=420, width=95)

    def checkFlagOnScreenFromList(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)    
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175) 
        choice = self.myJoinedProject.get(ANCHOR)        
        self.checkFlagOnScreenDict['SequenceFile'] = choice

    def checkFlagOnScreenMessage(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)    
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175) 
        choice = self.checkFlagOnCommend.get()
        self.checkFlagOnScreenDict['Message'] = choice

    def changeFlagOnList(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)    
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175)   
        self.myJoinedProject = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", justify="left")
        self.myJoinedProject.place(x=700, y=252, width=95, height=100)         
        Button(self.mainGui, text="Set", command=self.checkFlagOnScreenFromList, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=775, y=355)  
        Label(self.mainGui, text="Set sequence", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=700, y=230, width=95) 
        projectList = os.listdir('./dataProjects')      
        for i in projectList:
            if i != self.projectName:
                self.myJoinedProject.insert(END, i)  

    def checkFlagOnTolerance(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkFlagOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)

        if self.checkFlagOnScreenDict['Tolerance'] == 'Tolerance_100':
            Button(self.mainGui, text="100%", command=self.checkFlagOnTolerance100, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=252, width=95)
        else: Button(self.mainGui, text="100%", command=self.checkFlagOnTolerance100, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=252, width=95)

        if self.checkFlagOnScreenDict['Tolerance'] == 'Tolerance_90':    
            Button(self.mainGui, text="90%", command=self.checkFlagOnTolerance90, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=274, width=95)
        else: Button(self.mainGui, text="90%", command=self.checkFlagOnTolerance90, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=274, width=95)

        if self.checkFlagOnScreenDict['Tolerance'] == 'Tolerance_80':    
            Button(self.mainGui, text="80%", command=self.checkFlagOnTolerance80, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=296, width=95)
        else: Button(self.mainGui, text="80%", command=self.checkFlagOnTolerance80, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=296, width=95)

        if self.checkFlagOnScreenDict['Tolerance'] == 'Tolerance_70':    
            Button(self.mainGui, text="70%", command=self.checkFlagOnTolerance70, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=318, width=95)
        else: Button(self.mainGui, text="70%", command=self.checkFlagOnTolerance70, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=318, width=95)

        if self.checkFlagOnScreenDict['Tolerance'] == 'Tolerance_50':    
            Button(self.mainGui, text="50%", command=self.checkFlagOnTolerance50, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=340, width=95)
        else: Button(self.mainGui, text="50%", command=self.checkFlagOnTolerance50, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=340, width=95)

        if self.checkFlagOnScreenDict['Tolerance'] == 'Tolerance_30':    
            Button(self.mainGui, text="30%", command=self.checkFlagOnTolerance30, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=500, y=362, width=95)
        else: Button(self.mainGui, text="30%", command=self.checkFlagOnTolerance30, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=500, y=362, width=95)

    def checkFlagOnTolerance100(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkFlagOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkFlagOnScreenDict['Tolerance']='Tolerance_100'        
    def checkFlagOnTolerance90(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkFlagOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkFlagOnScreenDict['Tolerance']='Tolerance_90'        
    def checkFlagOnTolerance80(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkFlagOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkFlagOnScreenDict['Tolerance']='Tolerance_80'        
    def checkFlagOnTolerance70(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkFlagOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkFlagOnScreenDict['Tolerance']='Tolerance_70'        
    def checkFlagOnTolerance50(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkFlagOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkFlagOnScreenDict['Tolerance']='Tolerance_50'        
    def checkFlagOnTolerance30(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=500, y=252, width=95, height=135)
        Button(self.mainGui, text="Tolerance", command=self.checkFlagOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
        self.checkFlagOnScreenDict['Tolerance']='Tolerance_30'        

    def checkFlagOnFlag(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Command", command=self.checkFlagOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)

        if self.checkFlagOnScreenDict['Command'] == "stop":
            Button(self.mainGui, text="Stop", command=self.checkFlagOnFlagStop, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=252, width=95)
        else: Button(self.mainGui, text="Stop", command=self.checkFlagOnFlagStop, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=252, width=95)

        if self.checkFlagOnScreenDict['Command'] == "skip":    
            Button(self.mainGui, text="Skip", command=self.checkFlagOnFlagSkip, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=274, width=95)
        else: Button(self.mainGui, text="Skip", command=self.checkFlagOnFlagSkip, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=274, width=95)

        if self.checkFlagOnScreenDict['Command'] == 'alert':    
            Button(self.mainGui, text="Alert", command=self.checkFlagOnFlagAlert, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=296, width=95)
        else: Button(self.mainGui, text="Alert", command=self.checkFlagOnFlagAlert, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=296, width=95)

        if self.checkFlagOnScreenDict['Command'] == 'sequence':    
            Button(self.mainGui, text="Sequence", command=self.checkFlagOnFlagSequence, font=("Consolas", 9, "normal"), fg="#555455", bg="#797479", bd=0, justify="left").place(x=600, y=318, width=95)
        else: Button(self.mainGui, text="Sequence", command=self.checkFlagOnFlagSequence, font=("Consolas", 9, "normal"), fg="#555455", bg="#252425", bd=0, justify="left").place(x=600, y=318, width=95)

    def checkFlagOnFlagStop(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175)
        Button(self.mainGui, text="Command", command=self.checkFlagOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        self.checkFlagOnScreenDict['Command']='stop' 
    def checkFlagOnFlagSkip(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Button(self.mainGui, text="Command", command=self.checkFlagOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175)
        self.checkFlagOnScreenDict['Command']='skip' 
    def checkFlagOnFlagAlert(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175)
        Button(self.mainGui, text="Setting", command=self.checkFlagOnScreen, font=("Consolas", 9, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=252, width=95)
        self.checkFlagOnScreenDict['Command']="alert" 
    def checkFlagOnFlagSequence(self):        
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=600, y=252, width=95, height=135)    
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=700, y=210, width=95, height=175)    
        Button(self.mainGui, text="Setting", command=self.checkFlagOnScreen, font=("Consolas", 9, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=252, width=95)
        self.checkFlagOnScreenDict['Command']='sequence' 

    def checkFlagOnScreenPic(self):
        ia=99
        for i in range(100):
            ix = ia / 100
            self.root.attributes('-alpha', ix)
            time.sleep(0.006)
            ia -= 1
        sleep(1)
        pro = str(self.projectName)        
        comm = str(self.checkFlagOnScreenDict['Command'])
        mess = str(self.checkFlagOnScreenDict['Message'])
        seqFile = str(self.checkFlagOnScreenDict['SequenceFile'])
        tol = str(self.checkFlagOnScreenDict['Tolerance'])
        flagId = str(self.fileNameLocateOn)
        if self.editorCommand==True:
            newLine = self.editorLine
            seqLO = str(f'checkFlag|||{flagId}|||{tol}|||{comm}|||{mess}|||{seqFile}|||TAB|||TAB9|||{newLine}') 
        
            os.system(f'start python cctf.py -p "{pro}" -s "{seqLO}" -e True')
            sys.exit()
        elif self.insertCommand == True:           
            controlID = self.insertbeforeLine                      
            
            seqLO = str(f'checkFlag|||IMG|||{tol}|||{comm}|||{mess}|||{seqFile}|||TAB|||TAB9|||{controlID}') 
            os.system(f'start python cctf.py -p "{pro}" -s "{seqLO}" -e InsertTrue')
            self.insertCommand = False
            self.insertbeforeLine = ''
            sys.exit()  
        else:     
            seqLO = str(f'checkFlag|||IMG|||{tol}|||{comm}|||{mess}|||{seqFile}|||TAB|||TAB9|||TAB10') 
            os.system(f'start python cctf.py -p "{pro}" -s "{seqLO}"')
            sys.exit()

    def editLineProject(self):
        choice = self.my_listBoxSequence.get(ANCHOR)
        choice=str(choice)
        choiceSPLIT=choice.split('</>')
        if choice != "":
            if choiceSPLIT[1] == 'osSystem':
                self.editorCommand = True
                self.editorLine = choice
                
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line osSystem", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                self.osSystemCommend = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.osSystemCommend.insert(END, str(choiceSPLIT[2])) 
                self.osSystemCommend.place(x=500, y=230, width=395)   

                Button(self.mainGui, text="Try", command=self.osSystemTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
                Button(self.mainGui, text="Add", command=self.osSystemAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
            
            if choiceSPLIT[1] == 'typeWrite':
                self.editorCommand = True
                self.editorLine = choice   

                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line typeWrite", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                self.typeWriteCommend = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.typeWriteCommend.insert(END, str(choiceSPLIT[2]))
                self.typeWriteCommend.place(x=500, y=230, width=395)        
                Button(self.mainGui, text="Try", command=self.typeWriteTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
                Button(self.mainGui, text="Add", command=self.typeWriteAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)            


            if choiceSPLIT[1] == 'SleepNow':
                self.editorCommand = True
                self.editorLine = choice  

                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line sleepNow", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                self.sleepNowCommend = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.sleepNowCommend.insert(END, str(choiceSPLIT[2]))
                self.sleepNowCommend.place(x=500, y=230, width=45)        
                Button(self.mainGui, text="Add", command=self.sleepNowAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95) 

            
            if choiceSPLIT[1] == 'mouseJump':
                self.editorCommand = True
                self.editorLine = choice   

                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line mouseJump", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                Label(self.mainGui, text="x", font=("Consolas", 10, "normal"), fg="gray", bg="#131313", justify="left").place(x=550, y=228, height=20)
                self.sleepmouseJumpX = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.sleepmouseJumpX.insert(END, str(choiceSPLIT[2]))
                self.sleepmouseJumpX.place(x=500, y=230, width=45)        
                self.sleepmouseJumpY = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.sleepmouseJumpY.insert(END, str(choiceSPLIT[3]))
                self.sleepmouseJumpY.place(x=570, y=230, width=45)       
                Button(self.mainGui, text="Try", command=self.mouseJumpTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
                Button(self.mainGui, text="Add", command=self.mouseJumpAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
            
            if choiceSPLIT[1] == 'mouseDown':
                self.editorCommand = True
                self.editorLine = choice

                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line mouseDown", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)        
                Button(self.mainGui, text="Left", command=self.mouseDownSetLeft, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45)        
                Button(self.mainGui, text="Middle", command=self.mouseDownSetMiddle, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=552, y=228, width=45)   
                Button(self.mainGui, text="Right", command=self.mouseDownSetRight, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=604, y=228, width=45)
    
            
            if choiceSPLIT[1] == 'mouseUp':
                self.editorCommand = True
                self.editorLine = choice   

                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line mouseUp", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)        
                Button(self.mainGui, text="Left", command=self.mouseUpSetLeft, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=228, width=45)        
                Button(self.mainGui, text="Middle", command=self.mouseUpSetMiddle, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=552, y=228, width=45)   
                Button(self.mainGui, text="Right", command=self.mouseUpSetRight, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=604, y=228, width=45)
    
            
            if choiceSPLIT[1] == 'stiffMouse':
                self.editorCommand = True
                self.editorLine = choice   

                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line stiffMouse", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                Label(self.mainGui, text="x", font=("Consolas", 10, "normal"), fg="gray", bg="#131313", justify="left").place(x=550, y=228, height=20)
                self.stiffMouseX = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.stiffMouseX.insert(END, str(choiceSPLIT[2]))
                self.stiffMouseX.place(x=500, y=230, width=45)        
                self.stiffMouseY = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.stiffMouseY.insert(END, str(choiceSPLIT[3]))
                self.stiffMouseY.place(x=570, y=230, width=45)       
                Button(self.mainGui, text="Try", command=self.stiffMouseTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
                Button(self.mainGui, text="Add", command=self.stiffMouseAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
            
            if choiceSPLIT[1] == 'mouseDrag':
                self.editorCommand = True
                self.editorLine = choice   
    
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line mouseDrag", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                Label(self.mainGui, text="x", font=("Consolas", 10, "normal"), fg="gray", bg="#131313", justify="left").place(x=550, y=228, height=20)
                self.sleepmouseDragX = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.sleepmouseDragX.insert(END, str(choiceSPLIT[2]))
                self.sleepmouseDragX.place(x=500, y=230, width=45)        
                self.sleepmouseDragY = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.sleepmouseDragY.insert(END, str(choiceSPLIT[3]))
                self.sleepmouseDragY.place(x=570, y=230, width=45)  
                self.sleepmouseDragS = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.sleepmouseDragS.insert(END, str(choiceSPLIT[4]))
                self.sleepmouseDragS.place(x=640, y=230, width=45)       
                Button(self.mainGui, text="Try", command=self.mouseDragTryLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
                Button(self.mainGui, text="Add", command=self.mouseDragAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

            if choiceSPLIT[1] == 'mouseClick':
                self.editorCommand = True
                self.editorLine = choice
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line mouseClick", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                Button(self.mainGui, text="Left", command=self.mouseClickSetLeft, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=45)        
                Button(self.mainGui, text="Middle", command=self.mouseClickSetMiddle, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=552, y=250, width=45)   
                Button(self.mainGui, text="Right", command=self.mouseClickSetRight, font=("Consolas", 8, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=604, y=250, width=45)

            if choiceSPLIT[1] == 'mouseScroll':
                self.editorCommand = True
                self.editorLine = choice   
                
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line mouseScroll", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                
                self.sleepmouseScrollS = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left")
                self.sleepmouseScrollS.insert(END, str(choiceSPLIT[2]))
                self.sleepmouseScrollS.place(x=500, y=230, width=45)                  
                
                Button(self.mainGui, text="Add", command=self.mouseScrollAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
            
            if choiceSPLIT[1] == 'keyPress':
                self.editorCommand = True
                self.editorLine = choice   

                buttonKeys = vpc.tableChar()
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line keyPress", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                self.my_listKeys = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", justify="left")
                self.my_listKeys.place(x=495, y=230, width=120, height=210)
                for i in buttonKeys:            
                    self.my_listKeys.insert(END, i)
                Button(self.mainGui, text="Add", command=self.keyPressAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=450, width=95) 
            
            if choiceSPLIT[1] == 'keyHold':
                self.editorCommand = True
                self.editorLine = choice   
    
                buttonKeys = vpc.tableChar()
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line keyHold", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                self.my_listHoldKeys = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", justify="left")
                self.my_listHoldKeys.place(x=495, y=230, width=120, height=210)
                for i in buttonKeys:            
                    self.my_listHoldKeys.insert(END, i)
                Button(self.mainGui, text="Add", command=self.keyHoldAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=450, width=95) 
            
            if choiceSPLIT[1] == 'keyDown':
                self.editorCommand = True
                self.editorLine = choice   
    
                buttonKeys = vpc.tableChar()
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line keyDown", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                self.my_listkeyDown = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", justify="left")
                self.my_listkeyDown.place(x=495, y=230, width=120, height=210)
                for i in buttonKeys:            
                    self.my_listkeyDown.insert(END, i)
                Button(self.mainGui, text="Add", command=self.keyDownAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=450, width=95)   
            
            if choiceSPLIT[1] == 'keyUp':
                self.editorCommand = True
                self.editorLine = choice   

                buttonKeys = vpc.tableChar()
                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Editing Line keyUp", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                self.my_listkeyUp = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", justify="left")
                self.my_listkeyUp.place(x=495, y=230, width=120, height=210)
                for i in buttonKeys:            
                    self.my_listkeyUp.insert(END, i)
                Button(self.mainGui, text="Add", command=self.keyUpAddLine, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=450, width=95)  
            
            if choiceSPLIT[1] == 'DictWrite':
                self.editorCommand = True
                self.editorLine = choice

                Label(self.mainGui, text='Let\'s start dictWrite', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
                Button(self.mainGui, text="Edit", command=self.dictWrite, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

            if choiceSPLIT[1] == 'checkPixel':
                self.editorCommand = True
                self.editorLine = choice                 

                self.checkPixelOnScreenDict['Command'] = choiceSPLIT[7]
                self.checkPixelOnScreenDict["RGB"] = (int(choiceSPLIT[3]), int(choiceSPLIT[4]), int(choiceSPLIT[5]))
                self.checkPixelOnScreenDict['Tolerance'] = choiceSPLIT[6]
                self.checkPixelOnScreenDict['Message'] = choiceSPLIT[9]
                self.checkPixelOnScreenDict['SequenceFile'] = choiceSPLIT[8]
                l = str(choiceSPLIT[2])
                locSPLIT = l.split('x')
                self.checkPixelOnScreenDict["Locate"]= (locSPLIT[0], locSPLIT[1])
                

                Label(self.mainGui, text='Let\'s start checkPixel', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
                Button(self.mainGui, text="Edit", command=self.checkPixelOnScreen, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95) 

            if choiceSPLIT[1] == 'LocateOnScreen':
                self.editorCommand = True
                self.editorLine = choice


                self.locateOnScreenDict['Center'] = choiceSPLIT[2]

                self.fileNameLocateOn = choiceSPLIT[3]
                
                self.locateOnScreenDict["Flag"] = (int(choiceSPLIT[4]), int(choiceSPLIT[5]))
                self.locateOnScreenDict['Wait'] = choiceSPLIT[6]
                self.locateOnScreenDict['GoAnd'] = choiceSPLIT[7]

                self.locateOnScreenDict['Tolerance'] = choiceSPLIT[8]
                
                # LocateOnScreen|||Center_YES|||./dataProjects/a/flag_2.png|||30|||30|||Wait_YES|||GoTo_moveTo|||Tolerance_30|||TAB10
                # 'Center' : 'Center_NO', 'Flag' : (100, 100), 'GoAnd' : 'GoAnd_Click', 'Wait' : 'Wait_NO',  'Tolerance' : 'Tolerance_90'

                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Task Line locateOnScreen", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)

                Button(self.mainGui, text="Tolerance", command=self.locateOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
                Button(self.mainGui, text="Set flag", command=self.locateOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
                Button(self.mainGui, text="Go and ..", command=self.locateOnGoTo, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=700, y=230, width=95)
                Button(self.mainGui, text="Wait", command=self.locateOnWait, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=800, y=230, width=95)

                Button(self.mainGui, text=" ", command=self.locateOnCenterYes, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=650, y=404, width=10, height=10)  
                Label(self.mainGui, text="Capture center", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=670, y=400, width=95)
                Button(self.mainGui, text="Capture", command=self.locateOnScreenPic, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=650, y=420, width=95)

            if choiceSPLIT[1] == 'checkFlag':
                self.editorCommand = True
                self.editorLine = choice

                self.fileNameLocateOn = choiceSPLIT[2]
                self.checkFlagOnScreenDict['Tolerance'] = choiceSPLIT[3]
                self.checkFlagOnScreenDict['Command'] = choiceSPLIT[4]               
                
                self.checkFlagOnScreenDict['Message'] = choiceSPLIT[5]
                self.checkFlagOnScreenDict['SequenceFile'] = choiceSPLIT[6]
                
                # checkFlag|||./dataProjects/a/flag_3.png|||Tolerance_50|||alert|||Alert 111|||None:///12345667876!@#$%^&*().1234342323fdsfsdfsdfsd|||TAB|||TAB9|||TAB10
                # self.checkFlagOnScreenDict = {'Command' : 'stop', 'Message' : "message", 'SequenceFile' : "None:///12345667876!@#$%^&*().1234342323fdsfsdfsdfsd", 'Tolerance' : 'Tolerance_90'

                Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
                Label(self.mainGui, text="Task Line checkFlagOnScreen", font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=495, y=210, height=20)
                Button(self.mainGui, text="Tolerance", command=self.checkFlagOnTolerance, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=230, width=95)
                Button(self.mainGui, text="Command", command=self.checkFlagOnFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=230, width=95)
                if self.checkFlagOnScreenDict['Command'] == 'alert':
                    self.checkFlagOnCommend = Entry(self.mainGui, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", bd=0, justify="left")
                    if self.checkFlagOnScreenDict['Message'] =='message':
                        self.checkFlagOnCommend.insert(END, "Alert text")
                        Button(self.mainGui, text="Set", command=self.checkFlagOnScreenMessage, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=775, y=275) 
                    else:
                        curText = self.checkFlagOnScreenDict['Message']
                        self.checkFlagOnCommend.insert(END, curText)
                        Button(self.mainGui, text="Change", command=self.checkFlagOnScreenMessage, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=755, y=275) 

                    self.checkFlagOnCommend.place(x=700, y=252, width=95)
                    Label(self.mainGui, text="Set alert", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=700, y=230) 
                
                if self.checkFlagOnScreenDict['Command'] == 'sequence':
                    if self.checkFlagOnScreenDict['SequenceFile'] == 'None:///12345667876!@#$%^&*().1234342323fdsfsdfsdfsd':
                        self.myJoinedProject = Listbox(self.mainGui, borderwidth=0, highlightthickness=0, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#1b1b1b", justify="left")
                        self.myJoinedProject.place(x=700, y=252, width=95, height=100) 
                        Button(self.mainGui, text="Set", command=self.checkFlagOnScreenFromList, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=775, y=355)
                    else:
                        curSeqFile = self.checkFlagOnScreenDict['SequenceFile']
                        Label(self.mainGui, text=curSeqFile, font=("Consolas", 10, "normal"), fg="#6c7692", bg="#131313", justify="left").place(x=700, y=252, width=95)
                        Button(self.mainGui, text="Change", command=self.changeFlagOnList, font=("Consolas", 7, "normal"), fg="#3279bc", bg="#1b1b1b", bd=0, justify="left").place(x=755, y=275) 

                    Label(self.mainGui, text="Set sequence", font=("Consolas", 9, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=700, y=230, width=95)  
                    projectList = os.listdir('./dataProjects')      
                    for i in projectList:
                        if i != self.projectName:
                            try:self.myJoinedProject.insert(END, i)
                            except:pass

                Button(self.mainGui, text="Capture", command=self.checkFlagOnScreenPic, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=650, y=420, width=95)

            if choiceSPLIT[1] == 'Raport':
                self.editorCommand = True
                self.editorLine = choice
                print(choiceSPLIT[2])
                self.fileNameLocateOn = choiceSPLIT[2]

                self.checkRaportDict['Dir'] = f'./dataProjects/{self.projectName}'
                print(self.checkRaportDict['Dir'])
                f1s = str(choiceSPLIT[3])
                l1s = f1s.split("/")
                for i in l1s:
                    ix=i.endswith('.dat')
                    if ix:
                        f2s = i.split('.')
                        fileNameRaport=f2s[0]                    
                try:self.checkRaportDict['Raport'] = fileNameRaport
                except:self.checkRaportDict['Raport'] = 'fileName'
                self.checkRaportDict['Tolerance'] = choiceSPLIT[4]
                
                # Raport|||./dataProjects/a/flag_5.png|||/C:/Users/M/Desktop/raport.dat|||Tolerance_70|||TAB|||TAB|||TAB|||TAB9|||Raport
                # 'Dir' : './', 'Raport' : "raport", 'Tolerance' : 'Tolerance_90'

                Label(self.mainGui, text='Let\'s start checkRaport', font=("Consolas", 10, "normal"), fg="#a8b41d", bg="#131313", justify="left").place(x=495, y=255, height=20)
                Button(self.mainGui, text="Edit", command=self.checkRaport, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=495, y=280, width=95)

    def removerLineProject(self):
        choice = self.my_listBoxSequence.get(ANCHOR)
        self.removeLineProject = choice
        if choice != "":
            choiceShow = choice[:55] + ' ...'
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text="Task Line Remover", font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text=choiceShow, font=("Consolas", 8, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=500, y=228)            
            Button(self.mainGui, text="Remove Line", command=self.removerLineProccess, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
            Button(self.mainGui, text="Cancel", command=self.restart, font=("Consolas", 9, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
    
    def removerLineProccess(self):
        proName = self.projectName
        chkID = self.removeLineProject
        chkID=str(chkID)
        splChkID = chkID.split('</>')
        directory=f'./dataProjects/{self.projectName}/'

        if splChkID[1]=='DictWrite':
            try:os.remove(directory+splChkID[2])
            except:pass
        
        if splChkID[1]=='LocateOnScreen':
            try:os.remove(splChkID[3])
            except:pass
        
        if splChkID[1]=='checkFlag':
            try:os.remove(splChkID[2])
            except:pass
        
        if splChkID[1]=='Raport':
            try:os.remove(splChkID[2])
            except:pass
        
        ev.deleter(proName, chkID)

        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Task Line Remover", font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text='The line has been removed', font=("Consolas", 8, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=500, y=228)            
        Button(self.mainGui, text="Reload", command=self.restart, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        self.removeLineProject = None
        

    def playExcalibure(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=630, y=45, height=50, width=160)
        Button(self.mainGui, text="While", command=self.playExcalibureWhile, font=("Consolas", 7, "normal"), fg="#84e263", bg="#131313", bd=0, justify="left").place(x=640, y=48, height=20)
        Button(self.mainGui, text="Loops", command=self.playExcalibureLoops, font=("Consolas", 7, "normal"), fg="#84e263", bg="#131313", bd=0, justify="left").place(x=680, y=48, height=20)

    def playExcalibureWhile(self):
        whiles = '0</>0</>1'
        os.system(f'start python excalibure.py -p {self.projectName} -a "{whiles}"')
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=630, y=45, height=50, width=160)

    def playExcalibureLoops(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=710, y=45, height=34, width=40)
        Button(self.mainGui, text="< ", command=self.playExcalibureLoopsMinus, font=("Consolas", 8, "normal"), fg="#84e263", bg="#131313", bd=0, justify="left").place(x=720, y=50)
        self.exLoops = Label(self.mainGui, text=str(self.playExcalibureLoop), font=("Consolas", 7, "normal"), fg="white", bg="#181818", justify="left").place(x=740, y=51,  width=20)        
        Button(self.mainGui, text=" >", command=self.playExcalibureLoopsPlus, font=("Consolas", 8, "normal"), fg="#84e263", bg="#131313", bd=0, justify="left").place(x=765, y=50)
        Button(self.mainGui, text=" start", command=self.playExcalibureLoopsGo, font=("Consolas", 8, "normal"), fg="green", bg="#131313", bd=0, justify="left").place(x=727, y=68)
    
    def playExcalibureLoopsMinus(self):
        if self.playExcalibureLoop > 1:
            self.playExcalibureLoop -= 1
        else:
            self.playExcalibureLoop = 1
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=710, y=45, height=34, width=40)
        Button(self.mainGui, text="< ", command=self.playExcalibureLoopsMinus, font=("Consolas", 8, "normal"), fg="#84e263", bg="#131313", bd=0, justify="left").place(x=720, y=50)
        self.exLoops = Label(self.mainGui, text=str(self.playExcalibureLoop), font=("Consolas", 7, "normal"), fg="white", bg="#181818", justify="left").place(x=740, y=51,  width=20)        
        Button(self.mainGui, text=" >", command=self.playExcalibureLoopsPlus, font=("Consolas", 8, "normal"), fg="#84e263", bg="#131313", bd=0, justify="left").place(x=765, y=50)
        Button(self.mainGui, text=" start", command=self.playExcalibureLoopsGo, font=("Consolas", 8, "normal"), fg="green", bg="#131313", bd=0, justify="left").place(x=727, y=68)

    def playExcalibureLoopsPlus(self):
        if self.playExcalibureLoop < 100:
            self.playExcalibureLoop += 1
        else:
            self.playExcalibureLoop = 100
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=710, y=45, height=34, width=40)
        Button(self.mainGui, text="< ", command=self.playExcalibureLoopsMinus, font=("Consolas", 8, "normal"), fg="#84e263", bg="#131313", bd=0, justify="left").place(x=720, y=50)
        self.exLoops = Label(self.mainGui, text=str(self.playExcalibureLoop), font=("Consolas", 7, "normal"), fg="white", bg="#181818", justify="left").place(x=740, y=51,  width=20)        
        Button(self.mainGui, text=" >", command=self.playExcalibureLoopsPlus, font=("Consolas", 8, "normal"), fg="#84e263", bg="#131313", bd=0, justify="left").place(x=765, y=50)
        Button(self.mainGui, text=" start", command=self.playExcalibureLoopsGo, font=("Consolas", 8, "normal"), fg="green", bg="#131313", bd=0, justify="left").place(x=727, y=68)

    def playExcalibureLoopsGo(self):
        action = str(self.playExcalibureLoop)
        whiles = f'0</>1</>{action}'
        os.system(f'start python excalibure.py -p {self.projectName} -a "{whiles}"')
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=630, y=45, height=50, width=160)

    def insertLineProject(self):
        choice = self.my_listBoxSequence.get(ANCHOR)        
        if choice != "":
            self.insertCommand = True
            self.insertbeforeLine = str(choice)
            print()
            insertID = self.insertbeforeLine.split('</>')
            choiceID = insertID[0]
            Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
            Label(self.mainGui, text="Task Line Insert", font=("Consolas", 10, "normal"), fg="#00edf0", bg="#131313", justify="left").place(x=495, y=210, height=20)
            Label(self.mainGui, text=f'Configure a new line to add it before ID: {choiceID}', font=("Consolas", 8, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=500, y=228)            
            Button(self.mainGui, text="Start", command=self.workSpace, font=("Consolas", 9, "normal"), fg="#00edf0", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        
    def insertCancel(self):
        self.insertCommand = False
        self.insertbeforeLine = ''
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=490, y=68, width=400, height=24)
        Label(self.mainGui, text='Add task to list', font=("Consolas", 10, "normal"), fg="#91856c", bg="#131313", justify="left").place(x=495, y=70, height=20)
        
    def delProject(self):
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Delete project", font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text=f'Are you sure you want to delete the project named: {self.projectName}', font=("Consolas", 8, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=500, y=228)            
        Button(self.mainGui, text="Remove Line", command=self.deleteProjectYes, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Cancel", command=self.workSpace, font=("Consolas", 9, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)
    
    def deleteProjectYes(self):
        directory=f'./dataProjects/{self.projectName}/' 
        for f in os.listdir(directory):    
            if os.path.isfile(directory+f):
                os.remove(directory+f)
        os.rmdir(directory)

        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=495, y=215, width=400, height=258)
        Label(self.mainGui, text="Delete project", font=("Consolas", 10, "normal"), fg="red", bg="#131313", justify="left").place(x=495, y=210, height=20)
        Label(self.mainGui, text=f'Project {self.projectName} has been deleted.', font=("Consolas", 8, "normal"), fg="gray", bg="#131313", bd=0, justify="left").place(x=500, y=228)            
        Button(self.mainGui, text="Constructor", command=self.openConstructor, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=500, y=250, width=95)
        Button(self.mainGui, text="Exit", command=self.exitProgram, font=("Consolas", 9, "normal"), fg="white", bg="#1b1b1b", bd=0, justify="left").place(x=600, y=250, width=95)

    def openConstructor(self):
        os.system(f'start python constructor.py')
        sys.exit()

    def restart(self):
        os.system(f'start python workspace.py -p {self.projectName}')
        sys.exit()
    
    def exitProgram(self):        
        sys.exit()


root = tkinter.Tk()
area = MainProcess(root)
root.mainloop()