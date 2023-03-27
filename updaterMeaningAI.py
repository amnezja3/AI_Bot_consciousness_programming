import config
import wtf
import neuralWordsNet as nwn
import wordConverter as wcn


BRAIN_FILE_ADDRESS = str(config.brain('brain'))

try:brainFile = open(BRAIN_FILE_ADDRESS, 'r+')
except:brainFile = open(BRAIN_FILE_ADDRESS, 'a+')
finally:brainFile = open(BRAIN_FILE_ADDRESS, 'r+')
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

# print(allBrain)

# f  = open('testUTF8.neural', 'w+')
# for x in allBrain:
#     f.write(x)
# f.close()


def update():


    BRAIN_FILE_ADDRESS = str(config.brain('brain'))

    try:brainFile = open(BRAIN_FILE_ADDRESS, 'r+')
    except:brainFile = open(BRAIN_FILE_ADDRESS, 'a+')
    finally:brainFile = open(BRAIN_FILE_ADDRESS, 'r+')
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

    updateing = open(BRAIN_FILE_ADDRESS, 'r')
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


    upd = open(BRAIN_FILE_ADDRESS, 'r')
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
    
    print('Analiz with brain: ' + str(allinSet) + ' / ' + str(len(updateSet)))

    wordsList = []
    for c in updSet:
        updat = str(config.clearCharacters(c)).strip()
        wordsList.append(updat)
    
    testingList = wcn.getDataForWord(wordsList)
    meaningAIresult = nwn.neuralNet(testingList, None, None, None, None, 'kindSpeach', None, None) 
    [['słowo', None, None], ['słowo', 'rzeczownik', 30]]
    counter = 1
    for pp in meaningAIresult:
        partSp = pp[1]
        partSpSplit = pp[0]
        if partSp != None:
            written = INDEX_MEANING + str(partSp) + SEP_PART + str('#cz.mowy#' + partSpSplit) + SEP_SPLIT + '\n'
            print('Updated: ' + written + str(counter) + ' / ' + str(allinSet))
            wtf.addQuestionAnswer(written)
            counter += 1

update()