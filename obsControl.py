import virtualPC as vpc
import pyperclip
import config
from random import choice

def checkLast():
    vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/NewProjectTESTYPRODUKCJE/flag_1.png|||50|||50|||Wait_YES|||GoTo_moveTo|||Tolerance_90|||NOPRINT')
    vpc.whatNow('mouseJump|||-25|||-50|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('mouseClick|||triple|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('keyDown|||ctrl|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('keyPress|||c|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('keyUp|||ctrl|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    textCLIP = pyperclip.paste()
    try: 
        listCLIP = textCLIP.split(':')[1].strip()
        user = textCLIP.split(':')[0].strip()
        return listCLIP, user
    except IndexError: 
        listCLIP = None
        user = None
        return listCLIP, user

def sendAnswer(string):
    stringLen = len(string)
    if stringLen > 450:
        string = string[:450] + '...'
    def clearPL(s):
        s = s.lower().replace('\n', ' ').replace('ą', 'a').replace('ć', 'c').replace('ę', 'e').replace('ł', 'l').replace('ń', 'n').replace('ó', 'o').replace('ś', 's').replace('ź', 'z').replace('ż', 'z')
        return s
    string = clearPL(string)
    vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/NewProjectTESTYPRODUKCJE/flag_1.png|||50|||50|||Wait_YES|||GoTo_moveTo|||Tolerance_90|||NOPRINT')
    vpc.whatNow('mouseJump|||40|||0|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow(f'typeWrite|||{string}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('keyPress|||enter|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('mouseJump|||0|||60|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    
    return string

def obsStart(toTask, admin=config.botAdmin()):
    # print(admin)
    # print(checkLast()[0], checkLast()[1])
    for _ in range(65):
        if toTask != '' and toTask != checkLast()[0] and checkLast()[0] != None and admin != checkLast()[1] and checkLast()[1] != None:
            listCLIP = checkLast()[0]
            return listCLIP, checkLast()[1]
    
    rrWord = [
            'mów dowcip', 'powiedz jakiś żart', 'powiedz coś mądrego o dzieciach', 'powiedz coś mądrego o życiu', 
            'powiedz coś mądrego o miłości', 'powiedz coś mądrego o radości', 'tell a joke'
            ]
    return choice(rrWord), ''