import pyautogui as pa
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import sys
from time import sleep
import argparse
import virtualPC as vpc
from virtualPC import VirtualData as VD
import editorVPC as ev

#####################################        ARGUMETOWANIE SKRYPTU     #####################################
parser = argparse.ArgumentParser(description="Hacker GRA cRPG v1")
parser.add_argument("-s", "--sequence", type=str, help="Enter the name in the command line, if there are spaces use quotation marks")
parser.add_argument("-p", "--project", type=str, help="Enter the name in the command line, if there are spaces use quotation marks")
parser.add_argument("-e", "--edit", type=str, help="Enter the name in the command line, if there are spaces use quotation marks")
args = parser.parse_args()
sequence = args.sequence
project = args.project
editIt = args.edit
##################################### ARGUMETOWANIE SKRYPTU ZAKONCZONE #####################################



minShot = pa.locateCenterOnScreen('minShot.png')
minOnShot = pa.locateCenterOnScreen('minOnShot.png')
if minShot:
    pa.moveTo(minShot)
    pa.click()
if minOnShot:
    
    pa.moveTo(minOnShot)
    pa.click()
sleep(5)
pa.screenshot('caly.png')
sleep(1)
coords = {'FLAG': (0,0,0,0)}

class MainProcess:
    def __init__(self, root):        
        self.editIt = editIt
        self.projectName = project
        self.sequence = sequence

        self.sequence = sequence
        screenSize = pa.size()
        self.sWidth = screenSize[0]
        self.sHeight = screenSize[1]

        sScale = 2
        rezW = int(self.sWidth / sScale)
        rezH = int(self.sHeight / sScale)
        posW = rezW - 40

        self.root = root
        self.root.title("VirtualPC")
        self.root.geometry(f"{rezW}x{rezH}+{posW}+20") 
        self.root.resizable(False, False)                
        self.bg=ImageTk.PhotoImage(file="caly.png")
        
        self.mainGui = Frame(root)
        self.mainGui.pack(side="top", expand=True, fill="both")
        self.screen = Image.open('caly.png')
        self.resized = self.screen.resize((rezW,rezH), Image.ANTIALIAS)
        self.newScreen = ImageTk.PhotoImage(self.resized)
        self.bg_image=Label(self.mainGui, image=self.newScreen, height=rezW, width=rezH)       
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)
        
        w = rezW
        h = rezH
        x = w/2
        y = h/2
        print(self.sequence)
        myCanvansUSER = Canvas(self.mainGui, width=w, heigh=h)
        myCanvansUSER.pack()
        imgUSER = PhotoImage(file="cross100.png")     
        myCanvansUSER.create_image(x,y, image=self.newScreen)
        myCanvansUSER.create_image(260, 125, anchor=NW, image=imgUSER)
        myLabelUSER = Label(self.mainGui, text="", font=("Consolas", 7, "normal"), fg="yellow", bg="#1b1b1b", bd=0, justify="left")        
        myLabelUSER.place(x=12, y=310)
        Label(self.mainGui, text='', font=("Consolas", 10, "normal"), fg="white", bg="#131313", justify="left").place(x=12, y=330, width=220, height=70)
        Label(self.mainGui, text="Choose a place to get the flag", font=("Consolas", 9, "normal"), fg="#5ea146", bg="#131313", bd=0, justify="left").place(x=15, y=330)    
        Button(self.mainGui, text="Cancel", command=self.cancelCapture, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=15, y=375)        
        def moveCel(e):
            # e.x
            # e.y
            global imgUSER
            imgUSER = PhotoImage(file="cross100.png") 
            myLabelUSER.config(text="Coordinates X: "+str(e.x)+ "Y: "+str(e.y))
            myCanvansUSER.create_image(e.x,e.y, image=imgUSER) 
            Button(self.mainGui, text="Capture", command=self.saveTheFlag, font=("Consolas", 9, "normal"), fg="yellow", bg="#1b1b1b", bd=0, justify="left").place(x=15, y=350, width=90)
            Button(self.mainGui, text="Wait 5 sec.", command=self.waitSaveTheFlag, font=("Consolas", 9, "normal"), fg="yellow", bg="#1b1b1b", bd=0, justify="left").place(x=107, y=350, width=90)
            Button(self.mainGui, text="Cancel", command=self.cancelCapture, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=15, y=375, width=90)
            cooStX = e.x * 2
            cooStY = e.y * 2
            
            coords["FLAG"] = (cooStX, cooStY)
        myCanvansUSER.bind('<B1-Motion>', moveCel)    

    def cancelCapture(self):
        os.system(f'start python workspace.py -p {self.projectName}')        
        sys.exit()
    
    def waitSaveTheFlag(self):
        import time
        ia=99
        for i in range(100):
            ix = ia / 100
            self.root.attributes('-alpha', ix)
            time.sleep(0.006)
            ia -= 1        
        
        cList = coords.get('FLAG')
        self.sequence = str(self.sequence)
        ii = self.sequence.split("|||")

        seqName = ii[0]
        oldFlag = ii[1]
        rapFile = ii[2]
        tol = ii[3]
        wW = 100
        hH = 100        
        editLine = ii[8]
        # Raport|||./dataProjects/a/flag_6.png|||/D:/PC2/!!michal_w�asne/hck/VisualPC/testy/raport.dat|||Tolerance_70|||TAB|||TAB|||TAB|||TAB9|||Raport'
        
        if self.editIt=='True':
            proName = self.projectName     
            sleep(5)
            cooX = cList[0] - wW 
            cooY = cList[1] - hH
            pa.screenshot(f'{oldFlag}', region=(int(cooX),int(cooY), wW,hH)) 
            print(oldFlag)
            newLine = f'{seqName}|||{oldFlag}|||{rapFile}|||{tol}|||TAB|||TAB|||TAB|||TAB9|||{seqName}'
            print(newLine)
            ev.editor(proName, editLine, newLine)

            os.system(f'start python workspace.py -p {self.projectName}')        
            sys.exit()
        elif self.editIt=='InsertTrue':
            projectDir = os.listdir(f'./dataProjects/{self.projectName}')
            projectFlags = []
            for p in projectDir:
                pT = p.endswith('.png') 
                pN = p.startswith('flag_')
                if pT and pN:
                    projectFlags.append(p)
            countId = len(projectFlags) + 1
            sleep(5)
            cooX = cList[0] - wW 
            cooY = cList[1] - hH
            pa.screenshot(f'./dataProjects/{self.projectName}/flag_{countId}.png', region=(int(cooX),int(cooY), wW,hH))             
            Button(self.mainGui, text="Capture the flag", command=self.saveTheFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=65, y=350)        
            proName = self.projectName   
            newLine = f'{seqName}|||./dataProjects/{self.projectName}/flag_{countId}.png|||{rapFile}|||{tol}|||TAB|||TAB|||TAB|||TAB9|||Raport\n'
            controlID = editLine
            # print(proName, newLine, controlID)
            ev.inserter(proName, newLine, controlID)
            os.system(f'start python workspace.py -p {self.projectName}')        
            sys.exit()

        else:
            projectDir = os.listdir(f'./dataProjects/{self.projectName}')
            projectFlags = []
            for p in projectDir:
                pT = p.endswith('.png') 
                pN = p.startswith('flag_')
                if pT and pN:
                    projectFlags.append(p)
            countId = len(projectFlags) + 1     
            sleep(5)
            cooX = cList[0] - wW
            cooY = cList[1] - hH 
            pa.screenshot(f'./dataProjects/{self.projectName}/flag_{countId}.png', region=(int(cooX),int(cooY), wW,hH))             
            Button(self.mainGui, text="Capture the flag", command=self.saveTheFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=65, y=350)        
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')
            f.write(f's{curId}:#$%^&*(st)|||{seqName}|||./dataProjects/{self.projectName}/flag_{countId}.png|||{rapFile}|||{tol}|||TAB|||TAB|||TAB|||TAB9|||Raport\n')
            f.close()        
            # print(cList[0],cList[1],wW, hH)
            os.system(f'start python workspace.py -p {self.projectName}')        
            sys.exit()
    
    def saveTheFlag(self):
        import time
        ia=99
        for i in range(100):
            ix = ia / 100
            self.root.attributes('-alpha', ix)
            time.sleep(0.006)
            ia -= 1        
        
        cList = coords.get('FLAG')
        self.sequence = str(self.sequence)
        ii = self.sequence.split("|||")

        seqName = ii[0]
        oldFlag = ii[1]
        rapFile = ii[2]
        tol = ii[3]
        wW = 100
        hH = 100        
        editLine = ii[8]
        # Raport|||./dataProjects/a/flag_6.png|||/D:/PC2/!!michal_w�asne/hck/VisualPC/testy/raport.dat|||Tolerance_70|||TAB|||TAB|||TAB|||TAB9|||Raport'
        
        if self.editIt=='True':
            proName = self.projectName
            
            
            sleep(0.5)
            cooX = cList[0] - wW 
            cooY = cList[1] - hH
            pa.screenshot(f'{oldFlag}', region=(int(cooX),int(cooY), wW,hH)) 
            print(oldFlag)
            newLine = f'{seqName}|||{oldFlag}|||{rapFile}|||{tol}|||TAB|||TAB|||TAB|||TAB9|||{seqName}'
            print(newLine)
            ev.editor(proName, editLine, newLine)

            os.system(f'start python workspace.py -p {self.projectName}')        
            sys.exit()
        elif self.editIt=='InsertTrue':
            projectDir = os.listdir(f'./dataProjects/{self.projectName}')
            projectFlags = []
            for p in projectDir:
                pT = p.endswith('.png') 
                pN = p.startswith('flag_')
                if pT and pN:
                    projectFlags.append(p)
            countId = len(projectFlags) + 1
            sleep(0.5)
            cooX = cList[0] - wW 
            cooY = cList[1] - hH
            pa.screenshot(f'./dataProjects/{self.projectName}/flag_{countId}.png', region=(int(cooX),int(cooY), wW,hH))             
            Button(self.mainGui, text="Capture the flag", command=self.saveTheFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=65, y=350)        
            proName = self.projectName   
            newLine = f'{seqName}|||./dataProjects/{self.projectName}/flag_{countId}.png|||{rapFile}|||{tol}|||TAB|||TAB|||TAB|||TAB9|||Raport\n'
            controlID = editLine
            # print(proName, newLine, controlID)
            ev.inserter(proName, newLine, controlID)
            os.system(f'start python workspace.py -p {self.projectName}')        
            sys.exit()
        else:
            projectDir = os.listdir(f'./dataProjects/{self.projectName}')
            projectFlags = []
            for p in projectDir:
                pT = p.endswith('.png') 
                pN = p.startswith('flag_')
                if pT and pN:
                    projectFlags.append(p)
            countId = len(projectFlags) + 1     
            sleep(0.5)
            cooX = cList[0] - wW
            cooY = cList[1] - hH 
            pa.screenshot(f'./dataProjects/{self.projectName}/flag_{countId}.png', region=(int(cooX),int(cooY), wW,hH))             
            Button(self.mainGui, text="Capture the flag", command=self.saveTheFlag, font=("Consolas", 9, "normal"), fg="gray", bg="#1b1b1b", bd=0, justify="left").place(x=65, y=350)        
            proName = self.projectName
            V = VD(f'dataProjects/{proName}/{proName}.vpc')
            SEQ = V.proSequence()
            lenSeq = len(vpc.idSectionBack(SEQ, 1))
            curId = lenSeq + 1
            f = open(f'./dataProjects/{self.projectName}/{self.projectName}.vpc', 'a+')
            f.write(f's{curId}:#$%^&*(st)|||{seqName}|||./dataProjects/{self.projectName}/flag_{countId}.png|||{rapFile}|||{tol}|||TAB|||TAB|||TAB|||TAB9|||Raport\n')
            f.close()        
            # print(cList[0],cList[1],wW, hH)
            os.system(f'start python workspace.py -p {self.projectName}')        
            sys.exit()
        

       
                
        # 'Raport|||IMG|||{rapFile}|||{tol}|||TAB|||TAB|||TAB|||TAB9|||raport'

        

root = tkinter.Tk()
area = MainProcess(root)
root.mainloop()