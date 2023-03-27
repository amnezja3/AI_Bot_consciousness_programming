import perceptronUNT
import percNet
import corrade
import trender
import wordConverter
import random
import sys
from time import sleep
import argparse

banner = '''
                                    ⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿
            Let's gamble    mr.     ⣿⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿
                                    ⣿⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻
                                    ⡿⠟⠋⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄
                                    ⠄⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄

'''

def neuralNet(
            testingList = ['są', 115, 261],
            settingTR = None, 
            useOldMemory = None, 
            maxLoops = None, 
            curcharacters = None, 
            memoryName = None,
            kindSpeach = None,
            maxExample = None):
    
    if maxExample == None:
        EXAMPLE = 25
    else:
        try: EXAMPLE = int(maxExample)
        except: EXAMPLE = 25
        
    if kindSpeach != None:
        kindSpeach = kindSpeach
    else:
        kindSpeach = 'standard'

    if memoryName != None:
        mName = memoryName
    else:
        mName = 'czasownik'

    if maxLoops == None:
        LOOPS = 256
    else:
        try: LOOPS = int(maxLoops)
        except: LOOPS = 256

    if useOldMemory != None:    
        if useOldMemory == 'True':
            useOldMemory = bool(useOldMemory)
            OLD = useOldMemory
        else: OLD = False        
    else: OLD = False

    if settingTR != None:    
        if settingTR == 'True':
            settingTR = bool(settingTR)
            SETTING = settingTR
        else: SETTING = False        
    else: SETTING = False

    if curcharacters != None: numCharacters = int(curcharacters)    
    else: numCharacters = 8

    partSpeach = kindSpeach
    maxCharacters = numCharacters
    scoreData = wordConverter.wordsNumbersList(False, partSpeach, maxCharacters, EXAMPLE) + wordConverter.wordsNumbersList(True, partSpeach, maxCharacters, EXAMPLE)    
    simData = testingList

    'settings'
    categoryPartSpeach = f'{partSpeach}_{maxCharacters}'
    maxLoops = LOOPS
    firstMemory = 3
    maxDeepMemory = 9
    maxOutMemory = 8
    memoryBuild = SETTING
    startOldMemory = OLD
    
    def wordsLists():
        memoryYes_0 = []
        memoryNo_0 = []    
        for s in scoreData:
            record = [s[0]] + [float(s[sx]) for sx in range(1, len(s) - 1, 1)] + ['True']
            if s[len(s) - 1] == partSpeach:
                memoryYes_0.append(record[1:])                
            if s[len(s) - 1] != partSpeach:
                memoryNo_0.append(record[1:len(s) - 1] + ['False'])
        return memoryYes_0 + memoryNo_0
        

    if memoryBuild:
        print('Building memory for the network in progress. Please wait!')
        sumList = len(wordsLists())
        if sumList > 3:
            for n in range(firstMemory):
                memoryHome_new = wordsLists()
                n = str(n)
                if startOldMemory:          
                    oldMemory = [
                                percNet.getMemeory(f'memory_{mName}_{categoryPartSpeach}_0{n}.csv')[0],
                                percNet.getMemeory(f'memory_{mName}_{categoryPartSpeach}_0{n}.csv')[1]
                        ]
                else:
                    oldMemory = [[None], None]
                
                while True:
                    try: weights = perceptronUNT.perceptron(memoryHome_new, oldMemory, maxLoops)
                    except: 
                        weights = [[None], None]
                        memoryHome_new = wordsLists() 
                    if weights[1] != None:
                        fileName = f'memory_{mName}_{partSpeach}_{maxCharacters}_0{n}.csv'
                        percNet.saveMemory(fileName, weights)
                        break
                    else: 
                        try: memoryHome_new.pop(random.randrange(0, len(memoryHome_new) - 1))   
                        except: 
                            memoryHome_new = wordsLists() + wordsLists()
            
            
            memoryHome_DEEP = []
            counter = 0
            for x in wordsLists():
                ex = corrade.levels(x, firstMemory, maxDeepMemory, maxOutMemory, mName, categoryPartSpeach, 'first')
                exp = ex + [x[len(x) - 1]]
                memoryHome_DEEP.append(exp)
                counter += 1

            for n in range(firstMemory, firstMemory + maxDeepMemory, 1):
                memoryHome_new = memoryHome_DEEP
                n = str(n)
                if startOldMemory:          
                    oldMemory = [
                                percNet.getMemeory(f'memory_{mName}_{categoryPartSpeach}_0{n}.csv')[0],
                                percNet.getMemeory(f'memory_{mName}_{categoryPartSpeach}_0{n}.csv')[1]
                        ]
                else:
                    oldMemory = [[None], None]
                while True:
                    try: weights = perceptronUNT.perceptron(memoryHome_new, oldMemory, maxLoops)
                    except: 
                        weights = [[None], None]
                        memoryHome_new = memoryHome_DEEP 
                    if weights[1] != None:
                        # print(weights); print(f'maxDeepMemory{n}'); sleep(1)
                        fileName = f'memory_{mName}_{categoryPartSpeach}_0{n}.csv'
                        percNet.saveMemory(fileName, weights)
                        break
                    else: 
                        try: memoryHome_new.pop(random.randrange(0, len(memoryHome_new) - 1))   
                        except: 
                            memoryHome_new = memoryHome_DEEP + memoryHome_DEEP

            memoryHome_OUT = []
            counter = 0
            for x in wordsLists():
                ex = corrade.levels(x, firstMemory, maxDeepMemory, maxOutMemory, mName, categoryPartSpeach, 'deep')
                exp = ex + [x[len(x) - 1]]
                memoryHome_OUT.append(exp)
                counter += 1

            for n in range(firstMemory + maxDeepMemory, firstMemory + maxDeepMemory + maxOutMemory, 1):
                memoryHome_new = memoryHome_OUT
                n = str(n)
                if startOldMemory:          
                    oldMemory = [
                                percNet.getMemeory(f'memory_{mName}_{categoryPartSpeach}_0{n}.csv')[0],
                                percNet.getMemeory(f'memory_{mName}_{categoryPartSpeach}_0{n}.csv')[1]
                        ]
                else:
                    oldMemory = [[None], None]
                while True:
                    try: weights = perceptronUNT.perceptron(memoryHome_new, oldMemory, maxLoops)
                    except: 
                        weights = [[None], None]
                        memoryHome_new = memoryHome_OUT 
                    if weights[1] != None:
                        # print(weights); print(f'maxOutMemory{n}'); sleep(1)
                        fileName = f'memory_{mName}_{categoryPartSpeach}_0{n}.csv'
                        percNet.saveMemory(fileName, weights)
                        break
                    else: 
                        try: memoryHome_new.pop(random.randrange(0, len(memoryHome_new) - 1))   
                        except: 
                            memoryHome_new = memoryHome_OUT + memoryHome_OUT
        else:
            print('Not enough of learning data !!'); sleep(1)
            sys.exit()

    if memoryBuild:
        loopList = scoreData
    else:
        loopList = simData
    
    wordConvert = wordConverter.getKindMemories()
    # print(wordConvert)
    returnList =[]
    for s in loopList:    
        if memoryBuild:
            record = [s[0]] + [float(s[sx]) for sx in range(1, len(s) - 1, 1)] + ['True']
        else:
            record = [s[0]] + [float(s[sx]) for sx in range(1, len(s), 1)] + ['True']

        trendRange = 0
        trendsTMP = []
        rndTr = []                 
        maxCH = len(record) - 2        
        for w in wordConvert:
            if w[1] == maxCH:
                try:
                    category = str(w[0]) + '_' + str(maxCH)
                    # print(category)
                    resultHome = corrade.levels(record[1:], firstMemory, maxDeepMemory, maxOutMemory, mName, category, 'all')[0]
                    if resultHome != 0:
                        trendsTMP.append(resultHome)
                        rndTr.append(category)
                        trendRange += 1                    
                except: continue
            if len(rndTr) == 6:
                break
        
        if len(rndTr) > 6:
            trendName = 6
        else:
            trendName = len(rndTr)
            
        if trendRange > 0:
            
            nnName = str(s[len(s)-1]) + '_' + str(maxCH)
            trName = f'{mName}_{trendName}_{maxCH}'

            checkList = trendsTMP
            lenCheckList = len(checkList)
            if memoryBuild:
                mainList = checkList + [nnName]
            else:
                mainList = checkList
            # print(rndTr)

            try: # testowt try --- TUTAJ
                trend = trender.getTrend(mainList, maxOutMemory, rndTr, trName)
                
                effect = str(trend[0])
                splitTrendEffect = effect.split('_')
                effectProcent = trend[1]

            # try: # testowt try przeniesiony nad trend bo wypierdalalo memory error
                exp = [str(s[0]), str(splitTrendEffect[0]), str(int(float(effectProcent) * 100)) + '%']
                returnList.append(exp)
                # print(str(s[0]) + ' to ' + str(splitTrendEffect[0]) + ' na ' + str(int(float(effectProcent) * 100)) + '%')
            except: 
                exp = [str(s[0]), None, None]
                returnList.append(exp)
                # print('No effect noticed!')
    
        # time.sleep(.1)
    return returnList   
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Sts scrapper Data Base")
    parser.add_argument("-t", "--training", type=str, help="Give True")
    parser.add_argument("-o", "--useOldMem", type=str, help="Give True")
    parser.add_argument("-m", "--max", type=str, help="loops")
    parser.add_argument("-c", "--characters", type=str, help="Give number of characters")
    parser.add_argument("-n", "--nameMemory", type=str, help="Give subname of memory file")
    parser.add_argument("-k", "--kind", type=str, help='Give settings: name of partspeach')
    parser.add_argument("-e", "--example", type=str, help='Give settings: example of number partspeach')

    args = parser.parse_args()

    settingTR = args.training
    useOldMemory = args.useOldMem
    maxLoops = args.max
    curcharacters = args.characters
    memoryName = args.nameMemory
    kindSpeach = args.kind
    maxExample = args.example
    
    testingList = [
        ['obdarzać', 111, 98, 100, 97, 114, 122, 97, 263],
        ['reanimować', 114, 101, 97, 110, 105, 109, 111, 119, 97, 263],
        ['przystąpić', 112, 114, 122, 121, 115, 116, 261, 112, 105, 263]
    ]
    
    ret = neuralNet(
            testingList,
            settingTR, 
            useOldMemory, 
            maxLoops, 
            curcharacters, 
            memoryName,
            kindSpeach,
            maxExample)
    
    # print(ret)
