# def getTrend(checkData, amountGroun, rndScor, trenderFile = 'trends', listSettings = [2.0, 0.6]):
# def checkFile(sport):
#     import os
#     z=0
#     di=os.listdir('database_files/') # stsstart/
#     for i in di:
#         if i.startswith(f'trends_{sport}.csv'):
#             z=1
#     return z

def getTrend(
            checkData = [0, 1, 4, 5], 
            amountGroun = 12,
            rndScor = [],
            trenderFile = 'trends'
            ):

    '''
    amountGroun = 12
    checkData = [0, 1, 4, 5, 'zaimek']
    
    trenderFile = 'trends'
    rndScor = ['rzeczownik', 'czasownik', 'zaimek', 'przysłówek'] # , 'e', 'o', 'k', 'w', 'p', 'h'
    listSettings = [0.0, 0.6]
    '''
    dictTrend = {}
    amountGroun += 1
    try: 
        trTest = int(checkData[len(checkData) - 1])
        # print(trTest)
        cla = False
    except: cla = True

    if len(rndScor) > 6:
        rndScor = rndScor[:6]
    
    lenTestList = len(rndScor)

    stringDataKey = ''
    for i in checkData:
        stringDataKey += str(i) + '.'
    if cla:
        stringDataKey = str(stringDataKey[:len(stringDataKey) - 1])
    else:
        stringDataKey = str(stringDataKey)
    
    # print(stringDataKey)
    
    if cla:
        lLen = len(stringDataKey) - len(checkData[len(checkData) - 1])
        stringTestKey = stringDataKey[:lLen]
    else:
        stringTestKey = stringDataKey

    # print(len(checkData))
    # print(stringTestKey)
    
    simulatTestingData = []
    for c in rndScor:
        exp = stringTestKey + c        
        simulatTestingData.append(exp)
        # print(exp)
    
    # print(simulatTestingData)
    if cla:
        if lenTestList == 1:
            print('Czas operacji: mniej niż 1 sec.')
        if lenTestList == 2:
            print('Czas operacji: mniej niż 2 sec.')
        if lenTestList == 3:
            print('Czas operacji: mniej niż 4 sec.')
        if lenTestList == 4:
            print('Czas operacji: mniej niż 10 sec.')
        if lenTestList == 5:
            print('Czas operacji: mniej niż 23 sec.')
        if lenTestList == 6:
            print('Czas operacji: ok. 1 min.')

        trendLists = []
        for r in rndScor:
            if lenTestList == 1:
                for a in range(1, amountGroun):            
                    exp = f'{a}.{r}'
                    trendLists.append(exp)        
            if lenTestList == 2:    
                for a in range(1, amountGroun):                          
                    for b in range(1, amountGroun):                    
                        exp =f'{a}.{b}.{r}'
                        trendLists.append(exp)
            if lenTestList == 3:
                for a in range(1, amountGroun):
                    for b in range(1, amountGroun):               
                        for c in range(1, amountGroun):                        
                            exp =f'{a}.{b}.{c}.{r}'
                            trendLists.append(exp)
            if lenTestList == 4:
                for a in range(1, amountGroun):
                    for b in range(1, amountGroun):             
                        for c in range(1, amountGroun):
                            for d in range(1, amountGroun):                    
                                exp =f'{a}.{b}.{c}.{d}.{r}'
                                trendLists.append(exp)
            if lenTestList == 5:
                for a in range(1, amountGroun):
                    for b in range(1, amountGroun):              
                        for c in range(1, amountGroun):
                            for d in range(1, amountGroun):
                                for e in range(1, amountGroun):                        
                                    exp =f'{a}.{b}.{c}.{d}.{e}.{r}'
                                    trendLists.append(exp)
            if lenTestList == 6:
                for a in range(1, amountGroun):                             
                    for b in range(1, amountGroun):               
                        for c in range(1, amountGroun):
                            for d in range(1, amountGroun):
                                for e in range(1, amountGroun):
                                    for f in range(1, amountGroun):                            
                                        exp =f'{a}.{b}.{c}.{d}.{e}.{f}.{r}'
                                        trendLists.append(exp)
        for a in trendLists:
            dictTrend[a] = 0    

    
    # print(trendLst)
    
    try: file = open(f'./database_files/trends_{trenderFile}.csv', 'r+', encoding='utf-8')
    except: file = open(f'./database_files/trends_{trenderFile}.csv', 'w+', encoding='utf-8')
    treDataLst = file.readlines()
    file.close()

    

    for a in treDataLst:
        aa = a.strip().split(';')
        dictTrend[str(aa[0])] = int(aa[1])
    # print(dictTrend)
    
    # print(cla)
    if cla: 
        for a in treDataLst:
            aa = a.strip().split(';')
            if stringDataKey == aa[0]:
                try: dictTrend[stringDataKey] += 1
                except: dictTrend[stringDataKey] = 1
        file = open(f'./database_files/trends_{trenderFile}.csv', 'w+', encoding='utf-8')
        for d, i in dictTrend.items():
            exp = str(d) + ';' + str(i) + '\n'
            file.write(exp)
        file.close()
    
    counterTrends = 1
    summer = 1
    for a in simulatTestingData:
        try: dictTrend[a]
        except: dictTrend[a] = 0
        if dictTrend[a] > 0:
            counterTrends += dictTrend[a]            
            summer += 1

    returnList = []
    counterIndex = 0
    for p in simulatTestingData:
        exp = [rndScor[counterIndex]] + [dictTrend[p] / counterTrends]
        returnList.append(exp)
        counterIndex += 1
    # print(len(returnList))
    # print(returnList)
    
    maxProc = 0
    for w in range(len(returnList)):
        try:returnList[w]
        except: continue
        # print(returnList[w][1])
        if returnList[w][1] >= maxProc:
            returnEXP = returnList[w]
            maxProc = returnList[w][1]
    if returnEXP[1] == 0:
        returnEXP = [None, None]            
    return returnEXP

if __name__ == '__main__':
    print(getTrend())