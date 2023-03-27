def whatIsThat2(keyword):
    # inny słownik https://sjp.pl/zapominasz
    import requests
    urlAddress = f'https://sjp.pwn.pl/szukaj/{keyword}.html'
    phraseList = ['Słownik języka polskiego PWN', 'Wielki słownik ortograficzny PWN', 'Synonimy', 'Podobne wyszukiwania']
    phraseEndTAGList = ['Słownik języka polskiego pod red. W. Doroszewskiego', 'Słownik języka polskiego PWN', '</article>', '</div>']

    exp = []
    def searchString(url):
        r = requests.get(url)
        htmlSTR = r.text
        return htmlSTR

    with open('pwn.temps', 'w+', encoding='utf8') as pwn:
        pwn.write(searchString(urlAddress))


    return exp

def whatIsThat(keyword):
    import requests
    urlAddress = f'https://sjp.pwn.pl/szukaj/{keyword}.html'
    phraseList = ['Słownik języka polskiego PWN', 'Wielki słownik ortograficzny PWN', 'Synonimy', 'Podobne wyszukiwania']
    phraseEndTAGList = ['Słownik języka polskiego pod red. W. Doroszewskiego', 'Słownik języka polskiego PWN', '</article>', '</div>']

    EXPORT = []
    def searchString(url, faze):
        r = requests.get(url)
        htmlSTR = r.text
        lenhtmlSTR = len(htmlSTR)
        lenFaze = len(faze)
        export = []
        for i in range(lenhtmlSTR):
            x = i+lenFaze
            if faze == htmlSTR[i:x]:
                export.append((i, x))
        return export, htmlSTR

    for phrase in range(len(phraseList)):
        allHtml = searchString(urlAddress, phraseList[phrase])[1]
        try:partHtml = allHtml[searchString(urlAddress, phraseList[phrase])[0][0][1]+1:]
        except:break
        rangeStart =  len(allHtml[searchString(urlAddress, phraseList[phrase])[0][0][1]:])
        lenPhraseEnd = len(phraseEndTAGList[phrase])
        for x in range(rangeStart):
            if partHtml[x:x+lenPhraseEnd] == phraseEndTAGList[phrase]:
                closerTAGindex = searchString(urlAddress, phraseList[phrase])[0][0][0] + x + lenPhraseEnd+1
                break
        soupSelected = str(allHtml[searchString(urlAddress, phraseList[phrase])[0][0][1]:closerTAGindex])
        sS = soupSelected.split('<li>')
        valuesAi = []
        for s in sS:
            s=s.strip()
            s1 = s.split('>')
            for c in s1:
                c=c.strip()
                s2 = c.split('<')
                try:inti = int(s2[0][0])
                except:inti=True
                if s2[0] != '' and s2[0] != ', ' and s2[0] != ' ' and s2[0] != '•\xa0' and s2[0] != 'pot.' and s2[0] != '1.\xa0' and inti==True:
                    valuesAi.append(s2[0].strip())
        newBrain = {phraseList[phrase]:valuesAi}
        EXPORT.append(newBrain)
    return EXPORT



def partSpeech(word):
    import requests
    import config

    TMP_WIKI = str(config.brain('wiki'))


    url = f'https://pl.wiktionary.org/wiki/{word}'
    r = requests.get(url)
    htmlSTR = r.text
    exp = None
    fi=open(TMP_WIKI, 'w+', encoding='utf-8')
    for ch in htmlSTR:
        try:fi.write(ch)
        except:pass
    fi.close()
    fi=open(TMP_WIKI, 'r', encoding='utf-8')
    fil = fi.readlines()
    fi.close()
    ind = 0
    for f in fil:
        f = str(f)
        f = f.replace('<dl><dt><span class="field field-title fld-znaczenia field-pl" data-field="znaczenia" data-section-links="pl">', '')
        if f.startswith('znaczenia'):
            final = fil[ind+2].replace('<p><i>', '').replace('/i>', '').replace('<i>', '').strip().split('<')
            # print(len(final))
            # print(type(final))
            # print(final)
            exp='meaning:' + word + '|#cz.mowy#' + final[0] + ';'
            break
        ind +=1
    # print('sprawdzam wiki ..')
    return exp

def recognize(sentension):
    import config
    import coffeeBrain as cf
    import neuralWordsNet as nwn
    import wordConverter as wcn

    meaningWords = cf.coffeePls()[3]

    sentension = str(sentension)
    # Gdzie są moje książki? Kiedy będziesz budować dom? Czy twoje oczy są zmęczone?

    recognizeSentention = ''

    # jaka to częśc mowy
    clearSentence = config.clearCharacters(sentension.strip())

    ccQuest = 0
    ccComm = 0

    couQues = 0

    sens = clearSentence.split(' ')
    commandTrue = False
    for r in sens:
        quesJests = [
                    'kto', 'co','jaki','który','gdzie','kiedy','jak','komu','czemu','czy',
                    'jakie','jaka','dlaczego','kim','skąd','dokąd','odkąd','jakiego','czym','czego',
                    'jakich','którędy'
                    ]
        for qj in quesJests:
            if r == qj:
                couQues +=1
                break
        for m in meaningWords.keys():
            if m == r:
                couQues += str(meaningWords[m]).strip().count('pyt')
                # w2 = sentension.count('kto '); w3 = sentension.count('co ')
                # w4 = sentension.count('jaki '); w5 = sentension.count('który ')
                # w6 = sentension.count('gdzie'); w7 = sentension.count('kiedy ')
                # w8 = sentension.count('jak '); w9 = sentension.count('komu ')
                # w10 = sentension.count('czemu '); w11 = sentension.count('kogo ')
                # w12 = sentension.count('czy '); w13 = sentension.count('jakie ')
                # w14 = sentension.count('jaka ');w15 = sentension.count('dlaczego ')
                # w16 = sentension.count('kim ')
                # couQues = w1+w2+w3+w4+w5+w6+w7+w8+w9+w10+w11+w12+w13+w14+w15+w16
                if couQues > 0:
                    ccQuest += 1
                if sentension.endswith('?') or sentension.endswith('znak zapytania'):
                    ccQuest += 1
                verbCommand = str(whatWhoVerb(m)).count('- TY tryb rozkazujacy')
                # print(whatWhoVerb(m))
                if sentension.endswith('!') or sentension.endswith('wykrzyknik'):
                    ccComm += 1
                elif verbCommand > 0:
                    commandTrue = True
                    ccComm += 1
    if ccQuest > 0:
        recognizeSentention = 'question:'
    if commandTrue:
        recognizeSentention = 'command:'
    if ccComm > 0 and recognizeSentention != 'question:':
        recognizeSentention = 'command:'
    if recognizeSentention != 'question:' and recognizeSentention != 'command:':
        recognizeSentention = 'explain:'

    wordsInSentence = clearSentence.strip().split(' ')
    countMeaning = 0
    for w in wordsInSentence:
        for psl in meaningWords.keys():
            psl = str(psl)
            psV = str(meaningWords[psl]).replace('#cz.mowy#', '')
            if psl == w.strip():
                countMeaning += 1
                recognizeSentention += w.strip() + ' > ' + psV.strip()

    for h in sens:
        for k in meaningWords.keys():
            if k == h:
                psV = str(meaningWords[k]).replace('#cz.mowy#', '')
                # psV.startswith('partykuła') or psV.startswith('przyimek') or psV.startswith('zaimek')
                if k == 'z' or k == 'do' or k == 'na' or k == 'bez' or k == 'za' or k == 'pod'\
                or k == 'u' or k == 'w' or k == 'nad' or k == 'o' or k == 'od' or k == 'ze' or k == 'po'\
                or k == 'znad' or k == 'przez' or k == 'poprzez' or k == 'uprzednio' or k == 'ewidentnie'\
                or k == 'następnie' or k == 'poprzednio' or k == 'poza' or k == 'później' or k == 'wcześniej'\
                or k == 'się' or k == 'siebie' or k == 'se' or k == 'sobie' or k == 'wam' or k == 'nie' or k == 'tak'\
                or psV.startswith('przyimek') or psV.startswith('spójnik'):
                    recognizeSentention += '*okolicznik+' + h.strip()
                elif psV.startswith('czasownik'):
                    recognizeSentention += '*orzeczenie+' + h.strip()
                # psV.count('mianownik') > 0 or psV.startswith('rzeczownik')
                elif psV.startswith('rzeczownik') or psV.startswith('zaimek osobowy')\
                    or psV.startswith('zaimek, forma fleksyjna') or psV.startswith('zaimek dzierżawczy')\
                        or psV.startswith('zaimek;') or psV.startswith('zaimek wskazujący'):
                    recognizeSentention += '*podmiot+' + h.strip()

                elif psV.startswith('przymiotnik') or psV.startswith('liczebnik'):
                    recognizeSentention += '*przydawka+' + h.strip()
                # or psV.startswith('spójnik')
                elif psV.startswith('przysłówek') or psV.startswith('zaimek pyt'):
                    recognizeSentention += '*dopełnienie+' + h.strip()
                

                

                
                # '''
                # przyimki proste (np. z, do, na, bez, za, pod, u, w, nad, o, od, po).
                # przyimki złożone, składające się z przyimków prostych (np. z + nad = znad, po + przez = poprzez).
                # '''
    # # sieć neuronowa 
    # judgment = recognizeSentention.count('orzeczenie')
    # subject = recognizeSentention.count('podmiot')
    # attributive = recognizeSentention.count('przydawka')
    # complement = recognizeSentention.count('dopełnienie')
    # circumstantial = recognizeSentention.count('okolicznik')

    # testingList = wcn.getDataForWord(sens)
    # effectAI = nwn.neuralNet(testingList, None, None, None, None, 'kindSpeach', None, None)

    # if judgment == 0:
    #     for h in effectAI:
    #         if h[0] == 'czasownik':
    #             recognizeSentention += '*orzeczenie+' + str(h[1]).strip()
    # if subject == 0:
    #     for h in effectAI:
    #         if h[0] == 'rzeczownik' or h[0] == 'zaimek' or h[0] == 'imiesłów':
    #             recognizeSentention += '*podmiot+' + str(h[1]).strip()
    # if attributive == 0:
    #     for h in effectAI:
    #         if h[0] == 'liczebnik' or h[0] == 'przymiotnik':
    #             recognizeSentention += '*przydawka+' + str(h[1]).strip()
    # if complement == 0:
    #     for h in effectAI:
    #         if h[0] == 'przysłówek':
    #             recognizeSentention += '*dopełnienie+' + str(h[1]).strip()
    # if circumstantial == 0:
    #     for h in effectAI:
    #         if h[0] == 'spójnik':
    #             recognizeSentention += '*okolicznik+' + str(h[1]).strip()

    # ['podmiot', 'orzeczenie', 'przydawka', 'dopełnienie', 'okolicznik']
    # print('generuję recognizeSentention ..')
    return recognizeSentention

def analiticRecognization(recognition):
    recognition = str(recognition)
    setWEB = {'przydawka' : '', 'dopełnienie' : '', 'podmiot' : '', 'orzeczenie' : '', 'okolicznik' : ''}
    recList = recognition.replace('question:', '').replace('explain:', '').split(';')
    for rec in recList:
        if rec.startswith('*'):
            re = rec.split('*')
            for r in re:
                wordandpart = r.split('+')
                if wordandpart[0].startswith('podmiot'):
                    setWEB['podmiot'] = setWEB['podmiot'] + wordandpart[1] + ' '
                    continue
                if wordandpart[0].startswith('orzeczenie'):
                    setWEB['orzeczenie'] = setWEB['orzeczenie'] + wordandpart[1] + ' '
                    continue
                if wordandpart[0].startswith('przydawka'):
                    setWEB['przydawka'] = setWEB['przydawka'] + wordandpart[1] + ' '
                    continue
                if wordandpart[0].startswith('dopełnienie'):
                    setWEB['dopełnienie'] = setWEB['dopełnienie'] + wordandpart[1] + ' '
                    continue
                if wordandpart[0].startswith('okolicznik'):
                    setWEB['okolicznik'] = setWEB['okolicznik'] + wordandpart[1] + ' '
                    continue
    return setWEB

def addQuestionAnswer(answer):
    import config
    # print('Zapisuję addQuestionAnswer ..')
    BRAIN_FILE_ADDRESS = str(config.brain('brain'))
    with open(BRAIN_FILE_ADDRESS, 'a+', encoding='utf-8') as f:
        f.write(answer)
    # f = open(BRAIN_FILE_ADDRESS, 'a+')
    # f.write(answer)
    # f.close()

def clearThis(string):
    import coffeeBrain as cf
    wordsCorrecting = cf.coffeePls(False)[2]
    x = str(string)
    try: wordsCorrecting[x]
    except KeyError: return []
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

def sayIt(say = "Opening .. please wait .. \nInstantion is running now ..", language = 0):
    import pyttsx3
    from googletrans import Translator
    translator = Translator()

    if language == 0:
        # Polski
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", 128)
            engine.setProperty("volume", 8)
            v= engine.getProperty("voices")
            engine.setProperty("voice", v[0].id)
            engine.say(str(say))
            engine.runAndWait()
        except:
            say = say
        return say
    if language == 1:
        # Ang
        try:
            transEnPl = translator.translate(say, src='pl', dest='en')
            strEN = str(transEnPl).split('text=')[1].split(', pronunciation=')[0]

            engine = pyttsx3.init()
            engine.setProperty("rate", 128)
            engine.setProperty("volume", 8)
            v= engine.getProperty("voices")
            engine.setProperty("voice", v[1].id)
            engine.say(str(strEN))
            engine.runAndWait()
        except:
            engine = pyttsx3.init()
            engine.setProperty("rate", 128)
            engine.setProperty("volume", 8)
            v= engine.getProperty("voices")
            engine.setProperty("voice", v[0].id)
            engine.say(str(say))
            engine.runAndWait()
            strEN = say
        return strEN
    if language == 2:
        # Other
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", 128)
            engine.setProperty("volume", 8)
            v= engine.getProperty("voices")
            engine.setProperty("voice", v[0].id)
            engine.say(str(say))
            engine.runAndWait()
        except:
            say = say
        return say

def mathRule(parse):
    print(parse)
    questAll = str(parse)
    questMath = questAll.replace('ile to jest ', '').replace('podzielić przez', '/')\
    .replace('podzielić na', '/').replace('pomnożyć przez', '*').replace('razy', '*')\
    .replace('plus', '+').replace('dodać', '+').replace('odjąć', '-').replace('minus', '-')\
    .replace('x', '*')
    if questMath.count('/') > 0:
        questMathPlus = questMath.split('/')
        dec = 0
        adderIndex = 1
        for p in range(len(questMathPlus)):
            # print(p, type(questMathPlus[p]))
            # print(p, questMathPlus)
            if dec != 0:
                try: dif = float(dec / float(questMathPlus[adderIndex].strip()))
                except:
                    continue
                'Błąd rozpoznania liczb.. 1Przykro mi!'
            else:
                try: dif = float(float(questMathPlus[p].strip()) / float(questMathPlus[adderIndex].strip()))
                except:
                    continue
                'Błąd rozpoznania liczb.. 2Przykro mi!'
            # print(dec, dif)
            dec = dif
            adderIndex += 1
        currentlySubject = str(dec)
        return currentlySubject
    elif questMath.count('*') > 0:
        questMathPlus = questMath.split('*')
        sum = 1
        for multi in questMathPlus:
            try: multi = float(multi.strip())
            except:
                continue
            'Błąd rozpoznania liczb.. Przykro mi!'
            sum *= multi
        currentlySubject = str(sum)
        return currentlySubject
    elif questMath.count('+') > 0:
        questMathPlus = questMath.split('+')
        sum = 0
        for plus in questMathPlus:
            try: plus = float(plus.strip())
            except:
                continue
            'Błąd rozpoznania liczb.. Przykro mi!'
            sum += plus
        currentlySubject = str(sum)
        return currentlySubject
    elif questMath.count('-') > 0:
        questMathPlus = questMath.split('-')
        sum = float(questMathPlus[0])
        for m in range(len(questMathPlus)):
            if m == 0:
                continue
            try: minus = float(questMathPlus[m].strip())
            except:
                continue
            'Błąd rozpoznania liczb.. Przykro mi!'
            sum -= minus
        currentlySubject = str(sum)
        return currentlySubject
    else: return questAll


def leanguageDetector(detect):
    from googletrans import Translator
    translator = Translator()
    universal = detect

    try:
        detector = translator.detect(universal)
        strDetector = str(detector).replace('Detected(lang=', '').split(', confidence=')[0]
    except:
        strDetector = 'pl'


    # print(strDetector)
    if strDetector == 'pl':
        srce = strDetector
        deste = strDetector
        speak = 0

    elif strDetector == 'en':
        srce = strDetector
        deste = 'pl'
        speak = 1

    else:
        srce = strDetector
        deste = 'pl'
        speak = 2

    try:
        transEnPl = translator.translate(universal, src=srce, dest=deste)
        strL = str(transEnPl).split('text=')[1].split(', pronunciation=')[0]
    except:
        strL = universal
    return strL, speak

def whatSentention(sentention):
    sentention = str(sentention)
    # print(sentention)
    '''
    polskim wyróżnia się:
    spójniki współrzędne (parataktyczne):
    łączne, np. a, i, oraz, tudzież
    rozłączne, np. albo, bądź, czy, lub
    wykluczające, np. ani, ni
    przeciwstawne, np. a, aczkolwiek, ale, jednak, lecz, natomiast, zaś
    wyjaśniające, np. czyli, mianowicie, ponieważ, to jest
    wynikowe, np. dlatego, i, przeto, tedy, więc, zatem, toteż
    spójniki podrzędne (hipotaktyczne), np. aby, bowiem, choć, czy, jeżeli, ponieważ, że.
    '''
    categoryS = {
        'łączne' : [],
        'rozłączne' : [],
        'wykluczające' : [],
        'przeciwstawne' : [],
        'wyjaśniające' : [],
        'wynikowe' : [],
        'hipotaktyczne' : [],

        'sentention' : sentention
             }

    a = sentention.count(' a ')
    i = sentention.count(' i ')
    oraz = sentention.count(' oraz ')
    tudziez = sentention.count(' tudzież ')
    laczne = a + i + oraz + tudziez
    if laczne > 0:
        exp = f'łączne, a({a}), i({i}), oraz({oraz}), tudzież({tudziez})'
        # print(exp)
        if a > 0: categoryS['łączne'] = categoryS['łączne'] + [' a ']
        if i > 0: categoryS['łączne'] = categoryS['łączne'] + [' i ']
        if oraz > 0: categoryS['łączne'] = categoryS['łączne'] + [' oraz ']
        if tudziez > 0: categoryS['łączne'] = categoryS['łączne'] + [' tudzież ']

    albo = sentention.count(' albo ')
    badz = sentention.count(' bądź ')
    czy = sentention.count(' czy ')
    lub = sentention.count(' lub ')
    rozlaczne = albo + badz + czy + lub
    if rozlaczne > 0:
        exp = f'rozłączne, albo({albo}), bądź({badz}), czy({czy}), lub({lub})'
        # print(exp)
        if albo > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + [' albo ']
        if badz > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + [' bądź ']
        if czy > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + [' czy ']
        if lub > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + [' lub ']

    ani = sentention.count(' ani ')
    ni = sentention.count(' ni ')
    wykluczajace = ani + ni
    if wykluczajace > 0:
        exp = f'wykluczające, ani({ani}), ni({ni})'
        # print(exp)
        if ani > 0: categoryS['wykluczające'] = categoryS['wykluczające'] + [' ani ']
        if ni > 0: categoryS['wykluczające'] = categoryS['wykluczające'] + [' ni ']

    aP = sentention.count(' a ')
    aczkolwiek = sentention.count(' aczkolwiek ')
    ale = sentention.count(' ale ')
    jednak = sentention.count(' jednak ')
    lecz = sentention.count(' lecz')
    natomiast = sentention.count(' natomiast ')
    zas = sentention.count(' zaś ')
    przeciwstawne = aP + aczkolwiek + ale + jednak + lecz + zas
    if przeciwstawne > 0:
        exp = f'przeciwstawne, np. a({aP}), aczkolwiek({aczkolwiek}), ale({ale}), jednak({jednak}), lecz({lecz}), natomiast({natomiast}), zas({zas})'
        # print(exp)
        if aP > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' a ']
        if aczkolwiek > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' aczkolwiek ']
        if ale > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' ale ']
        if jednak > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' jednak ']
        if lecz > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' lecz ']
        if natomiast > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' natomiast ']
        if zas > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' zaś ']

    czyli = sentention.count(' czyli ')
    mianowicie = sentention.count(' mianowicie')
    poniewaz = sentention.count(' ponieważ ')
    tojest = sentention.count(' to jest ')
    wyjasniajace = czyli + mianowicie + poniewaz + tojest
    if wyjasniajace > 0:
        exp = f'wyjaśniające, czyli({czyli}), mianowicie({mianowicie}), poniewaz({poniewaz}), to jest({tojest})'
        # print(exp)
        if czyli > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + [' czyli ']
        if mianowicie > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + [' mianowicie ']
        if poniewaz > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + [' ponieważ ']
        if tojest > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + [' to jest ']

    dlatego = sentention.count(' dlatego ')
    iW = sentention.count(' i ')
    przeto = sentention.count(' przeto ')
    tedy = sentention.count(' tedy ')
    wiec = sentention.count(' więc ')
    zatem = sentention.count(' zatem ')
    totez = sentention.count(' toteż ')
    bo = sentention.count(' bo ')
    wynikowe = dlatego + iW + przeto + tedy + wiec + zatem + totez + bo
    if wynikowe > 0:
        exp = f'wynikowe, dlatego({dlatego}), i({iW}), przeto({przeto}), tedy({tedy}) wiec({wiec}) zatem({zatem}) toteż({totez}) '
        # print(exp)
        if dlatego > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' dlatego ']
        if iW > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' i ']
        if przeto > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' przeto ']
        if tedy > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' tedy ']
        if wiec > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' więc ']
        if zatem > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' zatem ']
        if totez > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' toteż ']
        if bo > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' bo ']

    aby = sentention.count(' aby ')
    bowiem = sentention.count(' bowiem ')
    choc = sentention.count(' choć ')
    czyP = sentention.count(' czy ')
    jezeli = sentention.count(' jeżeli ')
    poniewaz = sentention.count(' ponieważ ')
    ze = sentention.count(' że ')
    podrzedne = aby+ bowiem + choc + czyP + jezeli + poniewaz + ze
    if podrzedne > 0:
        exp = f'spójniki podrzędne (hipotaktyczne), np. aby({aby}), bowiem({bowiem}), choć({choc}) czy({czyP}) jeżeli({jezeli}) ponieważ({poniewaz}) że({ze}) '
        # print(exp)
        if aby > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' aby ']
        if bowiem > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' bowiem ']
        if choc > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' choć ']
        if jezeli > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' jeżeli ']
        if poniewaz > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' ponieważ ']
        if ze > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' że ']
    return categoryS

def splitSententionNum(sentention):
    sentention = str(sentention)
    # print(sentention)
    exp = set()
    whatWho = whatSentention(sentention)
    for k, v in whatWho.items():
        if len(whatWho[k]) > 0 and k != 'sentention':
            for a in v:
                exp.add(a)
    for b in exp:
        sentention = sentention.replace(b, f'|{b}').replace(',', '|').replace('||', '|')
    expA = sentention.split('|')
    return expA, exp, whatWho

def usersBase(username):
    import os
    usersFilesDir = os.listdir('./users')
    noUser = True
    for u in usersFilesDir:
        user_in_file = u.replace('user_', '').replace('.neural', '')
        if username == user_in_file:
            noUser = False
            continue
    if noUser:
        with open(f'./users/user_{username}.neural', 'w', encoding='utf-8') as userFile:
            userinfos = f'user_name:{username}\n'
            userFile.write(userinfos)
    with open(f'./users/user_{username}.neural', 'r', encoding='utf-8') as userFile:
        userContent = userFile.readlines()
    expList = []
    for x in userContent:
        x = x.strip()
        if x.startswith('user_name:') or x.startswith('task_id:'):
            expList.append(x)
    userData = {}
    for a in expList:
        a = str(a)
        if a.startswith('task_id:'):
            aa = a.split('|')
            userData[int(aa[0].replace('task_id:', ''))] = [aa[1]] + [b for b in aa[2:]]
        if a.startswith('user_name:'):
            un = a.split(':')[1]
            userData['USER_NAME'] = un
    return userData

def usersBaseLastId(username):
    userData = usersBase(username)
    cKey = 1
    for k in userData.keys():
        try: int(k)
        except: continue
        cKey += 1
    return cKey

def usersBaseUpdate(username, senten):
    userData = usersBase(username)
    cKey = 0
    for k in userData.keys():
        try: int(k)
        except: continue
        cKey += 1

    newKey = cKey + 1
    with open(f'./users/user_{username}.neural', 'a+', encoding='utf-8') as userFile:
        exp = f'task_id:{newKey}|{senten}\n'
        userFile.write(exp)

def userBaseDictionary(user_Name):
    TALKS_WE = {}
    userHistoryBase = usersBase(user_Name)
    for k_US, v_US in userHistoryBase.items():
        # print(type(v_US[0]))
        try: int(k_US)
        except: continue
        # f'USER*{questAllTRUE_FALSE}@OR${OR_U_data}>OR:{OR_U}@OR$@PO${PO_U_data}>PO:{PO_U}@PO$@PR$[]>PR:{PR_U}@PR$@DO$[]>DO:{DO_U}@DO$@OK${OK_U_data}>OK:{OK_U}@OK$^' + talksUser
        consen = v_US[0]
        WE_WHO = consen.split('*')[0]
        WE_TRUE_FALSE = consen.split('*')[1].split('@')[0]

        WE_OR = consen.split('@OR$')[1]
        WE_OR_EX = WE_OR.split('>OR:')[0]
        WE_OR_WORDS_LIST = WE_OR.split('>OR:')[1].strip().split(' ')

        WE_PO = consen.split('@PO$')[1]
        WE_PO_EX = WE_PO.split('>PO:')[0]
        WE_PO_WORDS_LIST = WE_PO.split('>PO:')[1].strip().split(' ')

        WE_PR = consen.split('@PR$')[1]
        WE_PR_EX = WE_PR.split('>PR:')[0]
        WE_PR_WORDS_LIST = WE_PR.split('>PR:')[1].strip().split(' ')

        WE_DO = consen.split('@DO$')[1]
        WE_DO_EX = WE_DO.split('>DO:')[0]
        WE_DO_WORDS_LIST = WE_DO.split('>DO:')[1].strip().split(' ')

        WE_OK = consen.split('@OK$')[1]
        WE_OK_EX = WE_OK.split('>OK:')[0]
        try: WE_OK_WORDS_LIST = WE_OK.split('>OK:')[1].strip().split(' ')
        except: WE_OK_WORDS_LIST = []

        coma_dot_counter = consen.split('^#^')[1].count(';')
        # print(coma_dot_counter)
        if coma_dot_counter > 1:
            range_coma_dot = len(consen.split('^#^')[1]) - 2
        else: 
            range_coma_dot = len(consen.split('^#^')[1]) -1
        # print(range_coma_dot)

        talks_section = consen.split('^#^')[1][:range_coma_dot].split(';')
        # print(range_coma_dot)
        WE_TALKS_SECTIONS_DETAILS = []
        WE_TALKS_SECTIONS_CONTENT = []
        for itNow in talks_section:
            # print(k_US)
            # print(itNow)
            # print(len(itNow))
            exp_1 = itNow.split('$$$')[0].split('###')
            exp_2 = itNow.split('$$$')[1].split('^^^')
            # print(exp_1)
            # print(exp_2)
            WE_TALKS_SECTIONS_DETAILS.append(exp_1)
            WE_TALKS_SECTIONS_CONTENT.append(exp_2)

        
        TALKS_WE[k_US] = {
            'WHO' : WE_WHO, 
            'TRUE_FALSE' : WE_TRUE_FALSE, 
            'OR_EX' : WE_OR_EX, 
            'OR_WORDS_LIST' : WE_OR_WORDS_LIST, 
            'PO_EX' : WE_PO_EX, 
            'PO_WORDS_LIST' : WE_PO_WORDS_LIST,  
            'PR_EX' : WE_PR_EX, 
            'PR_WORDS_LIST' : WE_PR_WORDS_LIST,  
            'DO_EX' : WE_DO_EX, 
            'DO_WORDS_LIST' : WE_DO_WORDS_LIST,  
            'OK_EX' : WE_OK_EX, 
            'OK_WORDS_LIST' : WE_OK_WORDS_LIST, 
            'TALKS_SECTIONS_DETAILS' : WE_TALKS_SECTIONS_DETAILS,
            'TALKS_SECTIONS_CONTENT' : WE_TALKS_SECTIONS_CONTENT}
    return TALKS_WE

def prefixVerb(beg):
    beg = str(beg)
    beggs = [
        'za', 'ze', 'z', 'we', 'wy', 'wł', 'w', 'od', 'o', 'upo', 'u', 'pod', 'poprze', 'po', 'prze', 
        'do', 'na', 'roz', 're'
        ]
    begL = [beg, beg]
    for b in beggs:
        if beg.startswith(b):
            begL = [beg[len(b):], beg]
            break
    return begL

def meaningpPartDetector(word):
    import coffeeBrain as cf
    meaningWords = cf.coffeePls()[3]
    with open('odm.neural', 'r', encoding='utf-8') as wordsFile:
        allwords = wordsFile.readlines()

    word # = 'pesymistyczne'
    word_1 = {}
    wordsCleaner = set()
    for w in allwords:
        ishere = w.startswith(f'{word}, ')
        if ishere == False:
            ishere_C = w.count(f' {word}, ')
        if ishere_C == 0:
            ishere_E = w.endswith(f', {word}')
        if ishere or ishere_E or ishere_C > 0:
            ww = w.strip().split(', ')
            word_finded = ww[0]
            try:
                kindMeaning = meaningWords[word_finded]
                # print(kindMeaning)
                word_finded = ww[0]
                for w in ww:
                    wordsCleaner.add(w)
                word_1[kindMeaning + f'odmiana dla {word_finded};'] =  [i for i in wordsCleaner]
            except:
                # continue
                # print(f'brak cz. mowy {word_finded}')
                regonMeaning = partSpeech(word_finded)
                if regonMeaning != None:
                    regonM = regonMeaning.split('|')[1]
                    for w in ww:
                        wordsCleaner.add(w)
                    word_1[regonM + f'odmiana dla {word_finded};'] =  [i for i in wordsCleaner]
                else:
                    continue
        ishere = 0
    for key, words in word_1.items():
        for w in words:
            try:
                meaningWords[w]
                continue
            except:
                newCommand = f'meaning:{w}|{key}\n'
                # print(newCommand)
                addQuestionAnswer(newCommand)

    cf.coffeePls()
    return word_1



def analitixVERB(senten):
    import coffeeBrain as cf
    meaningBase = cf.coffeePls(False)[3]
    sentSplit = str(senten).lower().split(' ')

    endes = [
        # 'lił', 'cie', 'uje', 'yli', 'ysz', 'esz', 'dzi', 'yły',
        # 'uję', 'iły', 'ię', 'cę', 'ać', 'yć', 'bym',
        # 'est', 'szę', 'lę', 'ądź', 'ali',
        # 'ieć', 'by', 'mij', 'byś', 'czę', 'iła',
        # 'asz', 'iń', 'uj',  'ieź', 'ieś',

        'ił', 'cie', 'ów', 'uje', 'yli', 'ysz', 'esz', 'żę', 'ić', 'li', 'ały', 'dzi', 'yły', 'gł', 'sł',
        'eś', 'my', 'uję', 'iły', 'ię', 'cę', 'rze', 'el', 'ać', 'yć', 'aż', 'bym', 'je', 'jestem', 'a',
        'ał', 'est', 'isz', 'będę', 'aj', 'ła', 'ała', 'si', 'em', 'ło', 'szę', 'lę', 'dzą', 'ądź', 'ali',
        'ąc', 'ieć', 'by', 'mij', 'byś', 'czę', 'ją', 'am', 'adź', 'ób', 'iła', 'eź', 'ne', 'rzy', 'oł',
        'edz', 'na', 'oi', 'gę', 'asz', 'iń', 'uj', 'ań', 'um', 'wi' ,'szcz', 'lcz', 'weź', 'ieź', 'ieś',
        'el', 'ap'
    ]

    pronouns = ['się', 'se', 'siebie', 'sobie']

    verbsWords = set()
    for p in pronouns:
        countWords = 0
        for s in sentSplit:
            # print(s)
            if p == s:
                # print(sentSplit[countWords - 1], sentSplit[countWords])
                try:
                    m = sentSplit[countWords - 1]
                    try: sneRco = str(meaningBase[m])
                    except KeyError: sneRco = "False"
                    if sneRco.startswith('#cz.mowy#czasownik'):
                        verbsWords.add(m)
                    if sneRco == "False":
                        exp = f'meaning:{m}|#cz.mowy#czasownik;\n'
                        addQuestionAnswer(exp)
                        # print(exp)
                except IndexError:
                    pass
            countWords += 1
    versTemp = []
    for k, v in meaningBase.items():
        k = str(k); v = str(v)
        if str(v).startswith('#cz.mowy#czasownik'):
            versTemp.append(k)
        if str(v).startswith('#cz.mowy#rzeczownik'):
            for s in sentSplit:
                m = prefixVerb(s)[0][:int(len(s) * 0.375)]
                cK = k.count(m)
                if cK > 0:
                    # print(k)
                    versTemp.append(k)

    for m in sentSplit:
        try:
            sneRco = str(meaningBase[m])
            # print(m, 'jest ok')
            if sneRco.startswith('#cz.mowy#czasownik'):
                verbsWords.add(m)
                continue
        except:
            if len(m) > 4:
                wordToCheck = m
                # print(m, 'pracuję')
                wordM = prefixVerb(m)[0]
                wordOrginal = prefixVerb(m)[1]
                STOP = False
                rangeWord = len(wordToCheck)
                rangeSym = int(len(wordToCheck) * 0.50)
                tempListKeys = []
                modifiM = prefixVerb(s)[0]
                for tem in versTemp:
                    if tem.count(modifiM[:rangeSym]):
                        tempListKeys.append(tem)
                        # print(tem)
                        # print(modifiM[:rangeSym])


                for _ in range(rangeWord - rangeSym):
                    shortWord = wordM[:rangeWord]
                    for k in tempListKeys:
                        for e in endes:
                            # print(k, m, wordM[:rangeWord], wordOrginal[:rangeWord], shortWord, e)

                            if str(k).count(shortWord) > 0 and str(m).endswith(e):
                                if str(k).count(wordM[:rangeWord]) > 0:

                                    exp = f'meaning:{m}|#cz.mowy#czasownik;\n'
                                    addQuestionAnswer(exp)
                                    # print(k, shortWord, wordM[:rangeWord])
                                    print(exp)
                                    verbsWords.add(k)
                                    STOP = True
                                    break
                                elif str(k).count(wordOrginal[:rangeWord]) > 0:

                                    exp = f'meaning:{m}|#cz.mowy#czasownik;\n'
                                    addQuestionAnswer(exp)
                                    # print(k, shortWord, wordOrginal[:rangeWord])
                                    print(exp)
                                    verbsWords.add(k)
                                    STOP = True
                                    break
                        if STOP:
                            break
                    rangeWord -= 1
                    if STOP:
                        break
    return verbsWords

def whatWhoVerb(xSentenceVerbs):
    import positionSimulation as position
    import coffeeBrain as cf
    meaningBase = cf.coffeePls(False)[3]
    xSentenceVerbs = str(xSentenceVerbs)
    words = xSentenceVerbs.split(' ')

    export = []

    for k in words:
        exp = []
        try: v = meaningBase[k]
        except KeyError: v = '#cz.mowy#UNK'
        if str(v).startswith('#cz.mowy#czasownik'):
            if str(k).endswith('am') or str(k).endswith('my') or str(k).endswith('ysz') or str(k).endswith('cie')\
            or str(k).endswith('a') or str(k).endswith('si') or str(k).endswith('ał') or str(k).endswith('ił')\
            or str(k).endswith('ło') or str(k).endswith('iła') or str(k).endswith('ała') or str(k).endswith('ię')\
            or str(k).endswith('ją') or str(k).endswith('li') or str(k).endswith('ały') or str(k).endswith('yły')\
            or str(k).endswith('yli') or str(k).endswith('ali') or str(k).endswith('je') or str(k).endswith('rze')\
            or str(k).endswith('oi') or str(k).endswith('ła') or str(k).endswith('gł') or str(k).endswith('oł')\
            or str(k).endswith('oi') or str(k).endswith('oi') or str(k).endswith('ać') or str(k).endswith('esz')\
            or str(k).endswith('dzą') or str(k).endswith('rzy') or str(k).endswith('uję') or str(k).endswith('isz')\
            or str(k).endswith('ieć') or str(k).endswith('asz') or str(k).endswith('est') or str(k).endswith('yć')\
            or str(k).endswith('będę') or str(k).endswith('gę') or str(k).endswith('ób') or str(k).endswith('cę')\
            or str(k).endswith('em') or str(k).endswith('czę') or str(k).endswith('lę') or str(k).endswith('eś')\
            or str(k).endswith('aj') or str(k).endswith('ądź') or str(k).endswith('edz') or str(k).endswith('eź')\
            or str(k).endswith('mij') or str(k).endswith('ów') or str(k).endswith('aż') or str(k).endswith('byś')\
            or str(k).endswith('bym') or str(k).endswith('sł') or str(k).endswith('szę') or str(k).endswith('uj')\
            or str(k).endswith('iń') or str(k).endswith('ań') or str(k).endswith('um') or str(k).endswith('wi')\
            or str(k).endswith('szcz') or str(k).endswith('lcz') or str(k).endswith('weź') or str(k).endswith('ieź')\
            or str(k).endswith('ieś') or str(k).endswith('adź') or str(k).endswith('el') or str(k).endswith('ap')\
            or str(k).endswith('są') or str(k).endswith('aś') or str(k).endswith('ucz') or str(k).endswith('erz')\
            or str(k).endswith('om') or str(k).endswith('yśl') or str(k).endswith('nów') or str(k).endswith('nij')\
            or str(k).endswith('ńcz') or str(k).endswith('ącz'):
                if str(k).endswith('am') or str(k).endswith('uję') or str(k).endswith('będę') or str(k).endswith('gę')\
                or str(k).endswith('żę') or str(k).endswith('jestem')  or str(k).endswith('szę') or str(k).endswith('cę')\
                or str(k).endswith('em') or str(k).endswith('ię') or str(k).endswith('czę') or str(k).endswith('lę')\
                or str(k).endswith('bym') :
                    meNow = position.positionUnVerb(k)
                    exp = [k, '- JA TY -', meNow]
                    if str(k).endswith('uję')  or str(k).endswith('szę') or str(k).endswith('gę') or str(k).endswith('cę')\
                    or str(k).endswith('czę') or str(k).endswith('lę'):
                        exp = [k, '- JA aspekt nie dokonany czas teraźniejszy TY -' , meNow]
                        if str(k).startswith('z') or str(k).startswith('wy') or str(k).startswith('prze')\
                        or str(k).startswith('za') or str(k).startswith('u') or str(k).startswith('do')\
                        or str(k).startswith('od') or str(k).startswith('po') or str(k).endswith('będę'):
                            exp = [k, '- JA aspekt nie dokonany czas przyszły TY -', meNow]
                    if str(k).endswith('bym'):
                        meNow = position.positionVerb(k)
                        exp = [k, '- JA tryb przypuszczający', meNow]
                if str(k).endswith('my'):
                    exp = [k, '- MY']
                if str(k).endswith('ysz') or str(k).endswith('esz') or str(k).endswith('isz') or str(k).endswith('asz')\
                or str(k).endswith('ób') or str(k).endswith('eś') or str(k).endswith('aj') or str(k).endswith('adź')\
                or str(k).endswith('ądź') or str(k).endswith('edz') or str(k).endswith('eź') or str(k).endswith('mij')\
                or str(k).endswith('ów') or str(k).endswith('aż') or str(k).endswith('byś') or str(k).endswith('uj')\
                or str(k).endswith('iń') or str(k).endswith('ań') or str(k).endswith('um') or str(k).endswith('szcz')\
                or str(k).endswith('lcz') or str(k).endswith('weź') or str(k).endswith('ieź') or str(k).endswith('ieś')\
                or str(k).endswith('el') or str(k).endswith('ap') or str(k).endswith('aś') or str(k).endswith('ucz')\
                or str(k).endswith('erz') or str(k).endswith('om') or str(k).endswith('yśl') or str(k).endswith('nów')\
                or str(k).endswith('nij') or str(k).endswith('ńcz') or str(k).endswith('ącz'):
                    meNow = position.positionVerb(k)
                    exp = [k, '- TY JA -', meNow]
                    if str(k).endswith('aj') or str(k).endswith('adź') or str(k).endswith('ądź') or str(k).endswith('edz')\
                    or str(k).endswith('eź') or str(k).endswith('mij') or str(k).endswith('ów') or str(k).endswith('aż')\
                    or str(k).endswith('ób') or str(k).endswith('uj') or str(k).endswith('iń') or str(k).endswith('ań')\
                    or str(k).endswith('um') or str(k).endswith('szcz') or str(k).endswith('lcz') or str(k).endswith('weź')\
                    or str(k).endswith('ieź') or str(k).endswith('ieś') or str(k).endswith('el') or str(k).endswith('om')\
                    or str(k).endswith('ap') or str(k).endswith('ucz') or str(k).endswith('erz') or str(k).endswith('yśl')\
                    or str(k).endswith('nów') or str(k).endswith('aj') or str(k).endswith('nij') or str(k).endswith('ńcz')\
                    or str(k).endswith('ącz'):
                        meNow = position.positionVerbInfinitive(k)
                        exp = [k, '- TY tryb rozkazujacy', meNow]
                    if str(k).endswith('byś'):
                        exp = [k, '- TY tryb przypuszczający', meNow]

                if str(k).endswith('cie'):
                    exp = [k, '- WY']
                if str(k).endswith('a') or str(k).endswith('si') or str(k).endswith('ał') or str(k).endswith('ił')\
                or str(k).endswith('ło') or str(k).endswith('iła') or str(k).endswith('ła') or str(k).endswith('je')\
                or str(k).endswith('rze') or str(k).endswith('oi') or str(k).endswith('gł') or str(k).endswith('oł')\
                or str(k).endswith('rzy') or str(k).endswith('sł') or str(k).endswith('wi'):
                    exp = [k, '- on/ona/ono']
                    if str(k).endswith('ał') or str(k).endswith('ił') or str(k).endswith('gł') or str(k).endswith('rzy')\
                    or str(k).endswith('sł'):
                        exp = [k, '- on']
                        if str(k).endswith('gł') or str(k).endswith('oł') or str(k).endswith('sł'):
                            exp = [k, '- on aspekt dokonany']
                        if str(k).endswith('rzy'):
                            exp = [k, '- on aspekt nie dokonany']
                    if str(k).endswith('iła') or str(k).endswith('ała'):
                        exp = [k, '- ona']
                    elif str(k).endswith('ła'):
                        exp = [k, '- ona aspekt dokonany']
                    if str(k).endswith('ło') or str(k).endswith('wi'):
                        exp = [k, '- ono']
                    if str(k).endswith('je') or str(k).endswith('rze') or str(k).endswith('oi'):
                        exp = [k, '- on/ona/ono aspekt nie dokonany']
                        if str(k).endswith('uje'):
                            exp = [k, '- on aspekt nie dokonany - strona czynna ']
                if str(k).endswith('ją') or str(k).endswith('li') or str(k).endswith('ały') or str(k).endswith('yły')\
                or str(k).endswith('yli') or str(k).endswith('ali') or str(k).endswith('dzą') or str(k).endswith('są'):
                    exp = [k, '- oni/one']
                    if str(k).endswith('ją') or str(k).endswith('są'):
                        exp = [k, '- oni/one strona zwtorna']
            if str(k).endswith('ać') or  str(k).endswith('dzi') or str(k).endswith('na') or str(k).endswith('iły')\
            or str(k).endswith('ne') or str(k).endswith('ieć') or str(k).endswith('est') or str(k).endswith('yć')\
            or str(k).endswith('ić') or str(k).endswith('ąc') or str(k).endswith('by'):
                if str(k).endswith('ać') or  str(k).endswith('dzi') or str(k).endswith('na') or str(k).endswith('ieć')\
                or str(k).endswith('est') or str(k).endswith('yć') or str(k).endswith('ić') or str(k).endswith('iły')\
                or str(k).endswith('ąc') or str(k).endswith('ne'):
                    exp = [k, '- tryb orzekający']
                if str(k).endswith('by'):
                    exp = [k, '- tryb przypuszczający']
            export.append(exp)
    return export

def changeProjests(OR_U = '', PO_U = '', OK_U = ''):
    B_A = whatWhoVerb(OR_U)
    B_PARSE_VERB_OR = OR_U
    B_PARSE_VERB_PO = PO_U
    B_PARSE_VERB_OK = OK_U
    print(B_A)
    for a in B_A:
        try: a[1]
        except: continue
        if str(a[1]).startswith('- TY'):
            try:a[2]
            except:continue
            A = a[0]
            B = a[2]
            # print('tutaj', A, B)
            B_PARSE_VERB_OR = B_PARSE_VERB_OR.replace(A, B)
            B_PARSE_VERB_OK = B_PARSE_VERB_OK.replace(A, B)
             
        elif str(a[1]).startswith('- JA'):
            try:a[2]
            except:continue
            E = a[0]
            F = a[2]
            B_PARSE_VERB_OR = B_PARSE_VERB_OR.replace(E, F)
            B_PARSE_VERB_OK = B_PARSE_VERB_OK.replace(E, F)
    
    B_B = whatWhoNounDenominator(PO_U)
    print(B_B)
    for b in B_B:
        try: b[1]
        except: continue
        B_PARSER_COUNTER = B_PARSE_VERB_OK.count(b[2]+' ') + B_PARSE_VERB_OK.count(b[0]+' ')
        if B_PARSER_COUNTER:
            C = b[0]+' '
            D = b[2]+' '
        else:
            C = b[0]
            D = b[2]
        if str(b[1]).startswith('- zaimek'):
            B_PARSE_VERB_PO = B_PARSE_VERB_PO.replace(C, D)
            B_PARSE_VERB_OK = B_PARSE_VERB_OK.replace(C, D)
    print(B_PARSE_VERB_OK)
    return B_PARSE_VERB_OR, B_PARSE_VERB_PO, B_PARSE_VERB_OK

def whatWhoNounDenominator(word):
    import coffeeBrain as cf
    import positionSimulation as position
    meaningBase = cf.coffeePls(False)[3]
    word = str(word)
    listWord = word.split(' ')
    export = []
    for oneword in listWord:
        try:
            meaningBase[oneword]
            wordIS = True
        except: wordIS = False
        exp = []
        if wordIS and meaningBase[oneword].count('zaimek') > 0:
            meNow = position.positionPronoun(oneword)
            exp = [oneword, '- zaimek', meNow]
        export.append(exp)
        if wordIS and meaningBase[oneword].count('mianownik') > 0:
            if oneword.endswith('ni') or oneword.endswith('za') or oneword.endswith('ść') or oneword.endswith('ać') or oneword.endswith('fa')\
            or oneword.endswith('ua') or oneword.endswith('sa') or oneword.endswith('da') or oneword.endswith('ti') or oneword.endswith('ra')\
            or oneword.endswith('ma') or oneword.endswith('ia') or oneword.endswith('ha') or oneword.endswith('dź') or oneword.endswith('wa')\
            or oneword.endswith('eś') or oneword.endswith('ęź') or oneword.endswith('ca') or oneword.endswith('la') or oneword.endswith('ew')\
            or oneword.endswith('uś') or oneword.endswith('ól') or oneword.endswith('bī') or oneword.endswith('ęć') or oneword.endswith('ja')\
            or oneword.endswith('oś') or oneword.endswith('ła') or oneword.endswith('śń') or oneword.endswith('ża') or oneword.endswith('śl')\
            or oneword.endswith('ka') or oneword.endswith('ba') or oneword.endswith('rć') or oneword.endswith('ga') or oneword.endswith('ta')\
            or oneword.endswith('va') or oneword.endswith('ęś') or oneword.endswith('ić') or oneword.endswith('na') or oneword.endswith('ań')\
            or oneword.endswith('oć') or oneword.endswith('pa') or oneword.endswith('źń'):
                if oneword !='słowa':
                    exp = [oneword, '- TA rodzaj żeński LP', 'mianownik']

            if oneword.endswith('ro') or oneword.endswith('pu') or oneword.endswith('mo') or oneword.endswith('um')\
            or oneword.endswith('po') or oneword.endswith('ńce') or oneword.endswith('ęk') or oneword.endswith('jo')\
            or oneword.endswith('to') or oneword.endswith('ło') or oneword.endswith('do') or oneword.endswith('ho') \
            or oneword.endswith('wo') or oneword.endswith('ko') or oneword.endswith('no') or oneword.endswith('bo') \
            or oneword.endswith('ku') or oneword.endswith('lo') or oneword.endswith('ię'):
                exp = [oneword, '- TO rodzaj nijaki LP', 'mianownik']

            if oneword.endswith('or') or oneword.endswith('eta') or oneword.endswith('pi') or oneword.endswith('iż')\
            or oneword.endswith('ak') or oneword.endswith('uj') or oneword.endswith('ąź') or oneword.endswith('ad') \
            or oneword.endswith('ąż') or oneword.endswith('go') or oneword.endswith('eż') or oneword.endswith('ał')\
            or oneword.endswith('ir') or oneword.endswith('ąb') or oneword.endswith('yś') or oneword.endswith('eń')\
            or oneword.endswith('sz'):
                exp = [oneword, '- TEN rodzaj męski żywotny LP', 'mianownik']

            if oneword.endswith('is') or oneword.endswith('er') or oneword.endswith('om')\
            or oneword.endswith('it') or oneword.endswith('uk') or oneword.endswith('yk')\
            or oneword.endswith('ld') or oneword.endswith('ód') or oneword.endswith('ns')\
            or oneword.endswith('ng') or oneword.endswith('nd') or oneword.endswith('ic')\
            or oneword.endswith('yb') or oneword.endswith('an') or oneword.endswith('em')\
            or oneword.endswith('aż') or oneword.endswith('eb') or oneword.endswith('ył')\
            or oneword.endswith('rf') or oneword.endswith('yc') or oneword.endswith('rk')\
            or oneword.endswith('yż') or oneword.endswith('ut') or oneword.endswith('rt')\
            or oneword.endswith('rz') or oneword.endswith('mb') or oneword.endswith('ąt')\
            or oneword.endswith('oc') or oneword.endswith('sk') or oneword.endswith('ob')\
            or oneword.endswith('ug') or oneword.endswith('st') or oneword.endswith('ap')\
            or oneword.endswith('uł') or oneword.endswith('ym') or oneword.endswith('os')\
            or oneword.endswith('rd') or oneword.endswith('ur') or oneword.endswith('op')\
            or oneword.endswith('un') or oneword.endswith('us') or oneword.endswith('ks')\
            or oneword.endswith('uć') or oneword.endswith('ik') or oneword.endswith('yp')\
            or oneword.endswith('fr') or oneword.endswith('ór') or oneword.endswith('pt')\
            or oneword.endswith('ex') or oneword.endswith('ąg') or oneword.endswith('ps')\
            or oneword.endswith('oń') or oneword.endswith('id') or oneword.endswith('ot')\
            or oneword.endswith('kl') or oneword.endswith('lt') or oneword.endswith('og')\
            or oneword.endswith('ąz') or oneword.endswith('ił') or oneword.endswith('ój')\
            or oneword.endswith('ch') or oneword.endswith('ed') or oneword.endswith('eg')\
            or oneword.endswith('mp') or oneword.endswith('or') or oneword.endswith('il')\
            or oneword.endswith('ób') or oneword.endswith('zd') or oneword.endswith('wr')\
            or oneword.endswith('yw') or oneword.endswith('et') or oneword.endswith('as')\
            or oneword.endswith('rp') or oneword.endswith('im') or oneword.endswith('ep')\
            or oneword.endswith('am') or oneword.endswith('ac') or oneword.endswith('oj')\
            or oneword.endswith('at') or oneword.endswith('aj') or oneword.endswith('ip')\
            or oneword.endswith('ul') or oneword.endswith('mn') or oneword.endswith('ij')\
            or oneword.endswith('ąs') or oneword.endswith('bs') or oneword.endswith('gy')\
            or oneword.endswith('óz') or oneword.endswith('yt') or oneword.endswith('oł')\
            or oneword.endswith('nr') or oneword.endswith('ig') or oneword.endswith('uz')\
            or oneword.endswith('el') or oneword.endswith('ek') or oneword.endswith('ęg')\
            or oneword.endswith('cz') or oneword.endswith('af') or oneword.endswith('ok')\
            or oneword.endswith('iś') or oneword.endswith('óg') or oneword.endswith('al')\
            or oneword.endswith('yl') or oneword.endswith('ol') or oneword.endswith('ej')\
            or oneword.endswith('en') or oneword.endswith('ec') or oneword.endswith('ub')\
            or oneword.endswith('nu') or oneword.endswith('ów') or oneword.endswith('ót')\
            or oneword.endswith('in') or oneword.endswith('ęt') or oneword.endswith('ab')\
            or oneword.endswith('ar') or oneword.endswith('br') or oneword.endswith('ęp')\
            or oneword.endswith('łd') or oneword.endswith('tr') or oneword.endswith('óż')\
            or oneword.endswith('ef') or oneword.endswith('az') or oneword.endswith('ół')\
            or oneword.endswith('łt') or oneword.endswith('up') or oneword.endswith('nk')\
            or oneword.endswith('aw') or oneword.endswith('ęd') or oneword.endswith('od')\
            or oneword.endswith('dz') or oneword.endswith('ąd') or oneword.endswith('ud')\
            or oneword.endswith('eł') or oneword.endswith('ys') or oneword.endswith('yn')\
            or oneword.endswith('eć') or oneword.endswith('iw') or oneword.endswith('rb')\
            or oneword.endswith('ąk') or oneword.endswith('on') or oneword.endswith('io')\
            or oneword.endswith('sł') or oneword.endswith('ąc') or oneword.endswith('nt')\
            or oneword.endswith('es') or oneword.endswith('rg'):

                exp = [oneword, '- TEN rodzaj męski nieżywotny LP', 'mianownik']

            if oneword.endswith('owie') or oneword.endswith('rzy')\
            or oneword.endswith('ele') or oneword.endswith('enci')\
            or oneword.endswith('eci') or oneword.endswith('yce')\
            or oneword.endswith('ci') or oneword.endswith('zi')\
            or oneword.endswith('si') or oneword.endswith('fi')\
            or oneword.endswith('wi'):
                exp = [oneword, '- CI rodzaj męskoosobowy LM', 'mianownik']

            if  oneword.endswith('nie') or oneword.endswith('oce') or oneword.endswith('ości') or oneword.endswith('na')\
            or oneword.endswith('na') or oneword.endswith('dy') or oneword.endswith('ry') or oneword.endswith('ty')\
            or oneword.endswith('ny') or oneword.endswith('ri') or oneword.endswith('ki') or oneword.endswith('gi')\
            or oneword.endswith('sy') or oneword.endswith('je') or oneword.endswith('ły') or oneword.endswith('re')\
            or oneword.endswith('ós') or oneword.endswith('se') or oneword.endswith('zy') or oneword.endswith('de')\
            or oneword.endswith('le') or oneword.endswith('te') or oneword.endswith('fy') or oneword.endswith('łe')\
            or oneword.endswith('py') or oneword.endswith('lę') or oneword.endswith('be') or oneword.endswith('me')\
            or oneword.endswith('wy') or oneword.endswith('ky') or oneword.endswith('my') or oneword.endswith('mi')\
            or oneword.endswith('ze') or oneword.endswith('że') or oneword.endswith('ne') or oneword.endswith('hy')\
            or oneword.endswith('żę')\
            or oneword == 'słowa':
                exp = [oneword, '- TE rodzaj niemeskoosobowy LM', 'mianownik']
            export.append(exp)

        if wordIS and meaningBase[oneword].count('dopełniacz') > 0:
            if oneword.endswith('ej') or oneword.endswith('ku') or oneword.endswith('sy') or oneword.endswith('ży')\
            or oneword.endswith('ły') or oneword.endswith('fy') or oneword.endswith('wy') or oneword.endswith('ii')\
            or oneword.endswith('ni') or oneword.endswith('ci') or oneword.endswith('ui') or oneword.endswith('yi')\
            or oneword.endswith('ry') or oneword.endswith('gi') or oneword.endswith('wi') or oneword.endswith('dy')\
            or oneword.endswith('ly') or oneword.endswith('cy') or oneword.endswith('hy') or oneword.endswith('py')\
            or oneword.endswith('by') or oneword.endswith('ki') or oneword.endswith('ti') or oneword.endswith('zy')\
            or oneword.endswith('ty') or oneword.endswith('my') or oneword.endswith('ny') or oneword.endswith('zi')\
            or oneword.endswith('si') or oneword.endswith('ji'):
                if not oneword.endswith('rzy') or not oneword.endswith('czy') or not oneword.endswith('szy')\
                    or not oneword.endswith('dzi') or not oneword.endswith('ęzi'):
                    exp = [oneword, '-  TEJ rodzaj żeński LP', 'dopełniacz']
                if oneword == 'kliszy' or oneword == 'więzi':
                    exp = [oneword, '-  TEJ rodzaj żeński LP', 'dopełniacz']
            export.append(exp)

            if oneword.endswith('hi') or oneword.endswith('ju') or oneword.endswith('ku') or oneword.endswith('zu')\
            or oneword.endswith('lu') or oneword.endswith('ka') or oneword.endswith('wa') or oneword.endswith('mu')\
            or oneword.endswith('ja') or oneword.endswith('pa') or oneword.endswith('du') or oneword.endswith('ła')\
            or oneword.endswith('gu') or oneword.endswith('ga') or oneword.endswith('iu') or oneword.endswith('fa')\
            or oneword.endswith('da') or oneword.endswith('bu') or oneword.endswith('za') or oneword.endswith('łu')\
            or oneword.endswith('ce') or oneword.endswith('nu') or oneword.endswith('ha') or oneword.endswith('na')\
            or oneword.endswith('sa') or oneword.endswith('ba') or oneword.endswith('ea') or oneword.endswith('ta')\
            or oneword.endswith('la') or oneword.endswith('ru') or oneword.endswith('hu') or oneword.endswith('cu')\
            or oneword.endswith('fu') or oneword.endswith('pu') or oneword.endswith('ża') or oneword.endswith('tu')\
            or oneword.endswith('ia') or oneword.endswith('ma') or oneword.endswith('mo') or oneword.endswith('ca')\
            or oneword.endswith('ra') or oneword.endswith('go') or oneword.endswith('su'):
                exp = [oneword, '- TEGO rodzaj męski LP', 'dopełniacz']

            if oneword.endswith('ór') or oneword.endswith('sp') or oneword.endswith('eb') or oneword.endswith('ob') or oneword.endswith('ib')\
            or oneword.endswith('yw') or oneword.endswith('id') or oneword.endswith('ób') or oneword.endswith('nd') or oneword.endswith('ir')\
            or oneword.endswith('óż') or oneword.endswith('af') or oneword.endswith('ef') or oneword.endswith('ek') or oneword.endswith('mb')\
            or oneword.endswith('ud') or oneword.endswith('ub') or oneword.endswith('żu') or oneword.endswith('at') or oneword.endswith('eń')\
            or oneword.endswith('ąg') or oneword.endswith('ep') or oneword.endswith('ld') or oneword.endswith('ag') or oneword.endswith('ur')\
            or oneword.endswith('śb') or oneword.endswith('iz') or oneword.endswith('ar') or oneword.endswith('rż') or oneword.endswith('zn')\
            or oneword.endswith('fr') or oneword.endswith('as') or oneword.endswith('sk') or oneword.endswith('im') or oneword.endswith('mn')\
            or oneword.endswith('or') or oneword.endswith('ąb') or oneword.endswith('nt') or oneword.endswith('uł') or oneword.endswith('zw')\
            or oneword.endswith('ad') or oneword.endswith('dź') or oneword.endswith('yk') or oneword.endswith('of') or oneword.endswith('tr')\
            or oneword.endswith('zt') or oneword.endswith('un') or oneword.endswith('yg') or oneword.endswith('mi') or oneword.endswith('cz')\
            or oneword.endswith('ik') or oneword.endswith('ez') or oneword.endswith('oń') or oneword.endswith('li') or oneword.endswith('yt')\
            or oneword.endswith('sł') or oneword.endswith('kt') or oneword.endswith('oi') or oneword.endswith('io') or oneword.endswith('ai')\
            or oneword.endswith('ał') or oneword.endswith('ót') or oneword.endswith('ac') or oneword.endswith('oz') or oneword.endswith('ul')\
            or oneword.endswith('óg') or oneword.endswith('iw') or oneword.endswith('op') or oneword.endswith('ył') or oneword.endswith('wd')\
            or oneword.endswith('ść') or oneword.endswith('um') or oneword.endswith('rn') or oneword.endswith('nw') or oneword.endswith('og')\
            or oneword.endswith('os') or oneword.endswith('ip') or oneword.endswith('ów') or oneword.endswith('on') or oneword.endswith('ec')\
            or oneword.endswith('ił') or oneword.endswith('ól') or oneword.endswith('óz') or oneword.endswith('ug') or oneword.endswith('es')\
            or oneword.endswith('sm') or oneword.endswith('uń') or oneword.endswith('mp') or oneword.endswith('uf') or oneword.endswith('wu')\
            or oneword.endswith('jd') or oneword.endswith('it') or oneword.endswith('uh') or oneword.endswith('yć') or oneword.endswith('et')\
            or oneword.endswith('ań') or oneword.endswith('az') or oneword.endswith('ąż') or oneword.endswith('ak') or oneword.endswith('ńc')\
            or oneword.endswith('rw') or oneword.endswith('ps') or oneword.endswith('am') or oneword.endswith('yp') or oneword.endswith('er')\
            or oneword.endswith('rg') or oneword.endswith('tn') or oneword.endswith('rs') or oneword.endswith('st') or oneword.endswith('uż')\
            or oneword.endswith('eł') or oneword.endswith('em') or oneword.endswith('rz') or oneword.endswith('ąk') or oneword.endswith('nz')\
            or oneword.endswith('nc') or oneword.endswith('yń') or oneword.endswith('uz') or oneword.endswith('ym') or oneword.endswith('sz')\
            or oneword.endswith('iń') or oneword.endswith('eg') or oneword.endswith('ch') or oneword.endswith('lk') or oneword.endswith('dm')\
            or oneword.endswith('yz') or oneword.endswith('iź') or oneword.endswith('ić') or oneword.endswith('ut') or oneword.endswith('aw')\
            or oneword.endswith('yn') or oneword.endswith('ol') or oneword.endswith('rt') or oneword.endswith('sc') or oneword.endswith('lm')\
            or oneword.endswith('ig') or oneword.endswith('uś') or oneword.endswith('zd') or oneword.endswith('rzy') or oneword.endswith('czy')\
            or oneword.endswith('szy') or oneword.endswith('an') or oneword.endswith('uk') or oneword.endswith('ic') or oneword.endswith('in')\
            or oneword.endswith('lf') or oneword.endswith('jz') or oneword.endswith('en') or oneword.endswith('ęć') or oneword.endswith('yr')\
            or oneword.endswith('ęg') or oneword.endswith('rb') or oneword.endswith('ei') or oneword.endswith('el') or oneword.endswith('up')\
            or oneword.endswith('ns') or oneword.endswith('al') or oneword.endswith('dz') or oneword.endswith('dzi') or oneword.endswith('ęzi')\
            or oneword.endswith('ot') or oneword.endswith('uć') or oneword.endswith('tw') or oneword.endswith('yc') or oneword.endswith('oź')\
            or oneword.endswith('ed') or oneword.endswith('yj') or oneword.endswith('rd') or oneword.endswith('od') or oneword.endswith('yb')\
            or oneword.endswith('ab') or oneword.endswith('żb') or oneword.endswith('ng') or oneword.endswith('żm') or oneword.endswith('ji')\
            or oneword.endswith('ół') or oneword.endswith('óp') or oneword.endswith('rm') or oneword.endswith('ok') or oneword.endswith('br')\
            or oneword.endswith('om') or oneword.endswith('dr') or oneword.endswith('źb') or oneword.endswith('ąt') or oneword.endswith('rć')\
            or oneword.endswith('rc') or oneword.endswith('ew') or oneword.endswith('śm') or oneword.endswith('ap') or oneword.endswith('pi')\
            or oneword.endswith('aj') or oneword.endswith('is') or oneword.endswith('zb') or oneword.endswith('ad'):
                if oneword != 'kliszy' or oneword != 'więzi':
                    exp = [oneword, '- TYCH rodzaj niemeskoosobowy LM', 'dopełniacz']
            export.append(exp)
        if wordIS and meaningBase[oneword].count('celownik') > 0: # komu? czemu?
            if oneword.endswith('gu') or oneword.endswith('cu') or oneword.endswith('ba') or oneword.endswith('um') or oneword.endswith('su')\
            or oneword.endswith('hu') or oneword.endswith('do') or oneword.endswith('te') or oneword.endswith('wi') or oneword.endswith('by')\
            or oneword.endswith('du') or oneword.endswith('iście') or oneword.endswith('yście') or oneword.endswith('iocie')\
            or oneword.endswith('micie') or oneword.endswith('iu') or oneword.endswith('tu') or oneword.endswith('żu') or oneword.endswith('ru')\
            or oneword.endswith('wu') or oneword.endswith('eu') or oneword.endswith('ke') or oneword.endswith('mu') or oneword.endswith('pu')\
            or oneword.endswith('nu') or oneword.endswith('la') or oneword.endswith('lu') or oneword.endswith('zu') or oneword.endswith('ku')\
            or oneword.endswith('to') or oneword.endswith('łu') or oneword.endswith('de') or oneword.endswith('ju') or oneword.endswith('bu'):
                exp = [oneword, '- TEMU rodzaj męski LP', 'celownik']

            if oneword.endswith('mi') or oneword.endswith('dy') or oneword.endswith('ri') or oneword.endswith('es') or oneword.endswith('pi')\
            or oneword.endswith('ti') or oneword.endswith('ej') or oneword.endswith('li') or oneword.endswith('le') or oneword.endswith('ci')\
            or oneword.endswith('hi') or oneword.endswith('fu') or oneword.endswith('ze') or oneword.endswith('ie') or oneword.endswith('zi')\
            or oneword.endswith('ii') or oneword.endswith('ży') or oneword.endswith('ui') or oneword.endswith('rg') or oneword.endswith('ce')\
            or oneword.endswith('oi') or oneword.endswith('ne') or oneword.endswith('si') or oneword.endswith('cy') or oneword.endswith('ji')\
            or oneword.endswith('zy'):
                if not oneword.endswith('iście') or not oneword.endswith('yście') or not oneword.endswith('iocie') or not oneword.endswith('micie'):
                 exp = [oneword, '- TEJ rodzaj żeński LP', 'celownik']

            if oneword.endswith('óm') or oneword.endswith('ni') or oneword.endswith('ms') or oneword.endswith('im') or oneword.endswith('om')\
            or oneword.endswith('ym'):
                exp = [oneword, '- TYM rodzaj nijaki LM', 'celownik']
            export.append(exp)


        if wordIS and meaningBase[oneword].count('biernik') > 0: # Kogo? co? widzę
            if oneword.endswith('hu') or oneword.endswith('la') or oneword.endswith('io') or oneword.endswith('ku') or oneword.endswith('ża')\
            or oneword.endswith('ra') or oneword.endswith('jo') or oneword.endswith('ca') or oneword.endswith('ba') or oneword.endswith('go')\
            or oneword.endswith('ga') or oneword.endswith('ła') or oneword.endswith('ti') or oneword.endswith('hi') or oneword.endswith('sa')\
            or oneword.endswith('ha') or oneword.endswith('za') or oneword.endswith('ja') or oneword.endswith('na') or oneword.endswith('da')\
            or oneword.endswith('ma') or oneword.endswith('ta') or oneword.endswith('lu') or oneword.endswith('fu')\
                or oneword == 'męnżczyznę':
                exp = [oneword, '- TEGO rodzaj męski żywotny LP', 'biernik']

            if oneword.endswith('ból') or oneword.endswith('er') or oneword.endswith('óg') or oneword.endswith('cz') or oneword.endswith('nk')\
            or oneword.endswith('ir') or oneword.endswith('eb') or oneword.endswith('st') or oneword.endswith('jf') or oneword.endswith('dz')\
            or oneword.endswith('ór') or oneword.endswith('uch') or oneword.endswith('ach') or oneword.endswith('ech') or oneword.endswith('zch')\
            or oneword.endswith('ęk') or oneword.endswith('pt') or oneword.endswith('am') or oneword.endswith('or') or oneword.endswith('ąc')\
            or oneword.endswith('il') or oneword.endswith('yw') or oneword.endswith('uk') or oneword.endswith('ug') or oneword.endswith('ys')\
            or oneword.endswith('at') or oneword.endswith('aż') or oneword.endswith('zd') or oneword.endswith('ił') or oneword.endswith('et')\
            or oneword.endswith('ng') or oneword.endswith('ób') or oneword.endswith('yl') or oneword.endswith('yn') or oneword.endswith('it')\
            or oneword.endswith('sk') or oneword.endswith('in') or oneword.endswith('kloc') or oneword.endswith('owoc') or oneword.endswith('as')\
            or oneword.endswith('yż') or oneword.endswith('jm') or oneword.endswith('łd') or oneword.endswith('łt') or oneword.endswith('ub')\
            or oneword.endswith('ok') or oneword.endswith('lo') or oneword.endswith('es') or oneword.endswith('ar') or oneword.endswith('zt')\
            or oneword.endswith('id') or oneword.endswith('ęg') or oneword.endswith('yk') or oneword.endswith('ns') or oneword.endswith('on')\
            or oneword.endswith('ed') or oneword.endswith('ud') or oneword.endswith('ek') or oneword.endswith('ik') or oneword.endswith('nt')\
            or oneword.endswith('ół') or oneword.endswith('sł') or oneword.endswith('rb') or oneword.endswith('az') or oneword.endswith('ip')\
            or oneword.endswith('op') or oneword.endswith('ąd') or oneword.endswith('ap') or oneword.endswith('iw') or oneword.endswith('rk')\
            or oneword.endswith('yp') or oneword.endswith('ęt') or oneword.endswith('aj') or oneword.endswith('zg') or oneword.endswith('fr')\
            or oneword.endswith('up') or oneword.endswith('ót') or oneword.endswith('ur') or oneword.endswith('kl') or oneword.endswith('rd')\
            or oneword.endswith('yt') or oneword.endswith('cy') or oneword.endswith('ol') or oneword.endswith('ot') or oneword.endswith('rz')\
            or oneword.endswith('ob') or oneword.endswith('im') or oneword.endswith('uz') or oneword.endswith('oł') or oneword.endswith('ef')\
            or oneword.endswith('un') or oneword.endswith('ód') or oneword.endswith('us') or oneword.endswith('ak') or oneword.endswith('nd')\
            or oneword.endswith('eg') or oneword.endswith('óz') or oneword.endswith('uł') or oneword.endswith('ąb') or oneword.endswith('el')\
            or oneword.endswith('ęd') or oneword.endswith('rs') or oneword.endswith('en') or oneword.endswith('ps') or oneword.endswith('ew')\
            or oneword.endswith('eł') or oneword.endswith('ąs') or oneword.endswith('ój') or oneword.endswith('ac') or oneword.endswith('zm')\
            or oneword.endswith('kt') or oneword.endswith('ep') or oneword.endswith('is') or oneword.endswith('ym') or oneword.endswith('ad')\
            or oneword.endswith('ał') or oneword.endswith('ęp') or oneword.endswith('iż') or oneword.endswith('yb') or oneword.endswith('ig')\
            or oneword.endswith('ij') or oneword.endswith('aw') or oneword.endswith('rf') or oneword.endswith('ec') or oneword.endswith('ąg')\
            or oneword.endswith('rm') or oneword.endswith('ąt') or oneword.endswith('sz') or oneword.endswith('ył') or oneword.endswith('os')\
            or oneword.endswith('mb') or oneword.endswith('ul') or oneword.endswith('óż') or oneword.endswith('ab') or oneword.endswith('rt')\
            or oneword.endswith('lt') or oneword.endswith('pa') or oneword.endswith('fa') or oneword.endswith('ut') or oneword.endswith('mn')\
            or oneword.endswith('em') or oneword.endswith('ks') or oneword.endswith('ic') or oneword.endswith('od') or oneword.endswith('jt')\
            or oneword.endswith('ow') or oneword.endswith('wr') or oneword.endswith('ąz') or oneword.endswith('al') or oneword.endswith('om')\
            or oneword.endswith('rp') or oneword.endswith('og') or oneword.endswith('tr') or oneword.endswith('lm') or oneword.endswith('eń')\
            or oneword.endswith('nr') or oneword.endswith('ej'):
                if oneword != 'cech' or oneword != 'straż' or oneword != 'klas':
                    exp = [oneword, '- TEN rodzaj męski nieżywotny LP', 'biernik']

            if oneword.endswith('sól') or oneword.endswith('an') or oneword.endswith('mp') or oneword.endswith('zą') or oneword.endswith('af')\
            or oneword.endswith('yc') or oneword.endswith('tę') or oneword.endswith('oń') or oneword.endswith('kę') or oneword.endswith('rg')\
            or oneword.endswith('oć') or oneword.endswith('straż') or oneword.endswith('do') or oneword.endswith('ję') or oneword.endswith('rć')\
            or oneword.endswith('mą') or oneword.endswith('ić') or oneword.endswith('oc') or oneword.endswith('eż') or oneword.endswith('dę')\
            or oneword.endswith('ho') or oneword.endswith('ęź') or oneword.endswith('ną') or oneword.endswith('wę') or oneword.endswith('śl')\
            or oneword.endswith('łą') or oneword.endswith('mi') or oneword.endswith('wą') or oneword.endswith('hę') or oneword.endswith('dź')\
            or oneword.endswith('uś') or oneword.endswith('rę') or oneword.endswith('gę') or oneword.endswith('mę') or oneword.endswith('lę')\
            or oneword.endswith('ać') or oneword.endswith('śń') or oneword.endswith('bą') or oneword.endswith('um') or oneword.endswith('eś')\
            or oneword.endswith('ść') or oneword.endswith('oś') or oneword.endswith('dą') or oneword.endswith('uć') or oneword.endswith('eć')\
            or oneword.endswith('łę') or oneword.endswith('eę') or oneword.endswith('zę') or oneword.endswith('fę') or oneword.endswith('ąź')\
            or oneword.endswith('ię') or oneword.endswith('tą') or oneword.endswith('ią') or oneword.endswith('pę') or oneword.endswith('po')\
            or oneword.endswith('no') or oneword.endswith('ko') or oneword.endswith('ań') or oneword.endswith('ęś') or oneword.endswith('cę')\
            or oneword.endswith('wo') or oneword.endswith('sę') or oneword.endswith('cą') or oneword.endswith('ęć') or oneword.endswith('żę')\
            or oneword.endswith('źń') or oneword.endswith('ką') or oneword.endswith('nę') or oneword.endswith('rą') or oneword.endswith('ło')\
            or oneword.endswith('iu'):
                if oneword != 'kloc' or oneword != 'owoc' or oneword != 'mężczyznę':
                    exp = [oneword, '- TĘ rodzaj żeński LP', 'biernik']

            if oneword.endswith('pól') or oneword.endswith('nu') or oneword.endswith('ch') or oneword.endswith('cech') or oneword.endswith('zaduch')\
            or oneword.endswith('ych') or oneword.endswith('zi') or oneword.endswith('oj') or oneword.endswith('ów') or oneword.endswith('klas')\
            or oneword.endswith('ii') or oneword.endswith('ży') or oneword.endswith('li') or oneword.endswith('zn') or oneword.endswith('ni'):
                exp = [oneword, '- TYCH rodzaj męski LM', 'biernik']

            if oneword.endswith('óm') or oneword.endswith('bę') or oneword.endswith('ia') or oneword.endswith('ły') or oneword.endswith('te')\
            or oneword.endswith('re') or oneword.endswith('sy') or oneword.endswith('ua') or oneword.endswith('że') or oneword.endswith('pi')\
            or oneword.endswith('ne') or oneword.endswith('mo') or oneword.endswith('si') or oneword.endswith('be') or oneword.endswith('gy')\
            or oneword.endswith('hy') or oneword.endswith('we') or oneword.endswith('ny') or oneword.endswith('py') or oneword.endswith('ie')\
            or oneword.endswith('to') or oneword.endswith('je') or oneword.endswith('dy') or oneword.endswith('ry') or oneword.endswith('zy')\
            or oneword.endswith('me') or oneword.endswith('łe') or oneword.endswith('wi') or oneword.endswith('ty') or oneword.endswith('ki')\
            or oneword.endswith('bo') or oneword.endswith('ze') or oneword.endswith('ka') or oneword.endswith('de') or oneword.endswith('le')\
            or oneword.endswith('wy') or oneword.endswith('fy') or oneword.endswith('ro') or oneword.endswith('gi') or oneword.endswith('ea')\
            or oneword.endswith('ce') or oneword.endswith('my') or oneword.endswith('ly') or oneword.endswith('by') or oneword.endswith('ci')\
            or oneword.endswith('wa'):
                exp = [oneword, '- TE rodzaj męski nieosobowy/żeński/nijaki LM', 'biernik']
            export.append(exp)

        if wordIS and meaningBase[oneword].count('narzędnik') > 0: # - z kim? z czym? idę
            if oneword.endswith('do') or oneword.endswith('ks') or oneword.endswith('ek') or oneword.endswith('to') or oneword.endswith('pu')\
            or oneword.endswith('by') or oneword.endswith('ti') or oneword.endswith('ie') or oneword.endswith('ow') or oneword.endswith('um')\
            or oneword.endswith('tą') or oneword.endswith('em') or oneword.endswith('nu') or oneword.endswith('et') or oneword.endswith('ku')\
            or oneword.endswith('no') or oneword.endswith('go') or oneword.endswith('im') or oneword.endswith('ym') or oneword.endswith('mo')\
            or oneword.endswith('iu') or oneword.endswith('io') or oneword.endswith('męszczyzną'):
                exp = [oneword, '- TYM rodzaj męski LP', 'narzędnik']

            if oneword.endswith('ną') or oneword.endswith('pą') or oneword.endswith('dą') or oneword.endswith('mą') or oneword.endswith('er')\
            or oneword.endswith('łą') or oneword.endswith('hą') or oneword.endswith('gą') or oneword.endswith('rg') or oneword.endswith('żą')\
            or oneword.endswith('rą') or oneword.endswith('bą') or oneword.endswith('yk') or oneword.endswith('wą') or oneword.endswith('są')\
            or oneword.endswith('fą') or oneword.endswith('ik') or oneword.endswith('zą') or oneword.endswith('eą') or oneword.endswith('ją')\
            or oneword.endswith('ką') or oneword.endswith('cą') or oneword.endswith('ią') or oneword.endswith('lą') or oneword.endswith('li'):
                if oneword != 'męszczyzną':
                    exp = [oneword, '- TĄ rodzaj żeński LP', 'narzędnik']

            if oneword.endswith('si') or oneword.endswith('mi'):
                exp = [oneword, '- TYMI rodzaj męski nieosobowy/żeński/nijaki LM', 'narzędnik']
            export.append(exp)

        if wordIS and meaningBase[oneword].count('miejscownik') > 0: # o kim? o czym? myślę
            if oneword.endswith('ie') or oneword.endswith('ym') or oneword.endswith('mo') or oneword.endswith('hu') or oneword.endswith('go')\
            or oneword.endswith('ne') or oneword.endswith('le') or oneword.endswith('io') or oneword.endswith('lu') or oneword.endswith('bu')\
            or oneword.endswith('ze') or oneword.endswith('nu') or oneword.endswith('mu') or oneword.endswith('ju') or oneword.endswith('im')\
            or oneword.endswith('to') or oneword.endswith('gu') or oneword.endswith('ti') or oneword.endswith('pu') or oneword.endswith('ku')\
            or oneword.endswith('iu') or oneword.endswith('żu') or oneword.endswith('zu') or oneword.endswith('su') or oneword.endswith('ru')\
            or oneword.endswith('cy') or oneword.endswith('no') or oneword.endswith('ek') or oneword.endswith('by') or oneword.endswith('um')\
            or oneword.endswith('do') or oneword.endswith('cu') or oneword.endswith('wu'):
                expected_IE_ZE = [
                    'dziedzinie', 'głowie', 'odzie', 'formie', 'szufladzie', 'prawdzie', 'nazwie', 'mamie', 'zupie', 'osobie',
                    'komendzie', 'przygodzie', 'rybie', 'mowie', 'klasie', 'muzie', 'istocie', 'żonie', 'kopie', 'sylabie',
                    'heroinie', 'zasadzie', 'liczbie', 'metodzie', 'wenie', 'umowie', 'trawie', 'podstawie', 'pupie', 'kwocie',
                    'tapecie', 'nagrodzie', 'cenie', 'ocenie', 'dziwie', 'roślinie', 'grzie', 'karcie', 'linie', 'kokiecie',
                    'ścianie', 'obudowie', 'gamie', 'ekspertyzie', 'odmianie', 'rozprawie', 'ławie', 'posadzie', 'sprawie', 'syrenie',
                    'syntezie', 'damie', 'kasie', 'krainie', 'zgubie', 'przeszkodzie', 'budowie', 'stropie', 'przyczynie', 'wyspie',
                    'łacie', 'niepogodzie', 'słowacczyźnie', 'gumie', 'werwie', 'rozmowie', 'lokacie', 'ochronie', 'sławie', 'stercie',
                    'ojczyźnie', 'stronie', 'fecie', 'radzie', 'seksbombie', 'dumie', 'godzinie', 'dupie', 'reklamie', 'zabawie',
                    'wadzie', 'legendzie', 'chorobie', 'próbie', 'zawadzie', 'tezie', 'bieliźnie', 'mamonie', 'kozie', 'matuchnie',
                    'lampie', 'łepetynie', 'wacie', 'nudzie', 'szafie', 'etykiecie', 'normie', 'sobocie', 'mapie', 'zimie',
                    'płycie', 'stówie', 'izbie', 'wspólnocie', 'rycinie', 'wymianie', 'kobiecie', 'dobie', 'szramie', 'trasie',
                    'osadzie', 'trupie', 'maszynie', 'ikonie', 'minucie', 'planecie', 'postawie', 'gwieździe', 'puazie', 'modlitwie',
                    'powabie', 'tkaninie', 'sumie', 'wiośnie', 'pogodzie', 'rutenie', 'zmianie', 'zarazie', 'modzie', 'szefie',
                    'bramie', 'katastrofie', 'kończynie', 'firmie', 'poradzie', 'przedmowie', 'wodzie', 'środzie', 'łajzie', 'utracie',
                    'cipie', 'szacie', 'krzywdzie', 'sekundzie', 'dyscyplinie', 'żupie', 'dziewczynie', 'pyzie', 'jarzynie', 'ranie',
                    'grupie', 'szamotaninie', 'oponie', 'scenie', 'zjawie', 'gazecie', 'imprezie', 'połowie', 'sprężynie', 'potrzebie',
                    'królewnie', 'myślówie', 'choinie', 'śrubie', 'zgodzie', 'poczcie', 'lufie', 'domenie', 'babie', 'ofercie',
                    'plamie', 'fasadzie', 'ślepocie', 'szczebiocie', 'erudycie', 'przesadzie', 'kelwinie', 'pannie', 'nucie', 'szkodzie',
                    'warstwie', 'ptaszynie', 'nizinie', 'brylantynie', 'walucie', 'strawie', 'ślinie', 'służbie', 'fazie', 'rodzinie',
                    'analizie', 'farbie', 'blokadzie', 'czekoladzie', 'podobiźnie', 'kurwie', 'dziecinie', 'gębie', 'obronie', 'minie',
                    'dominie', 'runie', 'bessie', 'pzie', 'rudzie', 'łapie', 'gazie', 'jamie', 'pipie', 'apokalipsie',
                    'trąbie', 'mieliźnie', 'słomie', 'ramie', 'nawie', 'gadzinie', 'obawie', 'mannie', 'witrynie', 'secie',
                    'burdzie', 'grypie', 'kruszynie', 'łzie', 'drużynie', 'strefie', 'flocie', 'tamie', 'kawie', 'biedzie',
                    'wydzielinie', 'rzeźbie', 'ustawie', 'gonitwie', 'urodzie', 'kupie', 'rundzie', 'bonanzie', 'robocie', 'elicie',
                    'esie', 'ekipie', 'taśmie', 'barwie', 'pauzie', 'bazie', 'brzytwie', 'poświacie', 'perspektywie', 'podkowie', 'jagodzie',
                    'jucie', 'kalinie', 'malinie', 'marynie', 'marzannie', 'rucie',

                    'nodze', 'podporze', 'girze', 'awanturze', 'atmosferze', 'słudze', 'siostrze', 'gwarze', 'cyfrze', 'pociesze', 'cesze',
                    'literze', 'podłodze', 'parze', 'księdze', 'procedurze', 'laurze', 'pladze', 'strukturze', 'przysłudze', 'ofierze', 'wadze',
                    'drodze', 'architekturze', 'uwadze', 'otusze', 'fryzurze', 'lebiedze', 'cenzurze', 'literaturze', 'dziurze', 'porze', 'karze',
                    'agenturze', 'kresze', 'blokierze', 'blasze', 'wydrze', 'warze', 'barierze', 'mierze', 'górze', 'orkiestrze', 'figurze', 'czwórze',
                    'uciesze', 'fakturze', 'operze', 'zaporze', 'aparaturze', 'wierze', 'posłudze', 'potędze', 'ciemiędze', 'orderze', 'fidze',
                    'naturze', 'lekturze', 'grze', 'powadze', 'temperaturze', 'smudze', 'kłamczusze', 'fatydze', 'kulturze', 'erze', 'dysze', 'metaforze',
                    'randze', 'czasze', 'oficerze', 'omedze', 'przewadze', 'skórze', 'henrze', 'lidze', 'lize', 'aferze', 'lupanarze', 'iskrze', 'broszurze',
                    'kotarze', 'radosze', 'zebrze', 'czyściosze', 'wiosze', 'bzdurze', 'florze', 'kasandrze', 'kirze', 'lorze'
                ]
                ex_IE_ZE = False
                for IE in expected_IE_ZE:
                    if oneword == IE:
                        ex_IE_ZE = True
                if not ex_IE_ZE:
                    exp = [oneword, '- TYM rodzaj męski LP', 'miejscownik']
                else:
                    exp = [oneword, '- TEJ rodzaj męski LP', 'miejscownik']

            if oneword.endswith('ke') or oneword.endswith('ży') or oneword.endswith('hi') or oneword.endswith('er') or oneword.endswith('ik')\
            or oneword.endswith('yk') or oneword.endswith('li') or oneword.endswith('ei') or oneword.endswith('mi') or oneword.endswith('ci')\
            or oneword.endswith('zy') or oneword.endswith('yi') or oneword.endswith('rg') or oneword.endswith('si') or oneword.endswith('ji')\
            or oneword.endswith('ni') or oneword.endswith('ii') or oneword.endswith('zi') or oneword.endswith('wi') or oneword.endswith('ej')\
            or oneword.endswith('ai') or oneword.endswith('ui') or oneword.endswith('ce'):
                exp = [oneword, '- TEJ rodzaj męski LP', 'miejscownik']

            if oneword.endswith('ch'):
                exp = [oneword, '- TYCH rodzaj męski LP', 'miejscownik']
            export.append(exp)

    export_final = []
    for f in export:
        if len(f) > 0: export_final.append(f)
    return export_final

