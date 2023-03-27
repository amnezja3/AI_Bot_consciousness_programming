import wtf
import coffeeBrain as cf
# from os import system

# system('cls')
meaningBase = cf.coffeePls(True)[3]
wordsCorrecting = cf.coffeePls(False)[2]


def analitix(senten):
    # print(senten)
    sentSplit = str(senten).lower().split(' ')

    def prefixVerb(beg):
        beg = str(beg)
        beggs = ['z', 'w', 'o', 'u', 'po', 'za', 'do', 'od', 'na', 'wy', 'roz', 'pod', 'prze']
        begL = [beg, beg]
        for b in beggs:
            if beg.startswith(b):
                begL = [beg[len(b):], beg]
        return begL


    endes = [
                'iszecie', 'iszemy', 'ujesz', 'icie', 
                'ycie', 'acie', 'iszę', 'isze', 'dzie',
                'am', 'amy', 'asz',  'ają', 'cie', 'ecie', 'czy'
                'ał', 'ił', 'ało', 'iło', 'ła', 'ły', 'ło', 'ął',
                'czą', 'ną', 'dzi', 'ci', 'szy', 'dź', 'aż',
                'by', 'bym', 'byś', 'je', 'rze', 'rzy', 'ra', 
                'oi', 'ne', 'ją', 'ysz', 'ać', 'ić', 'isz', 'esz', 
                'że', 'ni', 'emy', 'imy', 'ymy', 'my',
                'rę', 'sz', 'eś', 'aś', 'erz', 'rzcie',
                'eć', 'ść', 'no', 'to', 'nia',
                'szy', 'ąc', 'uję', 'uje', 'li', 'em', 'cie',
                'a', 'ł', 'ą', 'ę', 'c', 'ć'
            ]


    pronouns = ['się', 'se', 'siebie', 'sobie']

    def clearThis(string):
        x = str(string)
        listCorrect = str(wordsCorrecting[x])\
            .replace('Słownik języka polskiego PWN', '')\
            .replace('Zobacz więcej wyników wyszukiwania w SJP', '')\
            .replace('Słownik języka polskieg', '')\
            .replace('Wielki słownik ortograficzny PWN', '')\
            .replace('Zobacz więcej wyników wyszukiwania w WSO', '')\
            .replace('Synonimy', '').replace('«', '').replace('»', '')\
            .replace('Podobne wyszukiwania', '').replace('##', '')\
            .split(';')
        return listCorrect

    nounWords = set()
    # adjectiveWords = set()
    # adverbWords = set()
    # conjunctionWords = set()
    # prepositionWords = set()
    # numeralWords = set()
    # pronounWords = set()
    verbsWords = set()

    for p in pronouns:
        countWords = 0
        for s in sentSplit:
            if p == s:
                # print(sentSplit[countWords - 1], sentSplit[countWords])
                try:
                    m = sentSplit[countWords - 1]
                    sneRco = str(meaningBase[m])
                    if sneRco.startswith('#cz.mowy#czasownik'):
                        verbsWords.add(m)
                        exp = f'meaning:{m}|#cz.mowy#czasownik;\n'
                        wtf.addQuestionAnswer(exp)
                        print(exp)
                except:
                    pass
            countWords += 1

    for m in sentSplit:
        try:
            sneRco = str(meaningBase[m])
            # if sneRco.startswith('#cz.mowy#rzeczownik'):
            #     nounWords.add(m)
            #     continue
            # if sneRco.startswith('#cz.mowy#przymiotnik'):
            #     adjectiveWords.add(m)
            #     continue
            # if sneRco.startswith('#cz.mowy#przysłówek'):
            #     adverbWords.add(m)
            #     continue
            # if sneRco.startswith('#cz.mowy#spójnik'):
            #     conjunctionWords.add(m)
            #     continue
            # if sneRco.startswith('#cz.mowy#przyimek'):
            #     prepositionWords.add(m)
            #     continue
            # if sneRco.startswith('#cz.mowy#zaimek'):
            #     pronounWords.add(m)
            #     continue
            # if sneRco.startswith('#cz.mowy#liczebnik'):
            #     numeralWords.add(m)
            #     continue
            if sneRco.startswith('#cz.mowy#czasownik'):
                verbsWords.add(m)
                continue 
        except:        
            if len(m) > 4:
                wordToCheck = m # prefixVerb(m)[0]
                STOP = False
                # if m == wordToCheck:
                #     wordToCheck = m
                rangeWord = len(wordToCheck)
                rangeSym = int(len(wordToCheck) * 0.5)
                for _ in range(rangeWord - rangeSym):
                    shortWord = wordToCheck[:rangeWord]
                    # print(shortWord)
                    for k, v in meaningBase.items():
                        for e in endes:
                            if str(v).startswith('#cz.mowy#czasownik') and \
                                str(k).count(shortWord) > 0 and str(m).endswith(e):
                                if str(k).startswith(prefixVerb(m)[0]):
                                    # print(m, k, v)
                                    exp = f'meaning:{m}|#cz.mowy#czasownik;\n'
                                    wtf.addQuestionAnswer(exp)
                                    verbsWords.add(k)
                                    STOP = True
                                    break
                                if str(k).startswith(prefixVerb(m)[1]):
                                    # print(m, k, v)
                                    exp = f'meaning:{m}|#cz.mowy#czasownik;\n'
                                    wtf.addQuestionAnswer(exp)
                                    verbsWords.add(k)
                                    STOP = True
                                    break
                        if STOP:
                            break
                    if STOP:
                            break

                        # if str(v).startswith('#cz.mowy#rzeczownik') and \
                        #     str(k).count(shortWord) > 0:
                        #     # print(m, k, v)
                        #     nounWords.add(k)                            
                        # if str(v).startswith('#cz.mowy#przymiotnik') and \
                        #     str(k).count(shortWord) > 0:
                        #     # print(m, k, v)
                        #     adjectiveWords.add(k)                            
                        # if str(v).startswith('#cz.mowy#przysłówek') and \
                        #     str(k).count(shortWord) > 0:
                        #     # print(m, k, v)
                        #     adverbWords.add(k)                            
                        # if str(v).startswith('#cz.mowy#przyimek') and \
                        #     str(k).count(shortWord) > 0:
                        #     # print(m, k, v)
                        #     prepositionWords.add(k)                            
                        # if str(v).startswith('#cz.mowy#zaimek') and \
                        #     str(k).count(shortWord) > 0:
                        #     # print(m, k, v)
                        #     pronounWords.add(k)                            
                        # if str(v).startswith('#cz.mowy#liczebnik') and \
                        #     str(k).count(shortWord) > 0:
                        #     # print(m, k, v)
                        #     numeralWords.add(k)
                    rangeWord -= 1

    # for x in verbsWords:
    #     try:      
    #         listMeaningCorrect = clearThis(x)
    #         # print(x + ' dla ', choice(listMeaningCorrect))
    #         print(x + ' dla ', str(listMeaningCorrect))
    #         print('co robi', x, meaningBase[x])
    #         # print(listMeaningCorrect)
    #         # for lis in listMeaningCorrect:
    #         #     print(lis)
    #     except: 
    #         # print(f'brak definicji dla {x}')
    #         print('co robi', x, meaningBase[x])


    # for x in nounWords:
    #     try:      
    #         listMeaningCorrect = clearThis(x)                
    #         # print(x + ' dla ', choice(listMeaningCorrect))
    #         # print(x + ' dla ', str(listMeaningCorrect))
    #         print('kto lub co', x, meaningBase[x])
    #         # print(listMeaningCorrect)
    #         # for lis in listMeaningCorrect:
    #         #     print(lis)            
    #     except: 
    #         # print(f'brak definicji dla {x}')
    #         print('kto lub co', x, meaningBase[x])
        
    # for x in adjectiveWords:
    #     try:      
    #         listMeaningCorrect = clearThis(x)                
    #         # print(x + ' dla ', choice(listMeaningCorrect))
    #         # print(x + ' dla ', str(listMeaningCorrect))
    #         print('jaki, jaka, jakie', x, meaningBase[x])
    #         # print(listMeaningCorrect)
    #         # for lis in listMeaningCorrect:
    #         #     print(lis)            
    #     except: 
    #         # print(f'brak definicji dla {x}')
    #         print('jaki, jaka, jakie', x, meaningBase[x])

    # for x in adverbWords:
    #     try:
    #         listMeaningCorrect = clearThis(x)                
    #         # print(x + ' dla ', choice(listMeaningCorrect))
    #         # print(x + ' dla ', str(listMeaningCorrect))
    #         print('kogo czego', x, meaningBase[x])
    #         # print(listMeaningCorrect)
    #         # for lis in listMeaningCorrect:
    #         #     print(lis)            
    #     except: 
    #         # print(f'brak definicji dla {x}')
    #         print('kogo czego', x, meaningBase[x])

    # for x in conjunctionWords:
    #     try:      
    #         listMeaningCorrect = clearThis(x)               
    #         # print(x + ' dla ', choice(listMeaningCorrect))
    #         # print(x + ' dla ', str(listMeaningCorrect))
    #         print('łączy się za pomocą', x, meaningBase[x])
    #         # print(listMeaningCorrect)
    #         # for lis in listMeaningCorrect:
    #         #     print(lis)            
    #     except: 
    #         # print(f'brak definicji dla {x}')
    #         print('łączy się za pomocą', x, meaningBase[x])

    # for x in prepositionWords:
    #     try:      
    #         listMeaningCorrect = clearThis(x)               
    #         # print(x + ' dla ', choice(listMeaningCorrect))
    #         # print(x + ' dla ', str(listMeaningCorrect))
    #         print('w jaki sposób, gdzie lub miejsce działania', x, meaningBase[x])
    #         # print(listMeaningCorrect)
    #         # for lis in listMeaningCorrect:
    #         #     print(lis)            
    #     except: 
    #         # print(f'brak definicji dla {x}')
    #         print('w jaki sposób, gdzie lub miejsce działania', x, meaningBase[x])

    # for x in numeralWords:
    #     try:      
    #         listMeaningCorrect = clearThis(x)               
    #         # print(x + ' dla ', choice(listMeaningCorrect))
    #         # print(x + ' dla ', str(listMeaningCorrect))
    #         print('ile, jak wile', x, meaningBase[x])
    #         # print(listMeaningCorrect)
    #         # for lis in listMeaningCorrect:
    #         #     print(lis)            
    #     except: 
    #         # print(f'brak definicji dla {x}')
    #         print('ile, jak wile', x, meaningBase[x])

    # for x in pronounWords:
    #     try:      
    #         listMeaningCorrect = clearThis(x)               
    #         # print(x + ' dla ', choice(listMeaningCorrect))
    #         # print(x + ' dla ', str(listMeaningCorrect))
    #         print('w jakim kierunku', x, meaningBase[x])
    #         # print(listMeaningCorrect)
    #         # for lis in listMeaningCorrect:
    #         #     print(lis)            
    #     except: 
    #         # print(f'brak definicji dla {x}')
    #         print('w jakim kierunku', x, meaningBase[x])

    # for p in verbsWords:
    #     countWords = 0
    #     for s in sentSplit:
    #         if p == s:
    #             try: PO = sentSplit[countWords - 1]
    #             except IndexError: PO = ''
    #             try: OR = sentSplit[countWords]
    #             except IndexError: OR = ''
    #             try: DO = sentSplit[countWords + 1]
    #             except IndexError: DO = ''
    #             try: OK = sentSplit[countWords + 2]
    #             except IndexError: OK = ''
    #             print(PO, OR, DO, OK)
    #         countWords += 1

    # for p in pronounWords:
    #     countWords = 0
    #     for s in sentSplit:
    #         if p == s:
    #             try: PO = sentSplit[countWords - 2]
    #             except IndexError: PO = ''
    #             try: OR = sentSplit[countWords - 1]
    #             except IndexError: OR = ''
    #             try: OK = sentSplit[countWords]
    #             except IndexError: OK = ''
    #             try: DO = sentSplit[countWords + 1]
    #             except IndexError: DO = ''
    #             print(PO, OR, OK, DO)            
    #         countWords += 1


analitix('Rissa przypomniała sobie swoją rodzinę. Miłość powiedziała stanowczo. W tej samej chwili płomienie zgasły. Dziewczyna pospiesznie wzięła klucz i ponownie poprzez zwierciadło wróciła do komnaty z kamiennymi drzwiami. Klucz włożyła do dziurki. Pasował idealnie. Ciężko było otworzyć drzwi, ale Rissa była silna. Ku jej zdumieniu w komnacie na srebrnym cokole leżał duży turkusowy kamień. Podniosła go - nie był wcale taki ciężki. Dokładnie go obejrzała. Był piękny Zastukała o powierzchnię znaleziska. Okazało się, że w środku nic nie ma. Ale jego powierzchnia była twarda niczym diament. Owinęła kamień w swój fartuch i powoli ruszyła po schodach. Zupełnie nie znała tej drogi. Zaczęła płakać, a łzy kapały strumieniami na ziemię. Nagle, spomiędzy kamiennych kafelków, zaczęły tryskać fontanny światła. Tajemniczy blask sunął na ścianę. W końcu ukazały się kolejne drzwi. Nie były jednak kamienne, tylko drewniane. Rissa otworzyła je z łatwością. W środku, na półkach leżały stare zwoje. Dziewczyka rozwinęła jeden z nich i przeczytała Rok 1290, 12 kwietnia. Wieźliśmy wielki skarb dla królowej elfów - Esterii. Gdy zatrzymaliśmy się w puszczy, by wypocząć, napadli na nas żołnierze króla. Jednak my - mędrcy byliśmy szybsi. Zabezpieczyliśmy wieżę zagadkami, aby skarb był bezpieczny... Spojrzała w dół. Na samym dole zwoju była mapa, a nad nią napis: Mapa prowadząca do królowej Esterii. I jeszcze plan wyjścia z wieży. Rissa wzięła zwój i z oczami utkwionymi w pergaminie schodziła po schodach. Nie zapomniała jednak o turkusowym kamieniu. Zawiązała go na plecach. Ze starym zwojem z łatwością wyszła z wieży. Potem skierowała się na południe, w stronę domu. Powiedziała rodzicom, że wybiera się na wyprawę, ale nie powiedziała dokąd. Zapakowała sporo prowiantu i wody. Turkusowy kamień włożyła do skórzanej torby. Gdy była gotowa, udała się na północ, choć obawiała się tej drogi. Na pergaminie widniały bowiem jeszcze takie słowa Gdzie mroźne góry, gdzie wilki zęby szczerzą, tam Piękna Pani ma swą siedzibę. Już sam fragment o mroźnych górach nie spodobał się jej, mimo to wyruszyła. Pora nie była już taka wczesna, zaczynało się ściemniać.')