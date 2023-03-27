import virtualPC as vpc
import pyperclip
import config
from random import choice, randrange

def checkLast():
    reconesse = ['Nearby', 'IM', 'Open_IM', 'moveAva', 'ANY_BLINK']
    proccess = choice(reconesse)
    print(proccess)
    if proccess == 'IM':
        vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/SL_BOT/flag_2.png|||30|||24|||Wait_NO|||GoAnd_Click|||Tolerance_85|||TAB10')
        # vpc.whatNow('mouseJump|||100|||0|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
        # vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    if proccess == 'Nearby':
        vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/SL_BOT/flag_3.png|||30|||24|||Wait_NO|||GoAnd_Click|||Tolerance_85|||TAB10')
        # vpc.whatNow('mouseJump|||100|||0|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
        # vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    if proccess == 'Open_IM':
        vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/SL_BOT/flag_1.png|||30|||30|||Wait_NO|||GoTo_moveTo|||Tolerance_90|||NOPRINT')
        vpc.whatNow('mouseJump|||50|||-70|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
        vpc.whatNow('mouseClick|||one|||right|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
        vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/SL_BOT/flag_4.png|||30|||24|||Wait_NO|||GoAnd_Click|||Tolerance_85|||TAB10')
        vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    if proccess == 'moveAva':
        vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/SL_BOT/flag_1.png|||30|||30|||Wait_YES|||GoTo_moveTo|||Tolerance_90|||NOPRINT')
        vpc.whatNow('mouseJump|||0|||40|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
        vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')        
        vpc.moveGoAvatarSL(randrange(1, 3))
    if proccess == 'ANY_BLINK':
        vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/SL_BOT/flag_3.png|||30|||24|||Wait_NO|||GoAnd_Click|||Tolerance_85|||TAB10')
        # vpc.whatNow('mouseJump|||100|||0|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
        # vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
        
    vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/SL_BOT/flag_1.png|||30|||30|||Wait_YES|||GoTo_moveTo|||Tolerance_90|||NOPRINT')
    vpc.whatNow('mouseJump|||0|||-20|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('mouseClick|||double|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('mouseClick|||triple|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('keyDown|||ctrl|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('keyPress|||c|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('keyUp|||ctrl|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')    
    textCLIP = pyperclip.paste()
    print(textCLIP)
    try:         
        listCLIP = textCLIP.split(':')[2].strip()
        u = textCLIP.split(':')[1].strip()
        user = u.split('] ')[1].strip()
        # print(listCLIP, user)
        return listCLIP, user
    except IndexError: # IndexError ValueError
        vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/SL_BOT/flag_1.png|||30|||30|||Wait_YES|||GoTo_moveTo|||Tolerance_90|||NOPRINT')
        vpc.whatNow('mouseJump|||0|||40|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
        vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')        
        vpc.moveGoAvatarSL(randrange(1, 5))
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
    vpc.whatNow('LocateOnScreen|||Center_YES|||./dataProjects/SL_BOT/flag_1.png|||30|||30|||Wait_YES|||GoTo_moveTo|||Tolerance_90|||NOPRINT')
    vpc.whatNow('mouseJump|||40|||0|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow(f'typeWrite|||{string}|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('keyPress|||enter|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('mouseJump|||0|||60|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    vpc.whatNow('mouseClick|||one|||left|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10')
    
    return string

def obsStart(toTask, admin=config.botSL_Admin()):
    # print(admin)
    # print(checkLast()[0], checkLast()[1])
    for _ in range(65):
        if toTask != '' and toTask != checkLast()[0] and checkLast()[0] != None and admin != checkLast()[1] and checkLast()[1] != None:
            listCLIP = checkLast()[0]
            return listCLIP, checkLast()[1]
    
    rrWord = ['mówisz straszne nudy', 'mów dowcip', 'żart jakiś', 'to dzieci', 'to cierpliwość', 'to miłość', 'to radość',
                'tell me about your self', 'joke', 'kids', 'patient', 'love', 'happy']
    return choice(rrWord), ''