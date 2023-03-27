import virtualPC as vpc
from virtualPC import VirtualData as VD
import argparse
import pyautogui as pa
from time import sleep

##
import os, sys
os.system('cls')
##


#####################################        ARGUMETOWANIE SKRYPTU     #####################################
parser = argparse.ArgumentParser(description="Hacker GRA cRPG v1")
parser.add_argument("-p", "--project", type=str, help="Enter the name in the command line, if there are spaces use quotation marks")
parser.add_argument("-a", "--action", type=str, help="Enter the name in the command line, if there are spaces use quotation marks")
args = parser.parse_args()
project = args.project
action = args.action
##################################### ARGUMETOWANIE SKRYPTU ZAKONCZONE #####################################

if project == None:
    print('Use the argument -p "Project Name"')
    sys.exit()


minShot = pa.locateCenterOnScreen('minShot.png')
minOnShot = pa.locateCenterOnScreen('minOnShot.png')
if minShot:
    pa.moveTo(minShot)
    pa.click()
if minOnShot:
    pa.moveTo(minOnShot)
    pa.click()
sleep(1)

SHELL = f'dataProjects/{project}/{project}.vpc'
HOME = f'dataProjects/{project}/'

V = VD(SHELL)
HEADER = V.header()
PRE = V.preLoader()
PRO = V.proGeneral()
SEQ = V.proSequence()
LOG = V.logsSession()

flags = vpc.getFlagsDict(PRO)
sequence = vpc.getSequence(SEQ) 

l1 = vpc.fullConntent(PRO, HOME, 0)
l2 = vpc.fullConntent(PRO, HOME, 1)
l3 = vpc.fullConntent(PRO, HOME, 2)
l4 = vpc.fullConntent(PRO, HOME, 3)



# Cała sekwencja i zalezne sekwencje
action = str(action)
actionTimer = action.split('</>')

TIMER = int(actionTimer[0])
STEPER = int(actionTimer[1])
ENDER = int(actionTimer[2])
while True:
    wholeLoops = len(vpc.loop(PRO, sequence, flags, l1,l2,l3,l4))
    for i in range(wholeLoops):
        checkInstruction = vpc.whatNow(vpc.loop(PRO, sequence, flags, l1,l2,l3,l4)[i])  
        sleep(0.006)  
        if checkInstruction != None:
            vSHELL = f'dataProjects/{checkInstruction}/{checkInstruction}.vpc'
            vHOME = f'dataProjects/{checkInstruction}/'
            vV = VD(vSHELL)       
            vPRO = vV.proGeneral()
            vSEQ = vV.proSequence()
            vflags = vpc.getFlagsDict(vPRO)
            vsequence = vpc.getSequence(vSEQ) 
            vl1 = vpc.fullConntent(vSEQ, vHOME, 0)
            vl2 = vpc.fullConntent(vSEQ, vHOME, 1)
            vl3 = vpc.fullConntent(vSEQ, vHOME, 2)
            vl4 = vpc.fullConntent(vSEQ, vHOME, 3)
            vwholeLoops = len(vpc.loop(vPRO, vsequence, vflags, vl1,vl2,vl3,vl4))
            for vi in range(vwholeLoops):
                vcheckInstruction = vpc.whatNow(vpc.loop(vPRO, vsequence, vflags, vl1,vl2,vl3,vl4)[vi])
                sleep(0.006)
                if vcheckInstruction != None:
                    a_SHELL = f'dataProjects/{vcheckInstruction}/{vcheckInstruction}.vpc'
                    a_HOME = f'dataProjects/{vcheckInstruction}/'
                    a_V = VD(a_SHELL)       
                    a_PRO = a_V.proGeneral()
                    a_SEQ = a_V.proSequence()
                    a_flags = vpc.getFlagsDict(a_PRO)
                    a_sequence = vpc.getSequence(a_SEQ) 
                    a_l1 = vpc.fullConntent(a_SEQ, a_HOME, 0)
                    a_l2 = vpc.fullConntent(a_SEQ, a_HOME, 1)
                    a_l3 = vpc.fullConntent(a_SEQ, a_HOME, 2)
                    a_l4 = vpc.fullConntent(a_SEQ, a_HOME, 3)
                    a_wholeLoops = len(vpc.loop(a_PRO, a_sequence, a_flags, a_l1,a_l2,a_l3,a_l4))
                    for a_i in range(a_wholeLoops):
                        a_checkInstruction = vpc.whatNow(vpc.loop(a_PRO, a_sequence, a_flags, a_l1,a_l2,a_l3,a_l4)[a_i])
                        sleep(0.006)                        
                        if a_checkInstruction != None:
                            b_SHELL = f'dataProjects/{a_checkInstruction}/{a_checkInstruction}.vpc'
                            b_HOME = f'dataProjects/{a_checkInstruction}/'
                            b_V = VD(b_SHELL)       
                            b_PRO = b_V.proGeneral()
                            b_SEQ = b_V.proSequence()
                            b_flags = vpc.getFlagsDict(b_PRO)
                            b_sequence = vpc.getSequence(b_SEQ) 
                            b_l1 = vpc.fullConntent(b_SEQ, b_HOME, 0)
                            b_l2 = vpc.fullConntent(b_SEQ, b_HOME, 1)
                            b_l3 = vpc.fullConntent(b_SEQ, b_HOME, 2)
                            b_l4 = vpc.fullConntent(b_SEQ, b_HOME, 3)
                            b_wholeLoops = len(vpc.loop(b_PRO, b_sequence, b_flags, b_l1,b_l2,b_l3,b_l4))
                            for b_i in range(b_wholeLoops):
                                b_checkInstruction = vpc.whatNow(vpc.loop(b_PRO, b_sequence, b_flags, b_l1,b_l2,b_l3,b_l4)[b_i])
                                sleep(0.006)
                                if b_checkInstruction != None:
                                    c_SHELL = f'dataProjects/{b_checkInstruction}/{b_checkInstruction}.vpc'
                                    c_HOME = f'dataProjects/{b_checkInstruction}/'
                                    c_V = VD(c_SHELL)       
                                    c_PRO = c_V.proGeneral()
                                    c_SEQ = c_V.proSequence()
                                    c_flags = vpc.getFlagsDict(c_PRO)
                                    c_sequence = vpc.getSequence(c_SEQ) 
                                    c_l1 = vpc.fullConntent(c_SEQ, c_HOME, 0)
                                    c_l2 = vpc.fullConntent(c_SEQ, c_HOME, 1)
                                    c_l3 = vpc.fullConntent(c_SEQ, c_HOME, 2)
                                    c_l4 = vpc.fullConntent(c_SEQ, c_HOME, 3)
                                    c_wholeLoops = len(vpc.loop(c_PRO, c_sequence, c_flags, c_l1,c_l2,c_l3,c_l4))
                                    for c_i in range(c_wholeLoops):
                                        c_checkInstruction = vpc.whatNow(vpc.loop(c_PRO, c_sequence, c_flags, c_l1,c_l2,c_l3,c_l4)[c_i])
                                        sleep(0.006)
                                        if c_checkInstruction != None:
                                            d_SHELL = f'dataProjects/{c_checkInstruction}/{c_checkInstruction}.vpc'
                                            d_HOME = f'dataProjects/{c_checkInstruction}/'
                                            d_V = VD(d_SHELL)       
                                            d_PRO = d_V.proGeneral()
                                            d_SEQ = d_V.proSequence()
                                            d_flags = vpc.getFlagsDict(d_PRO)
                                            d_sequence = vpc.getSequence(d_SEQ) 
                                            d_l1 = vpc.fullConntent(d_SEQ, d_HOME, 0)
                                            d_l2 = vpc.fullConntent(d_SEQ, d_HOME, 1)
                                            d_l3 = vpc.fullConntent(d_SEQ, d_HOME, 2)
                                            d_l4 = vpc.fullConntent(d_SEQ, d_HOME, 3)
                                            d_wholeLoops = len(vpc.loop(d_PRO, d_sequence, d_flags, d_l1,d_l2,d_l3,d_l4))
                                            for d_i in range(d_wholeLoops):
                                                d_checkInstruction = vpc.whatNow(vpc.loop(d_PRO, d_sequence, d_flags, d_l1,d_l2,d_l3,d_l4)[d_i])
                                                sleep(0.006)
                                                if d_checkInstruction != None:
                                                    e_SHELL = f'dataProjects/{d_checkInstruction}/{d_checkInstruction}.vpc'
                                                    e_HOME = f'dataProjects/{d_checkInstruction}/'
                                                    e_V = VD(e_SHELL)       
                                                    e_PRO = e_V.proGeneral()
                                                    e_SEQ = e_V.proSequence()
                                                    e_flags = vpc.getFlagsDict(e_PRO)
                                                    e_sequence = vpc.getSequence(e_SEQ) 
                                                    e_l1 = vpc.fullConntent(e_SEQ, e_HOME, 0)
                                                    e_l2 = vpc.fullConntent(e_SEQ, e_HOME, 1)
                                                    e_l3 = vpc.fullConntent(e_SEQ, e_HOME, 2)
                                                    e_l4 = vpc.fullConntent(e_SEQ, e_HOME, 3)
                                                    e_wholeLoops = len(vpc.loop(e_PRO, e_sequence, e_flags, e_l1,e_l2,e_l3,e_l4))
                                                    for e_i in range(e_wholeLoops):
                                                        vpc.whatNow(vpc.loop(e_PRO, e_sequence, e_flags, e_l1,e_l2,e_l3,e_l4)[e_i])
                                                        sleep(0.006)

    TIMER += STEPER
    if TIMER == ENDER:
        break
