def wordsNumbersList(
                    
                    yesNotPart = False, 
                    whatPart = 'all', 
                    symbolsWord = 10,
                    maxWords = 100):
    import coffeeBrain
    wordsMeaning = coffeeBrain.coffeePls()[3]

    partCategory = set()
    for l in wordsMeaning.values():
        l = str(l).replace('#cz.mowy#', '').replace(';', '')
        ll = l.replace(',', '').split(' ')
        if len(ll) > 3:
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

print(wordsNumbersList(False, 'All', 8, 10))