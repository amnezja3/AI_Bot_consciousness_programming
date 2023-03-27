
def update():
    import wtf
    import config

    BRAIN_FILE_ADDRESS = str(config.brain('brain'))

    try:brainFile = open(BRAIN_FILE_ADDRESS, 'r+', encoding='utf-8')
    except:brainFile = open(BRAIN_FILE_ADDRESS, 'a+', encoding='utf-8')
    finally:brainFile = open(BRAIN_FILE_ADDRESS, 'r+', encoding='utf-8')
    allBrain = brainFile.readlines()
    brainFile.close()

    SEP_GENERAL = ':'
    SEP_SPLIT = ';'
    SEP_PART = '|'
    SEP_NUM = '^'
    SEP_TITLE = '#'

    INDEX_QUESTION = 'question:'
    INDEX_EXPLAIN = 'explain:'
    INDEX_COMMAND = 'command:'
    INDEX_WORD = 'word:'
    INDEX_MEANING = 'meaning:'

    updateing = open(BRAIN_FILE_ADDRESS, 'r', encoding='utf-8')
    updateList = updateing.readlines()
    updateing.close()

    updateSet = set()
    updSet = set()

    wordBase = {}
    meaningBase = {}
    
    for w in updateList:
        if w.startswith(INDEX_WORD):
            w = str(w)
            ww = w.replace(INDEX_WORD, '').replace(SEP_GENERAL, ' ').replace(SEP_SPLIT, ' ').replace(SEP_PART, ' ').replace(SEP_NUM, ' ').replace(SEP_TITLE, ' ').split(' ')
            for a in ww:            
                updateSet.add(a.strip())
                updSet.add(a.strip())

    for a in allBrain:
        a = a.strip()
 
        word = a.startswith('word:')
        meaning = a.startswith('meaning:')

     
        if word:
            a = str(a).strip().replace('word:', '')
            aa = a.split(SEP_PART)
            wordBase[aa[0]] = aa[1]
        if meaning:        
            a = str(a).strip().replace('meaning:', '')
            aa = a.split(SEP_PART)
            meaningBase[aa[0]] = aa[1]


    upd = open(BRAIN_FILE_ADDRESS, 'r', encoding='utf-8')
    updList = upd.readlines()
    upd.close()



    for x in updList:
        if x.startswith(INDEX_MEANING):
            x = str(x)
            xx = x.replace(INDEX_MEANING, '').split(SEP_PART)
            for b in updateSet:
                if b == xx[0]:                
                    try:updSet.remove(b)
                    except:pass
                

    
    allinSet = len(updSet)
    counter = 1
    print('Analiz with brain: ' + str(allinSet) + ' / ' + str(len(updateSet)))
    for c in updSet:
        updat = str(config.clearCharacters(c))
        partSp = wtf.partSpeech(updat.strip())
        if partSp != None:
            partSp = partSp.replace(INDEX_MEANING, '')
            partSpSplit = partSp.split(SEP_PART)            
            
            written = INDEX_MEANING + str(updat.strip()) + SEP_PART + str(partSpSplit[1]) + '\n'
            print('Updated: ' + written + str(counter) + ' / ' + str(allinSet))
            f = open(BRAIN_FILE_ADDRESS, 'a+', encoding='utf-8')
            try:f.write(written)
            except:'Charset codeError';pass
            f.close()
            counter += 1
        else:
                for keyWord, valueWord in wordBase.items():
                    if keyWord == c:
                        valWo = str(valueWord).split('#Synonimy#')
                        if len(valWo) > 1:
                            if valWo[1].count('#') > 1:
                                calWoSyn = valWo[1].split('#')
                                clearSyn = calWoSyn[0].split(';')
                                access = True
                                for shr in clearSyn:
                                    if shr[0:3] == c[0:3]:
                                        partSp = wtf.partSpeech(shr)
                                        if partSp != None and access:
                                            ssAccess = partSp.replace(INDEX_MEANING, '').split(SEP_PART)
                                            written = INDEX_MEANING + str(c) + SEP_PART + str(ssAccess[1]) + '\n'
                                            meaningBase[c] = ssAccess[1]
                                            f = open(BRAIN_FILE_ADDRESS, 'a+', encoding='utf-8')
                                            try:f.write(written)
                                            except:'Charset codeError';pass
                                            f.close()
                                            access = False