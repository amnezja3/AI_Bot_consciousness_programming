import os
import wordConverter

input('Uwaga, sieć zostanie uzupełniona.\
    \nPrzerywanie procesu zbronione!\
    \n[CTRL+C - CANCEL]\
    \n[ENTER - CONTINUE]\
    \n:::>>>')

o = input('-o True\
    \n[ENTER - CONTINUE]\
    \n:::>>>')

e = input('-e examples:\n:::>>>')
m = input('-m max loops:\n:::>>>')

mc = input('min chracters:\n:::>>>')
mw = input('max chracters:\n:::>>>')

try: 
    if int(mc) > 0 and int(mc) < int(mw) and int(mw) > 0:
        mc = int(mc) 
        mw = int(mw) + 1
    else:
        mc = 1 
        mw = 25
except ValueError:
    mc = 1 
    mw = 25

try: e = int(e)
except ValueError: e = 25 
    
try: m = int(m)    
except ValueError: m = 256
    
if o == "":    
    couchbase = f'-o True -e {e} -m {m}'
else:
    couchbase = f'-o False -e {e} -m {m}'

kindSpeach = 'kindSpeach'

partSeach = wordConverter.partSeachCategory()

for i in range(mc, mw):
    # print(i)
    if len(wordConverter.wordsNumbersList(False, 'all', i, 100000)) > 20:        
        for a in partSeach:
            # print(a, i)
            if len(wordConverter.wordsNumbersList(True, a, i, 100)) > 2:
                memoryName = f'-n {kindSpeach} -k {a} -c {i}'
                os.system(f'python neuralWordsNet.py -t True {couchbase} {memoryName}')
                # continue
if len(wordConverter.getKindMemories()) == 0: print('W sieci musi być zbudowana przynajmniej jedna pamięć!\nUżyj: neuralWordsNet.py')
else: print('Sieć została zbudowana. Gratulacje')
