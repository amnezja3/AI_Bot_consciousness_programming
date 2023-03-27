def coffeePls(update = True):
    if update:
        pass
        # print('archives now..')
    import config

    BRAIN_FILE_ADDRESS = str(config.brain('brain'))

    
    with open(BRAIN_FILE_ADDRESS, 'r', encoding='utf-8') as brainFile: 
        allBrain = brainFile.readlines()
  

    questionBase = {}
    explainBase = {}
    commandBase = {}
    wordBase = {}
    meaningBase = {}
    moodsBase = []
    quotationsBase = {}

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

    for a in allBrain:
        a = a.strip()
        question = a.startswith('question:')
        explain = a.startswith('explain:')
        command = a.startswith('command:')
        word = a.startswith('word:')
        meaning = a.startswith('meaning:')
        moods = a.startswith('mood:')
        quotation = a.startswith('quotations:')

        if question:
            a = str(a).strip().replace('question:', '')
            aa = a.split(SEP_PART)
            if aa[1] != '':
                questionBase[aa[0]] = aa[1]
        if explain:
            print('explain: ');print(a)
        if command:
            a = str(a).strip().replace('command:', '')
            aa = a.split(SEP_PART)
            if aa[1] != '':
                commandBase[aa[0].strip()] = aa[1]            
        if word:
            a = str(a).strip().replace('word:', '')
            aa = a.split(SEP_PART)
            if aa[1] != '':
                wordBase[aa[0].strip()] = aa[1]
        if meaning:        
            a = str(a).strip().replace('meaning:', '')
            aa = a.split(SEP_PART)
            if aa[1] != '':
                meaningBase[aa[0].strip()] = aa[1]
        if moods:
            a = str(a).strip().replace('mood:', '')
            if a != '':
                moodsBase.append(a)
        if quotation:        
            a = str(a).strip().replace('quotations:', '')
            aa = a.split(SEP_PART)
            if aa[1] != '':
                quotationsBase[aa[0]] = aa[1]

    if update:
        with open(BRAIN_FILE_ADDRESS, 'w+', encoding='utf-8') as file:
            for k1, v1 in commandBase.items():
                file.write(INDEX_COMMAND + str(k1) + SEP_PART + str(v1) + '\n')

            for k2, v2 in questionBase.items():
                file.write(INDEX_QUESTION + str(k2) + SEP_PART + str(v2) + '\n')
            
            for k1, v1 in wordBase.items():
                file.write(INDEX_WORD + str(k1) + SEP_PART + str(v1) + '\n')
            
            for k, v in meaningBase.items():
                file.write(INDEX_MEANING + str(k) + SEP_PART + str(v) + '\n')
            
            for m in moodsBase:
                file.write('mood:' + str(m) + '\n')
            
            for k, v in quotationsBase.items():
                file.write('quotations:' + str(k) + SEP_PART + str(v) + '\n')

    return commandBase, questionBase, wordBase, meaningBase, moodsBase, quotationsBase
    # print(meaningBase['co'])
    
    

# coffeePls()