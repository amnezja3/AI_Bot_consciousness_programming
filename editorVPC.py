from virtualPC import VirtualData as VD
import virtualPC as vpc



def editor(proName, editLine, newLine):    
    # proName = 'a'
    # editLine = 's4:#$%^&*(st) mouseClick one'
    # newLine = 'mouseClick|||xxxx|||yyyyy|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
    
    proName=str(proName)
    editLine=str(editLine)
    newLine=str(newLine)

    SEP = '|||'
    V = VD(f'dataProjects/{proName}/{proName}.vpc')
    HEADER = V.header()
    PRE = V.preLoader()
    PRO = V.proGeneral()
    SEQ = V.proSequence()
    LOG = V.logsSession()

    tempDict = {} # doadje id do keys i commandLine do values
    for i in SEQ:
        i=str(i)
        ii = i.split(SEP)
        tempDict[ii[0]]=ii[1:]

    editLineSplit = editLine.split('</>')
    editID={} # tworzy Dict z edytowaną linią key=Id Values=commandLine
    for i in tempDict.keys():
        if i == editLineSplit[0]:
            editID[i]=tempDict[i]

    for k,v in editID.items():sampeleID=k;sampeleCommand=v # oddaje klucz i wartość edytowanej lini
    print(editLineSplit)
    newLine=newLine.split(SEP)

    if editLineSplit[1] == 'osSystem':
        sampeleCommand[1]=newLine[1]

    if editLineSplit[1] == 'typeWrite':
        sampeleCommand[1]=newLine[1]

    if editLineSplit[1] == 'SleepNow':
        sampeleCommand[1]=newLine[1]
    
    if editLineSplit[1] == 'mouseJump':
        sampeleCommand[1]=newLine[1]
        sampeleCommand[2]=newLine[2]

    if editLineSplit[1] == 'mouseDown':
        sampeleCommand[1]=newLine[1]

    if editLineSplit[1] == 'mouseUp':
        sampeleCommand[1]=newLine[1]

    if editLineSplit[1] == 'stiffMouse':
        sampeleCommand[1]=newLine[1]
        sampeleCommand[2]=newLine[2]

    if editLineSplit[1] == 'mouseDrag':
        sampeleCommand[1]=newLine[1]
        sampeleCommand[2]=newLine[2]
        sampeleCommand[3]=newLine[3]

    if editLineSplit[1] == 'mouseClick':
        sampeleCommand[1]=newLine[1]
        sampeleCommand[2]=newLine[2]
        
    if editLineSplit[1] == 'mouseScroll':
        sampeleCommand[1]=newLine[1]

    if editLineSplit[1] == 'keyPress':
        sampeleCommand[1]=newLine[1]

    if editLineSplit[1] == 'keyHold':
        sampeleCommand[1]=newLine[1]

    if editLineSplit[1] == 'keyDown':
        sampeleCommand[1]=newLine[1]

    if editLineSplit[1] == 'keyUp':
        sampeleCommand[1]=newLine[1]

    if editLineSplit[1] == 'DictWrite':
        sampeleCommand[1]=newLine[1]
        def clearGeneral(gg):
            for vpcPRO in PRO:
                vpcPRO=str(vpcPRO)
                splitPRO=vpcPRO.split(SEP)
                for lll in splitPRO:
                    if lll==gg:                        
                        PRO.remove(vpcPRO)
            f=open(f'dataProjects/{proName}/{proName}.vpc', 'w+')
            for vpcPRO in PRO:f.write(vpcPRO+'\n')                
            f.close()
            lenPRO = len(vpc.idSectionBack(PRO, 1))
            curGId = lenPRO + 1
            fileName = newLine[1]
            curId = editLineSplit[0]            
            f = open(f'./dataProjects/{proName}/{proName}.vpc', 'a+')        
            f.write(f'g{curGId}:#$%^&*(gg)|||DictWrite|||{fileName}|||TypeWrite|||{curId}|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')                        
            f.close()
        clearGeneral(editLineSplit[0])
        PRO = V.proGeneral()

    if editLineSplit[1] == 'checkPixel':
        sampeleCommand[1]=newLine[1]

        sampeleCommand[2]=newLine[2]
        sampeleCommand[3]=newLine[3]
        sampeleCommand[4]=newLine[4]

        sampeleCommand[5]=newLine[5]
        sampeleCommand[6]=newLine[6]
        sampeleCommand[7]=newLine[7]
        sampeleCommand[8]=newLine[8]


    if editLineSplit[1] == 'LocateOnScreen':
        sampeleCommand[1]=newLine[1]
        sampeleCommand[2]=newLine[2]
        sampeleCommand[3]=newLine[3]
        sampeleCommand[4]=newLine[4]
        sampeleCommand[5]=newLine[5]
        sampeleCommand[6]=newLine[6]
        sampeleCommand[7]=newLine[7]
       

    if editLineSplit[1] == 'checkFlag':
        sampeleCommand[1]=newLine[1]
        sampeleCommand[2]=newLine[2]
        sampeleCommand[3]=newLine[3]
        sampeleCommand[4]=newLine[4]
        sampeleCommand[5]=newLine[5]
        sampeleCommand[6]=newLine[6]
    
    if editLineSplit[1] == 'Raport':
        sampeleCommand[1]=newLine[1]
        sampeleCommand[2]=newLine[2]
        sampeleCommand[3]=newLine[3]
        sampeleCommand[4]=newLine[4]
        sampeleCommand[5]=newLine[5]
        sampeleCommand[6]=newLine[6]

    readyLine="" 
    for i in editID[editLineSplit[0]]:readyLine += i+SEP
    readyLine=readyLine.rstrip(SEP)

    allReady=[]
    for k,v in tempDict.items():
        oneReady=''
        for i in v:
            oneReady += i + SEP
        oneReady=oneReady.rstrip(SEP)
        tempDict[k]=oneReady
    tempDict[sampeleID]=readyLine

    for x,y in tempDict.items():allReady.append(x+SEP+y)
    readySEQ = allReady

    f=open(f'dataProjects/{proName}/{proName}.vpc', 'w+')    
    for vpcH in HEADER:f.write(vpcH+'\n')    
    for vpcPRE in PRE:f.write(vpcPRE+'\n')    
    for vpcPRO in PRO:f.write(vpcPRO+'\n')    
    for vpcSEQ in readySEQ:f.write(vpcSEQ+'\n')    
    for vpcLOG in LOG:f.write(vpcLOG+'\n')
    f.close()

def inserter(proName, newLineCommand, controlID):
    
    # proName = 'kkkk'
    SEP = '|||'
    SMALLSEP = '</>'
    # newLineCommand = 'stiffMouse|||1|||1|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
    # chkID = 's1:#$%^&*(st)</>typeWrite</>hello world</>TAB4</>TAB5</>TAB6</>TAB7</>TAB8</>TAB9</>TAB10'   
    chkID=str(controlID)
    chkSpl = chkID.split(SMALLSEP)
    SHELL = f'dataProjects/{proName}/{proName}.vpc'    

    tempID = chkSpl[0].split(':')
    ssID = int(tempID[0].lstrip('s'))

    if ssID > 1:
        preID = ssID 
    else:
        preID = 1

    newLID = f's{preID}:{tempID[1]}{SEP}{newLineCommand}'
    onNewLID = f's{preID}:{tempID[1]}'


    V = VD(SHELL)
    HEADER = V.header()
    PRE = V.preLoader()
    PRO = V.proGeneral()
    SEQ = V.proSequence()
    LOG = V.logsSession()

    #Sequences
    newSEQinsert = []
    for i in SEQ:
        iss = str(i)
        ill = iss.split(SEP)
        for j in ill:
            if j==onNewLID:
                newSEQinsert.append(newLID)        
        newSEQinsert.append(i)

    # for i in newSEQinsert:print(i)

    noIDSEQ=[]
    for i in newSEQinsert:
        i=str(i)
        iTr=i.startswith('s')
        if iTr: 
            ill=i.split(SEP)
            newLine=ill[1:]
            noIDSEQ.append(newLine)  

    # for i in noIDSEQ:print(i)


    lnIDS = len(noIDSEQ)
    freshLinesSEQ=[newSEQinsert[0]]
    for i in range(lnIDS):
        x = i+1
        idConstruct = f's{x}:#$%^&*(st)'
        consT=""
        for j in noIDSEQ[i]:        
            consT += j + SEP
        consT=consT.rstrip(SEP)
        compleT= idConstruct+SEP+consT
        freshLinesSEQ.append(compleT)  

    for i in freshLinesSEQ:print(i)

    #Corect ID General
    freshLinesPRO = [PRO[0]]
    gID = 1
    for s in freshLinesSEQ:
        s=str(s)
        splS = s.split(SEP)
        if splS[1]=="DictWrite":
            sID = splS[0]
            gFile = splS[2]
            gLine=f'g{gID}:#$%^&*(gg)|||DictWrite|||{gFile}|||TypeWrite|||{sID}|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            freshLinesPRO.append(gLine)
            gID+=1

    for i in freshLinesPRO:print(i)

    f=open(f'dataProjects/{proName}/{proName}.vpc', 'w+')    
    for vpcH in HEADER:f.write(vpcH+'\n')    
    for vpcPRE in PRE:f.write(vpcPRE+'\n')    
    for vpcPRO in freshLinesPRO:f.write(vpcPRO+'\n')    
    for vpcSEQ in freshLinesSEQ:f.write(vpcSEQ+'\n')    
    for vpcLOG in LOG:f.write(vpcLOG+'\n')
    f.close()

def deleter(proName, chkID):
    # proName = 'kkkk'
    SEP = '|||'
    # chkID = 's3:#$%^&*(st)|||typeWrite|||hello world|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
    chkID=str(chkID)
    chkSpl = chkID.split('</>')
    SHELL = f'dataProjects/{proName}/{proName}.vpc'    

    V = VD(SHELL)
    HEADER = V.header()
    PRE = V.preLoader()
    PRO = V.proGeneral()
    SEQ = V.proSequence()
    LOG = V.logsSession()

    #Sequences
    for i in SEQ:
        iss = str(i)
        ill = iss.split(SEP)
        for j in ill:
            if j==chkSpl[0]:
                SEQ.remove(i)
    noIDSEQ=[]
    for i in SEQ:
        i=str(i)
        iTr=i.startswith('s')
        if iTr: 
            ill=i.split(SEP)
            newLine=ill[1:]
            noIDSEQ.append(newLine)  
    lnIDS = len(noIDSEQ)
    freshLinesSEQ=[SEQ[0]]
    for i in range(lnIDS):
        x = i+1
        idConstruct = f's{x}:#$%^&*(st)'
        consT=""
        for j in noIDSEQ[i]:        
            consT += j + SEP
        consT=consT.rstrip(SEP)
        compleT= idConstruct+SEP+consT
        freshLinesSEQ.append(compleT)    

    #Corect ID General
    freshLinesPRO = [PRO[0]]
    gID = 1
    for s in freshLinesSEQ:
        s=str(s)
        splS = s.split(SEP)
        if splS[1]=="DictWrite":
            sID = splS[0]
            gFile = splS[2]
            gLine=f'g{gID}:#$%^&*(gg)|||DictWrite|||{gFile}|||TypeWrite|||{sID}|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10'
            freshLinesPRO.append(gLine)
            gID+=1


    f=open(f'dataProjects/{proName}/{proName}.vpc', 'w+')    
    for vpcH in HEADER:f.write(vpcH+'\n')    
    for vpcPRE in PRE:f.write(vpcPRE+'\n')    
    for vpcPRO in freshLinesPRO:f.write(vpcPRO+'\n')    
    for vpcSEQ in freshLinesSEQ:f.write(vpcSEQ+'\n')    
    for vpcLOG in LOG:f.write(vpcLOG+'\n')
    f.close()


