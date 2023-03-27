import os
import sys
import time
import pyautogui as pa
from time import sleep
import random

class VirtualData:
    def __init__(self, shell, demonType = None):
        self.shell = shell      

        demonType = str(demonType)
        transDemon = demonType.split('|||')
        self.demonType = transDemon        
        
        self.headerTag = '#$%^&*(st)HEADER'
        self.headerSym = 'h'

        self.preTag = '#$%^&*(st)PRE_LOADER'
        self.preSym = 'p'

        self.proTag = '#$%^&*(gg)PRO_GENERAL'
        self.proSym = 'g'

        self.seqTag = '#$%^&*(st)SEQUENCES'
        self.seqSym = 's'

        self.logTag = '#$%^&*(st)LOG_SESSION'
        self.logSym = 'l'


    def header(self):
        f = open(self.shell, 'r')
        head = f.readlines()
        f.close()
        expList = []
        for l in head:
            lc = l.strip()
            line = lc.startswith(self.headerTag)
            if line == True:
                expList.append(lc)
            vShell = lc.startswith(self.headerSym)
            if vShell == True:
                expList.append(lc)        
        return expList

    def preLoader(self):
        f = open(self.shell, 'r')
        pre = f.readlines()
        f.close()        
        expList = []
        for l in pre:
            lc = l.strip()
            line = lc.startswith(self.preTag)
            if line == True:
                expList.append(lc)
            vShell = lc.startswith(self.preSym)
            if vShell == True:
                expList.append(lc)        
        return expList

    def proGeneral(self):
        f = open(self.shell, 'r')
        pro = f.readlines()
        f.close()
        expList = []
        for l in pro:
            lc = l.strip()
            line = lc.startswith(self.proTag)
            if line == True:
                expList.append(lc)            
            vShell = lc.startswith(self.proSym)
            if vShell == True:                
                expList.append(lc)
        return expList

    def proSequence(self):
        f = open(self.shell, 'r')
        seq = f.readlines()
        f.close()
        expList = []
        for l in seq:
            lc = l.strip()
            line = lc.startswith(self.seqTag)
            if line == True:
                expList.append(lc)
            vShell = lc.startswith(self.seqSym)
            if vShell == True:
                expList.append(lc)        
        return expList

    def logsSession(self):
        f = open(self.shell, 'r')
        log = f.readlines()
        f.close()
        expList = []
        for l in log:
            lc = l.strip()
            line = lc.startswith(self.logTag)
            if line == True:
                expList.append(lc)
            vShell = lc.startswith(self.logSym)
            if vShell == True:
                expList.append(lc)        
        return expList

###############
# Operacyjne
###############
def idSectionBack(section, indX):    
    # zwraca wybraną pozycję w danej sekcji
    lens = len(section) - 1   
    llp = []
    try:
        for p in range(lens):
            ind = p+1         
            s =  section[ind]
            s = str(s)
            llpDemon = s.split('|||')
            llp.append(llpDemon[indX])    
        return llp
    except:
        llp.append('False')
        return llp    

def getFlagsDict(sequence):
    # pobiera flagi z secji PRO_GENERAL i zwraca słownik z kolejnością a,b,c,d oznaczeń wg. id
    s = {}
    #dla każdej kolumny w 
    lenSection = len(idSectionBack(sequence, 0))
    fla = ['a', 'b', 'c', 'd']
    for i in range(lenSection):        
        idBase = idSectionBack(sequence, 4)[i]
        s[idBase] = fla[i]
    return s

def getSequence(sequence):
    # pobiera sekwencje z sekcji SEQUENCE i zwraca szablon sekwencji
    s = {}    
    lenSection = len(idSectionBack(sequence, 0))    
    for i in range(lenSection):
        sp = '|||'
        idBase = idSectionBack(sequence, 0)[i]
        s[idBase] = idSectionBack(sequence, 1)[i]+sp+idSectionBack(sequence, 2)[i]+sp+idSectionBack(sequence, 3)[i]+sp+idSectionBack(sequence, 4)[i]+sp+idSectionBack(sequence, 5)[i]+sp+idSectionBack(sequence, 6)[i]+sp+idSectionBack(sequence, 7)[i]+sp+idSectionBack(sequence, 8)[i]+sp+idSectionBack(sequence, 9)[i]
    return s

def replacer(section, dict, a,b,c,d, fa,fb,fc,fd):
    # podmiena flag dla wybranego ID
    w = []
    
    for k, v in dict.items(): 
        sep='|||' 
        s1=idSectionBack(section, 1)
            
        s3=idSectionBack(section, 3)
        s4=idSectionBack(section, 4)
        s5=idSectionBack(section, 5)
        s6=idSectionBack(section, 6)
        s7=idSectionBack(section, 7)
        s8=idSectionBack(section, 8)
        s9=idSectionBack(section, 9)     
        if v=='a':            
            dict[k]=s1[0]+sep+fa[a]+sep+s3[0]+sep+s4[0]+sep+s5[0]+sep+s6[0]+sep+s7[0]+sep+s8[0]+sep+s9[0]
        if v=='b':                               
            dict[k]=s1[1]+sep+fb[b]+sep+s3[1]+sep+s4[1]+sep+s5[1]+sep+s6[1]+sep+s7[1]+sep+s8[1]+sep+s9[1]
        if v=='c':        
            dict[k]=s1[2]+sep+fc[c]+sep+s3[2]+sep+s4[2]+sep+s5[2]+sep+s6[2]+sep+s7[2]+sep+s8[2]+sep+s9[2]
        if v=='d':        
            dict[k]=s1[3]+sep+fd[d]+sep+s3[3]+sep+s4[3]+sep+s5[3]+sep+s6[3]+sep+s7[3]+sep+s8[3]+sep+s9[3]  
    for ll in dict.values():
        w.append(ll)    
    return w


########### wczytuj listy słów z plików
def getFilenames(generalSection, filePath):
    # zwraca sciezke do plikow okreslonych w sekcji PRO_GENERAL    
    fill = len(idSectionBack(generalSection, 2))
    if fill == 0:
        f1='False'
        f2='False'
        f3='False'
        f4='False'
    elif fill == 1:
        f1=str(filePath + idSectionBack(generalSection, 2)[0])
        f2='False'
        f3='False'
        f4='False'
    elif fill == 2:
        f1=str(filePath + idSectionBack(generalSection, 2)[0])
        f2=str(filePath + idSectionBack(generalSection, 2)[1])
        f3='False'
        f4='False'
    elif fill == 3:
        f1=str(filePath + idSectionBack(generalSection, 2)[0])
        f2=str(filePath + idSectionBack(generalSection, 2)[1])
        f3=str(filePath + idSectionBack(generalSection, 2)[2])
        f4='False'
    elif fill >= 4:
        f1=str(filePath + idSectionBack(generalSection, 2)[0])
        f2=str(filePath + idSectionBack(generalSection, 2)[1])
        f3=str(filePath + idSectionBack(generalSection, 2)[2])
        f4=str(filePath + idSectionBack(generalSection, 2)[3])     
    return [f1, f2, f3, f4]



def fileCreeper(file, id):
    # zwraca linię o wskazanym id z podanego pliku
    f = open(file, 'r')
    fb=f.readlines()
    fex=[]
    for fds in fb:
        fbs=fds.strip()
        fex.append(fbs)    
    if id <= len(fex):
        exp = fex[id]
        exp=str(exp)
        exp=exp.strip()
    else:
        print('Bład: wskazane ID nie istnieje')
        exp = ['False']
    f.close()
    return exp



def fullConntent(pro, path, filePos):
    # zwraca zawartość pliku do listy
    g = []
    try:    
        f=open(getFilenames(pro, path)[filePos], 'r')
        ff =f.readlines()
        for i in ff:
            i=i.strip()
            g.append(i)
        f.close()
        return g
    except:
        return ['False']



def signer(seq, flag):
    # oznacznie flag w pojedyńczej sekwencji zwraca słownik z podmienionymi wartosciami wedlug klucza
    for l in flag.keys():
        for s in seq.keys():
            if s == l:
                seq[s]=flag[s]
    return seq


def loop(section, seq,fla, aa,bb,cc,dd):
    # generuje liste z sekwencją wykonywalną
    p = []
    s = section
    ia = int(len(aa))
    ib = int(len(bb))
    ic = int(len(cc))
    id = int(len(dd))
    for a in range(ia):
        for b in range(ib):
            for c in range(ic):
                for d in range(id):
                    r = signer(seq, fla)
                    w = replacer(s,r, a,b,c,d, aa,bb,cc,dd)
                    for pix in w:
                        p.append(pix)
                    for flag in seq.values():
                        flag = str(flag)
                        rap = flag.endswith('Raport')                        
                        if rap==True:
                            fll = flag.split('|||')
                            p.append(f'CheckRaport|||{aa[0]}|||{bb[0]}|||{cc[0]}|||{dd[0]}|||Success|||{fll[3]}|||{fll[1]}|||{fll[2]}')

    return p

def whatNow(toDo):
    # wykonuje linie sequence
    toDo = str(toDo)
    td = toDo.split('|||')    
    if td[0] == 'osSystem':
        os.system(td[1])

    if td[0] == 'SleepNow':
        seconds = int(td[1]) / 100
        time.sleep(seconds)

    if td[0] == 'LocateOnScreen':
        c = int(td[7][10:]) / 100
        t_Main = pa.locateOnScreen(td[2], confidence=c)
        t = t_Main
        time.sleep(1)
        if td[1] == 'Center_YES':
            t = pa.locateCenterOnScreen(td[2], confidence=c)  
        if td[5] == 'Wait_YES':
            while True:
                if td[8] == 'TAB10':
                    print('Oczekiwanie na: ' + td[2])
                try: t = pa.locateCenterOnScreen(td[2], confidence=c) 
                except MemoryError: t = t_Main
                if t: 
                    break   
        if td[6] == 'GoAnd_Click' and t: 
            pa.moveTo(t)
            pa.click()   

        if td[6] == 'GoAnd_DoubleClick' and t:            
            pa.moveTo(t)
            pa.doubleClick()

        if td[6] == 'GoTo_moveTo'and t:
            pa.moveTo(t)

    if td[0] == 'DictWrite':
        if td[2] == 'TypeWrite':
            pa.typewrite(td[1])

    if td[0] == 'typeWrite':
        pa.typewrite(td[1], interval=0.025)

    if td[0] == 'keyPress':
        pa.press(td[1])

    if td[0] == 'mouseJump':
        x = int(td[1])
        y = int(td[2])
        pa.moveRel(x,y)

    if td[0] == 'mouseClick':
        if td[1] == 'one':
            pa.click(button=td[2])
        if td[1] == 'double':
            pa.doubleClick(button=td[2])
        if td[1] == 'triple':
            pa.tripleClick(button=td[2])

    if td[0] == 'mouseDown':
        pa.mouseDown(button=td[1])

    if td[0] == 'mouseUp':
        pa.mouseUp(button=td[1])

    if td[0] == 'stiffMouse':
        x = int(td[1])
        y = int(td[2])
        pa.moveTo(x,y)

    if td[0] == 'HotKey':
        pa.hotkey(td[2], td[3])
    if td[0] == 'mouseClick':
        if td[1]=='1':
            pa.click(button=td[2])
        if td[1]=='2':
            pa.doubleClick(button=td[2])
        if td[1]=='3':
            pa.tripleClick(button=td[2])
        
    if td[0] == 'mouseDrag':
        x = int(td[1])
        y = int(td[2])
        seconds = int(td[3]) / 100
        pa.drag(x,y,seconds)

    if td[0] == 'mouseScroll':
        scroll = int(td[1])
        pa.scroll(scroll)

    if td[0] == 'keyHold':
        pa.hold(td[1])

    if td[0] == 'keyDown':
        pa.keyDown(td[1])
        
    if td[0] == 'keyUp':
        pa.keyUp(td[1])

    if td[0] == 'CheckRaport':
        # Jeżeli znajdziesz flage zapisz raport do pliku
        c = int(td[6][10:]) / 100
        t = pa.locateCenterOnScreen(td[7], confidence=c) 
        if t: 
            sf = open(td[8], 'a+')
            ti = time.strftime("%B %d %Y %H:%M:%S", time.localtime())
            sf.write(f'[{ti}] Flag found: {t} Raport for words: ({td[1]}, {td[2]}, {td[3]}, {td[4]}) {td[5]}\n')
            sf.close()

    if td[0] == 'checkPixel':        
        xy = str(td[1])
        xy = xy.split('x')
        x = int(xy[0])
        y = int(xy[1])
        
        r = int(td[2])
        g = int(td[3])
        b = int(td[4])
        c = int(td[5][10:]) / 100
        # print(x, y, r, g, b, c, td[6], td[7], td[8])
        try:t = pa.pixelMatchesColor(x, y, (r, g, b), tolerance=c)
        except:t = False     
        if t:
            if td[6] == 'stop':
                print('Module is stop')
                sys.exit()
            if td[6] == 'skip':
                pass
            if td[6] == 'alert':
                pa.alert(text=td[8], title=td[8], button='OK')
            if td[6] == 'sequence':
                return td[7]
        
    if td[0] == 'checkFlag':
        c = int(td[2][10:]) / 100
        t = pa.locateCenterOnScreen(td[1], confidence=c)   
        if t:
            if td[3] == 'stop':
                print('Module is stop')
                sys.exit()
            if td[3] == 'skip':
                pass
            if td[3] == 'alert':
                pa.alert(text=td[4], title=td[4], button='OK')
            if td[3] == 'sequence':
                return td[5]

def tableChar():
    #     s = s.lower().replace(, 'a').replace( 'c').replace( 'e').replace(, 'l').replace(, 'n').replace( 'o').replace( 's').replace( 'z').replace( 'z')

    tblChr = ['0', '1', '2', '3', '4', '5', '6', '7', 'ą','ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż',
            '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`',
            'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
            '!', '"', '#', '$', '%', '&', "'", '(',')', '*', '+', ',', '-', '.', ' ',
            'enter', 'esc', 'escape', 'ctrl', 'ctrlleft',
            'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
            'browserback', 'browserfavorites', 'browserforward', 'browserhome',
            'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
            'convert', 'ctrlright', 'decimal', 'del', 'delete',
            'divide', 'down', 'end', 'execute', 'f1', 'f10',
            'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
            'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
            'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
            'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
            'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
            'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
            'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
            'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
            'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
            'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
            'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
            'command', 'option', 'optionleft', 'optionright', """\t""", """\n""", """\r""", '\\',
                '/']
    return tblChr

def moveGoAvatarSL(moveUp):
    moves = ['w','s','w', 'a', 'd','s','w','w', 'a', 'd']
    sleep(4)
    for _ in range(moveUp):
        oneMove = random.choice(moves)
        timeRange = random.randrange(1, 3)    
        pa.keyDown(oneMove)
        sleep(timeRange)
        pa.keyUp(oneMove)