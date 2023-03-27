import coffeeBrain
import os
import random
def partSeachCategory():
    wordsMeaning = coffeeBrain.coffeePls(False)[3]    
    partCategory = set()
    for l in wordsMeaning.values():
        l = str(l).replace('#cz.mowy#', '').replace(';', '')
        ll = l.replace(',', '').split(' ')
        if len(ll) > 1:
            partCategory.add(ll[0])
    return partCategory

def wordsNumbersList(                    
                    yesNotPart = False, 
                    whatPart = 'all', 
                    symbolsWord = 10,
                    maxWords = 100):
    
    wordsMeaning = coffeeBrain.coffeePls(False)[3]
    
    partCategory = set()
    for l in wordsMeaning.values():
        l = str(l).replace('#cz.mowy#', '').replace(';', '')
        ll = l.replace(',', '').split(' ')
        if len(ll) > 1:
            partCategory.add(ll[0])

    meaningSplied = {}
    for x, l in wordsMeaning.items():
        l = str(l).replace('#cz.mowy#', '').replace(';', '')
        for p in partCategory:
            if l.startswith(p):
                meaningSplied[x] = p
                break

    counter = 0
    filList =[]
    for k, v in meaningSplied.items():
        if yesNotPart:
            if v == whatPart and len(k) == symbolsWord:
                effectListTmp = []
                for c in k: 
                    unicode_char = ord(c)
                    effectListTmp.append(unicode_char)
                exp = [k] + effectListTmp + [v]
                filList.append(exp)                            
                counter += 1
        else:
            if v != whatPart and len(k) == symbolsWord:
                effectListTmp = []
                for c in k: 
                    unicode_char = ord(c)
                    effectListTmp.append(unicode_char)
                exp = [k] + effectListTmp + [v]
                filList.append(exp)                            
                counter += 1        
        if counter == maxWords:
            break

    return filList

def getDataForWord(wordsList):
    filList =[]    
    for w in wordsList:
        w = str(w)
        effectListTmp = []
        for c in w:
            unicode_char = ord(c)
            effectListTmp.append(unicode_char)
        exp = [w] + effectListTmp
        filList.append(exp) 
    return filList

def getKindMemories():
    kindSetMemories = set()
    exportListSorted = []
    folder = os.listdir('./memories')
    for f in folder:
        ff = f.split("_")
        exp = ff[2], int(ff[3]), ff[1]
        kindSetMemories.add(exp)
    
    for l in kindSetMemories:
        exportListSorted.append(l)
    
    exportListSorted.sort()
    return exportListSorted