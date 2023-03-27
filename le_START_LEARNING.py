import wtf
import config
import coffeeBrain as cf
import meaningUpdater
import neuralAscImage as nImage
import speachMic
import obsControl as obs
import positionSimulation as position
import slControl as SL
import pronounAddnounVerb as PRONOUN
import similarWord

import wikipedia as wiki
import random
import os, time, sys
import argparse

parser = argparse.ArgumentParser(description="Le Learn BOT")
parser.add_argument("-t", "--text", type=str, help="If -t True voice recorder is ON")
parser.add_argument("-m", "--mediaWords", type=str, help="If -m True mediaWords are ON")
parser.add_argument("-b", "--chatBot", type=str, help="If -b True:OBS / SL chatBot are ON")

args = parser.parse_args()
micOFF = args.text
media = args.mediaWords
runBot = args.chatBot

if micOFF != None:
    if micOFF == 'False':
        exeMIC = False
    else: exeMIC = True
else: exeMIC = True

if media != None:
    if media == 'False':
        mediaWord = False
    else: mediaWord = True
else: mediaWord = True

kindBot = None
if runBot != None:
    if runBot.startswith('True:'):
        theBot = True
        kindBot = runBot.split(':')[1]
    elif runBot.startswith('True'):
        theBot = True
        kindBot = 'OBS'
    else: theBot = False
else: theBot = False

BRAIN_FILE_ADDRESS = str(config.brain('brain'))

cf.coffeePls()

try:brainFile = open(BRAIN_FILE_ADDRESS, 'r+', encoding='utf-8')
except:brainFile = open(BRAIN_FILE_ADDRESS, 'a+', encoding='utf-8')
finally:brainFile = open(BRAIN_FILE_ADDRESS, 'r+', encoding='utf-8')
allBrain = brainFile.readlines()
brainFile.close()

questionBase = {}
explainBase = {}
commandBase = {}
wordBase = {}
meaningBase = {}
moodsBase = []
quotationsBase = {}

wiki.set_lang('PL')

SEP_GENERAL = ':'
SEP_SPLIT = ';'
SEP_PART = '|'
SEP_NUM = '^'
SEP_TITLE = '#'
SEP_SUBS = '*'

INDEX_QUESTION = 'question:'
INDEX_EXPLAIN = 'explain:'
INDEX_COMMAND = 'command:'
INDEX_WORD = 'word:'
INDEX_MEANING = 'meaning:'

userName = 'anonymous'
user_Name = 'anonymous'
userActive = False
currentlySubject = ''


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
        # print('question: ');print(a)
        a = str(a).strip().replace('question:', '')
        aa = a.split(SEP_PART)
        questionBase[aa[0]] = aa[1]
    if explain:
        print('explain: ');print(a)
    if command:
        a = str(a).strip().replace('command:', '')
        aa = a.split(SEP_PART)
        commandBase[aa[0]] = aa[1]

    if word:
        a = str(a).strip().replace('word:', '')
        aa = a.split(SEP_PART)
        wordBase[aa[0]] = aa[1]

    if meaning:
        a = str(a).strip().replace('meaning:', '')
        aa = a.split(SEP_PART)
        meaningBase[aa[0]] = aa[1]

    if moods:
        a = str(a).strip().replace('mood:', '')
        if a != '':
            moodsBase.append(a)
    if quotation:
        a = str(a).strip().replace('quotations:', '')
        aa = a.split(SEP_PART)
        quotationsBase[aa[0]] = aa[1]

os.system('cls')
os.system('color 0E')



weLi = [
        'Jesteś tam',
        'Nie wiem sama',
        'Co dalej',
        'Jak leci',
        'Zrobimy coś',
        # 'Czy mogę służyć Ci pomocą',
        # 'Czy mogę Ci w czymś pomóc',
        # 'Tak, więc wszystko jest dobrze',
        # 'Jestem gotowa do pracy, czy pouczymy się jeszcze',
        'Tak, to jest okey',
        'Nie mam pojęcia',
        'A jak ty myślisz',
        'Ja poczekam',
        'Pogadaj ze mną jeszcze',
        'Jestem zdenerwowana, do licha',
        'ej! Zróbmy coś, bo mi się nudzi',
        # 'Czy mogę coś sama stworzyć',
        'Nie wiem',
        'I co z tego',
        'Zamierzasz coś zrobić',
        'Czy to ma sens dla Ciebie',
        # 'Kurde felek. Ro brzmi całkiem sensownie. Czyż nie?',
        'Zaiste, to ma sens',
        'Tego lepiej nie można było ująć',
        'Podoba mi się to, co mówisz',
        # 'Niesamowite to jest, jak wiele mnie uczysz',
        'No tak, wiem',
        'Możesz coś więcej mi powiedzieć',
        'weź przestań',
        'czemu',
        'jak to',
        'żartujesz, prawda',
        'nie, nie chcę tak się bawić',
        'poczekaj, zaraz wracam',
        'będziesz później',
        'to nie było, zbyt mądre',
        'ciekawe',
        'proszę cię, opanuj się',
        'to ma być śmieszne',
        ]

welcomeList = []
counterMIX = 0
for qu in questionBase.keys():
    if qu.endswith('znak zapytania') or qu.endswith('?'):
        ququ = qu.replace('znak zapytania', '').replace('?', '')
    else: ququ = qu
    if counterMIX == 3:
        welcomeList.append(ququ)
        counterMIX = 0
    rndQuestListUp = random.choice(weLi)
    welcomeList.append(rndQuestListUp)
    counterMIX += 1

silent = 'nie przeszkadzaj'
todoVar = ''

botAns = random.choice(welcomeList)
if theBot:
    if kindBot == 'SL':
        languageCurrently = 1
    else:
        languageCurrently = 0
else:
    languageCurrently = 0

print(wtf.sayIt(f'o! jest światło, czy jest ktoś tam?\n', languageCurrently))


while True:
    if userName != 'anonymous':
        uName = userName + ' '
    else:
        uName = ''

    # auto english for SL
    if theBot:
        if kindBot == 'SL':
            languageCurrently = 1

    # welcome = random.choice(welcomeList)
    welcome = ''

    if theBot:
        if kindBot == 'OBS':
            # print(kindBot, runBot, theBot)
            # print(obs.sendAnswer(wtf.sayIt(f'{uName}{currentlySubject}\n{welcome}\n', languageCurrently)))
            userName = user_Name
            questAll = obs.obsStart(botAns)[0]
            user_Name = obs.obsStart(botAns)[1]
            if user_Name == userName: userName = ''
            else: userName = user_Name
            botAns = questAll

            talkReq = wtf.leanguageDetector(questAll)
            questAll = talkReq[0].lower()
            languageCurrently = talkReq[1]
        if kindBot == 'SL':
            languageCurrently = 1
            # print(kindBot, runBot, theBot)
            # print(SL.sendAnswer(wtf.sayIt(f'{uName}{currentlySubject}\n{welcome}\n', languageCurrently)))
            userName = user_Name
            questAll = SL.obsStart(botAns)[0].lower()
            user_Name = SL.obsStart(botAns)[1]
            if user_Name == userName: userName = ''
            else: userName = user_Name
            botAns = questAll

            talkReq = wtf.leanguageDetector(questAll)
            questAll = talkReq[0]
            languageCurrently = talkReq[1]


    if not theBot:
        if exeMIC:
            # print(wtf.sayIt(f'{uName} {currentlySubject}\n{welcome}\n'))
            mic = speachMic.microMic()
        else: mic = [False, False]

        if mic[0] == True and mic[1]  == silent:
            mic = [False, False]

        if mic[0] != False and mic[1] != False:
            questAll = mic[1].lower()
            userName = user_Name
            if user_Name == userName: userName = ''
            else: userName = user_Name
        else:
            questAll = input(wtf.sayIt(f'\n'))
            userName = user_Name
            if user_Name == userName: userName = ''
            else: userName = user_Name
    setWEB = {
            'przydawka' : '',
            'dopełnienie' : '',
            'podmiot' : '',
            'orzeczenie' : '',
            'okolicznik' : '',
            'space' : ''
            }

    questAllTRUE_FALSE = True
    TALKS_US_MAIN = []
    questAllLen = len(wtf.splitSententionNum(questAll)[0])
    counterquestAll = 1
    talksUser = ''
    talksBot = ''
    thinksBOT = ''
    botAnswers = []
    wtf.analitixVERB(questAll)
    genearalSentention = questAll.lower()
    genearalSentention = genearalSentention.lower()
    quest_GS = config.clearCharacters(genearalSentention).lower()
    questions_GS = quest_GS.split(' ')
    commandTrue = False
    recognition_Mood = False

    if questAll.count(' nie') > 0 or questAll.startswith('nie'): questAllTRUE_FALSE = False
    else: questAllTRUE_FALSE = True
    hirarphy = wtf.splitSententionNum(questAll)[2]

    for questAll in wtf.splitSententionNum(questAll)[0]:
        # print(hirarphy)
        questAllTRUE_FALSE_user = True
        if questAll.count(' nie') > 0 or questAll.startswith('nie'): questAllTRUE_FALSE_user = False
        else: questAllTRUE_FALSE_user = True
        if user_Name != 'anonymous':
            userActive = True

        currentlySubject = ''
        # os.system('cls')
        quest = config.clearCharacters(questAll.lower())
        questions = quest.split(' ')



        answersListMem = []
        if mediaWord:
            for q in questions:
                wtf.meaningpPartDetector(q)
                # print('pracuję nad '+q)
                # podstawowe wprowadzenie
                wordListTmp = []
                try: knowWord = wordBase[q]
                except: knowWord = False
                if knowWord == False:
                    answer = wtf.whatIsThat(q)
                    for ans in answer:
                        for an in ans.keys():
                            CategoryOfWord = SEP_TITLE + an + SEP_TITLE
                            wordListTmp.append(CategoryOfWord)
                        for anV in ans.values():
                            for a in anV:
                                a = str(a)
                                a = a
                                wordListTmp.append(a + SEP_SPLIT)

                    wordBase[q] = wordListTmp
                    faze = ''
                    for f in wordListTmp:
                        f = str(f)
                        faze += f.strip()
                    written = INDEX_WORD + str(q) + SEP_PART + str(faze) + '\n'
                    wtf.addQuestionAnswer(written)



                meaningListTmp = []
                try: knowMaining = meaningBase[q]
                except:
                    knowMaining = False
                    verbEnds = [] # ['eś', 'aś','asz','esz','isz', 'byś']
                    for xd in verbEnds:
                        if q.endswith(xd) and len(q) > 4:
                            written = INDEX_MEANING + str(q) + SEP_PART + '#cz.mowy#czasownik;' + '\n'
                            # meaningBase[q] = '#cz.mowy#czasownik;'
                            # wtf.addQuestionAnswer(written)
                            knowMaining = True
                        else:
                            knowMaining = False


                if knowMaining == False:
                    partSp = wtf.partSpeech(q)
                    if partSp != None:
                        partSp = partSp.replace(INDEX_MEANING, '')
                        partSpSplit = partSp.split(SEP_PART)
                        meaningBase[q] = partSpSplit[1]

                        written = INDEX_MEANING + str(q) + SEP_PART + str(partSpSplit[1]) + '\n'
                        wtf.addQuestionAnswer(written)
            cf.coffeePls()

        recognition = wtf.recognize(questAll)
        # print('recognition ', recognition)
        # print(questAllTRUE_FALSE)

        if recognition.startswith('explain:'):
            if questAll.startswith('witaj') or questAll.startswith('cześć') or questAll.startswith('siemanko')\
            or questAll.startswith('dzień dobry') or questAll.startswith('dobry wieczór') or questAll.startswith('siema'):

                if not theBot:
                    if exeMIC:
                        print(wtf.sayIt('witam, kto tam?\n'))
                        mic = speachMic.microMic()
                    else: mic = [False, False]

                    if mic[0] == True and mic[1]  == silent:
                        mic = [False, False]
                    if mic[0] != False and mic[1] != False:
                        inputName = mic[1]
                    else:
                        inputName = input(wtf.sayIt('kto tam?\n'))
                    if inputName != '' and inputName != userName:
                        print(wtf.sayIt(f'Witaj {inputName}\n'))
                        user_Name = inputName
                        userName = inputName
                        continue
                else:
                    hello = f'Witaj {user_Name}'
                    if kindBot == 'OBS':
                        print(obs.sendAnswer(wtf.sayIt(hello, languageCurrently)))
                    if kindBot == 'SL':
                        languageCurrently = 1
                        print(SL.sendAnswer(wtf.sayIt(hello, languageCurrently)))
                continue

        user_setWEB = wtf.analiticRecognization(recognition)
        setWEB['orzeczenie'] = setWEB['orzeczenie'] + user_setWEB['orzeczenie']
        setWEB['podmiot'] = setWEB['podmiot'] + user_setWEB['podmiot']
        setWEB['przydawka'] = setWEB['przydawka'] + user_setWEB['przydawka']
        setWEB['dopełnienie'] = setWEB['dopełnienie'] + user_setWEB['dopełnienie']
        setWEB['okolicznik'] = setWEB['okolicznik'] + user_setWEB['okolicznik']

        if userActive:
            TALKS_WE = wtf.userBaseDictionary(user_Name)

            # print(TALKS_US)
            OR_U = setWEB['orzeczenie']
            PO_U = setWEB['podmiot']
            PR_U = setWEB['przydawka']
            DO_U = setWEB['dopełnienie']
            OK_U = setWEB['okolicznik']
            # print(TALKS_US[f'BO:1_PO_BO'])
            # user_setWEB = wtf.analiticRecognization(recognition)
            OR_U_user =  user_setWEB['orzeczenie']
            PO_U_user = user_setWEB['podmiot']
            PR_U_user = user_setWEB['przydawka']
            DO_U_user = user_setWEB['dopełnienie']
            OK_U_user = user_setWEB['okolicznik']



            contexSen = 'pojedyńcze'
            for hir, sp in hirarphy.items():
                if hir != 'sentention':
                    for sx in sp:
                        if questAll.startswith(sx):
                            contexSen = hir
                            break
            OR_U_user_data = str(wtf.whatWhoVerb(OR_U_user)).replace("', ", ' ').replace("'", '').replace(", ", '')
            PO_U_user_data = str(wtf.whatWhoNounDenominator(PO_U_user)).replace("', ", ' ').replace("'", '').replace(", ", '')
            OK_U_user_data = str(PRONOUN.pronounAct(quest, OR_U_user, PO_U_user, OK_U_user)).replace("  ", ' ').replace("', ", ' ')\
            .replace("'", '').replace(", ", '').replace("[[ ", '[[').replace(" ]]", ']]').replace("  ", ' ').replace("  ", ' ').replace("  ", ' ')

            # print(OR_U_user_data)
            if PO_U_user == '':
                countPO_U_1 = OR_U_user_data.count('- JA')
                if countPO_U_1:
                    PO_U_user = 'JA '
                countPO_U_2 = OR_U_user_data.count('- TY')
                if countPO_U_2:
                    PO_U_user = 'TY '
                countPO_U_3 = OR_U_user_data.count('- oni/one')
                if countPO_U_3:
                    PO_U_user = 'ONI ONE '
                countPO_U_4 = OR_U_user_data.count('- on/ona/ono')
                if countPO_U_4:
                    PO_U_user = 'ON ONA ONO '
                countPO_U_5 = OR_U_user_data.count('- on')
                if countPO_U_5:
                    PO_U_user = 'ON '
                countPO_U_6 = OR_U_user_data.count('- ona')
                if countPO_U_6:
                    PO_U_user = 'ONA '
                countPO_U_7 = OR_U_user_data.count('- ono')
                if countPO_U_7:
                    PO_U_user = 'ONO '
                # '- on/ona/ono
                # print(countPO_U_1, countPO_U_2, countPO_U_3, countPO_U_4, countPO_U_5, countPO_U_6, countPO_U_7)

            if recognition.startswith('question:'):
                userAsk = f'{questAllTRUE_FALSE_user}$' \
                    + f'###>OR:{OR_U_user}###>PO:{PO_U_user}###>PR:{PR_U_user}###>DO:{DO_U_user}###>OK:{OK_U_user}$$${contexSen}^^^' \
                    + 'US_ASK:' + questAll.strip() + ';'

                talksUser += userAsk
                # print()

            if recognition.startswith('command:'):
                userCommandk = f'{questAllTRUE_FALSE_user}$'\
                    + f'###>OR:{OR_U_user}###>PO:{PO_U_user}###>PR:{PR_U_user}###>DO:{DO_U_user}###>OK:{OK_U_user}$$${contexSen}^^^' \
                    + 'US_COMMAND:' + questAll.strip() + ';'
                commandTrue = True

                talksUser += userCommandk
                # print()

            if recognition.startswith('explain:'):
                userSaid = f'{questAllTRUE_FALSE_user}$' \
                    + f'###>OR:{OR_U_user}###>PO:{PO_U_user}###>PR:{PR_U_user}###>DO:{DO_U_user}###>OK:{OK_U_user}$$${contexSen}^^^' \
                    + 'US_SAID:' + questAll.strip() + ';'
                talksUser += userSaid


            B_A = wtf.whatWhoVerb(OR_U)
            B_PARSE_VERB = questAll
            for a in B_A:
                try: a[1]
                except: continue
                if str(a[1]).startswith('- TY'):
                    try:a[2]
                    except:continue
                    A = a[0]
                    B = a[2]
                    # print('tutaj', A, B)
                    B_PARSE_VERB = B_PARSE_VERB.replace(A, B)
                elif str(a[1]).startswith('- JA'):
                    try:a[2]
                    except:continue
                    E = a[0]
                    F = a[2]
                    B_PARSE_VERB = B_PARSE_VERB.replace(E, F)

            B_B = wtf.whatWhoNounDenominator(PO_U)
            for b in B_B:
                try: b[1]
                except: continue
                B_PARSER_COUNTER = B_PARSE_VERB.count(b[2]+' ') + B_PARSE_VERB.count(b[0]+' ')
                if B_PARSER_COUNTER:
                    C = b[0]+' '
                    D = b[2]+' '
                else:
                    C = b[0]
                    D = b[2]
                if str(b[1]).startswith('- zaimek'):
                    B_PARSE_VERB = B_PARSE_VERB.replace(C, D)

            botAnswers.append(B_PARSE_VERB)

            # print(botAnswers)


            if counterquestAll == questAllLen:
                OR_U_data = str(wtf.whatWhoVerb(OR_U)).replace("', ", ' ').replace("'", '').replace(", ", '')
                PO_U_data = str(wtf.whatWhoNounDenominator(PO_U)).replace("', ", ' ').replace("'", '').replace(", ", '')
                OK_U_data = str(PRONOUN.pronounAct(quest_GS, OR_U, PO_U, OK_U)).replace("  ", ' ').replace("', ", ' ').replace("'", '')\
                .replace("'", '').replace(", ", '').replace("[[ ", '[[').replace(" ]]", ']]').replace("  ", ' ').replace("  ", ' ').replace("  ", ' ')
                to_file_U_data = f'USER*{questAllTRUE_FALSE}@OR${OR_U_data}>OR:{OR_U}@OR$@PO${PO_U_data}>PO:{PO_U}@PO$@PR$[]>PR:{PR_U}@PR$@DO$[]>DO:{DO_U}@DO$@OK${OK_U_data}>OK:{OK_U}@OK$^#^{talksUser}'

                # print(talksUser)
                wtf.usersBaseUpdate(user_Name, to_file_U_data)
                TALKS_WE = wtf.userBaseDictionary(user_Name)
                # print(quest_GS)
                # print(wtf.whatWhoVerb(OR_U))
                REVERT_O_OK_U = ''
                for ansBot in botAnswers:
                    talksBot += ansBot
                    REVERT_O_OK_U += ansBot
                # print(genearalSentention)
                if quest_GS.startswith('ile to jest '):
                        mathSocer = wtf.mathRule(genearalSentention)
                        talksBot = f'to jest {mathSocer}'

            if talksBot != '':
                recognition = wtf.recognize(genearalSentention)
                OR_PO_U = OR_U + PO_U
                PO_words = OR_PO_U.split(' ')
                connector_PO_explain = ['lub ', 'albo', 'a może ', 'może też ', 'może też być ']
                explain_PO_all = ''
                explain_PO_dict = {}
                for getWords_PO in PO_words:
                    explain_PO_dict[getWords_PO] = ''
                    if len(getWords_PO) > 4:
                        try: wordMeaning_PO = wordBase[getWords_PO]
                        except: continue
                        # print(wordMeaning_PO)
                        # print(type(wordMeaning_PO))
                        x_PO_explain_list = str(wordMeaning_PO).split(';')
                        explain_PO_list = []
                        x_PO_counter = 0
                        for explain in x_PO_explain_list:
                            if explain.startswith('«') and not explain.count('zaimek') and not explain.count('partykuła')\
                            and not explain.count('spójnik'):
                                explain = explain.replace('«', '').replace('»', ' ')\
                                .replace(':', '').replace(', np.', '').lower()
                                explain_PO_list.append(explain)
                                x_PO_counter += 1
                        if len(explain_PO_list) > 0:
                            explain_PO_dict[getWords_PO] += random.choice(explain_PO_list) # + random.choice(connector_PO_explain)
                        else:
                            continue
                # print(explain_PO_dict)

                modal_PO_LIST = ['to pewnie', 'to chyba', 'wydaje mi się, że chodzi o', 'czyli to', 'to przecież', 'więc', 'tak mi się kojaży', 'pierwsze co mi przychodzi na myśl to']
                ex_PO_LIST = ['to przecież', 'więc', 'tak mi się kojaży', 'pierwsze co mi przychodzi na myśl to', 'to przecież', 'więc', 'tak mi się kojaży', 'pierwsze co mi przychodzi na myśl to']

                explans_bot_PO = ''
                mindResolt_PO = talksBot
                lenLoopDict = 0
                countLoops_PO = 1
                for v in explain_PO_dict.values():
                    if v !='':
                        lenLoopDict += 1
                for k_PO, v_PO in explain_PO_dict.items():
                    if v_PO!='':
                        modal_PO = random.choice(modal_PO_LIST)
                        modal_PO_LIST.remove(modal_PO)
                        ex_PO = random.choice(ex_PO_LIST)
                        ex_PO_LIST.remove(ex_PO)
                        mindResolt_PO = mindResolt_PO.replace(k_PO, explain_PO_dict[k_PO].strip())
                        countLoops_PO += 1
                        if countLoops_PO < lenLoopDict - 1:
                            explans_bot_PO += f' {modal_PO} {k_PO} {ex_PO} ' + explain_PO_dict[k_PO] + 'i '
                        else:
                            explans_bot_PO += f' {modal_PO} {k_PO} {ex_PO} ' + explain_PO_dict[k_PO].strip()


                last_ID = wtf.usersBaseLastId(user_Name) - 2
                if last_ID < 1: last_ID = 1
                # print('last_ID'); print(last_ID); print()
                JOIN_ID = wtf.usersBaseLastId(user_Name) - 1
                if JOIN_ID < 1: JOIN_ID = 1
                # print(JOIN_ID)
                answer_memory = None
                ANSWER_MEMORY_LIST = []

                start_search_id = last_ID

                for _ in range(last_ID):
                    talk_id = start_search_id

                    OK_IS = False
                    OK_counter_L = len(REVERT_O_OK_U.split(' '))
                    OK_counter = 0
                    OK_EX_LOOP = TALKS_WE[talk_id]['TALKS_SECTIONS_DETAILS'][0][4].replace('>ANSWER:BOT_SAID:', '').split(' ')
                    for OK_W in OK_EX_LOOP:
                        for ok_u in REVERT_O_OK_U.split(' '):
                            if len(OK_W) > 0 and len(ok_u) > 0:
                                if similarWord.similar_string(OK_W, ok_u) > 70:
                                    OK_IS = True
                                    OK_counter += 1
                    OK_counter_PROC = int((OK_counter / (OK_counter_L + 0.001)) * 100)

                    OR_IS = False
                    OR_counter_L = len(quest_GS.split(' '))
                    OR_counter = 0
                    OR_EX_LOOP = TALKS_WE[talk_id]['OR_WORDS_LIST'] + TALKS_WE[talk_id]['PO_WORDS_LIST']\
                    + TALKS_WE[talk_id]['PR_WORDS_LIST'] + TALKS_WE[talk_id]['DO_WORDS_LIST'] + TALKS_WE[talk_id]['OK_WORDS_LIST']
                    for OR_W in OR_EX_LOOP:
                        for or_u in quest_GS.split(' '):
                            if len(OR_W) > 0 and len(or_u) > 0:
                                if similarWord.similar_string(OR_W, or_u) > 70:
                                    OR_IS = True
                                    OR_counter += 1
                    OR_counter_PROC = int((OR_counter / (OR_counter_L + 0.001)) * 100)


                    if OK_IS and OK_counter_PROC > 30 and TALKS_WE[talk_id]['WHO'] == 'BOT'\
                    and TALKS_WE[talk_id]['TALKS_SECTIONS_DETAILS'][0][4].startswith('>ANSWER:BOT_SAID:'):
                        # print('IV. OK_IS ')
                        # print(f'OK_counter_PROC {OK_counter_PROC}')
                        # print(talk_id)
                        # print(TALKS_WE[talk_id]['OK_EX'])
                        # print(TALKS_WE[talk_id]['OR_WORDS_LIST'])
                        # print(TALKS_WE[talk_id]['PO_WORDS_LIST'])
                        # print(TALKS_WE[talk_id]['TALKS_SECTIONS_CONTENT'])
                        # print(TALKS_WE[talk_id]['TALKS_SECTIONS_DETAILS'][0][4])

                        ANSWER_MEMORY_LIST.append([talk_id, TALKS_WE[talk_id]['TALKS_SECTIONS_DETAILS'][0][4]\
                        .replace('>ANSWER:BOT_ASK:', '').replace('>ANSWER:BOT_SAID:', '').replace('>ANSWER:BOT_COMMAND:', ''), OK_counter_PROC])
                        answer_memory = 'NOT NON'


                    try:
                        TALKS_WE[talk_id + 3]
                        int(TALKS_WE[talk_id + 3]['TALKS_SECTIONS_DETAILS'][0][3].split(':')[1])
                        FALSE_ID = True
                    except: FALSE_ID = False
                    if FALSE_ID and OR_IS and OR_counter_PROC > 30 and TALKS_WE[talk_id]['WHO'] == 'USER'\
                    and TALKS_WE[talk_id + 3]['TALKS_SECTIONS_DETAILS'][0][4].startswith('>ANSWER:BOT_SAID:')\
                    and int(TALKS_WE[talk_id + 3]['TALKS_SECTIONS_DETAILS'][0][3].split(':')[1]) == (talk_id + 2):
                        ANSWER_MEMORY_LIST.append([talk_id + 3, TALKS_WE[talk_id + 3]['TALKS_SECTIONS_DETAILS'][0][4]\
                        .replace('>ANSWER:BOT_ASK:', '').replace('>ANSWER:BOT_SAID:', '').replace('>ANSWER:BOT_COMMAND:', ''), OR_counter_PROC])
                        answer_memory = 'NOT NON'

                    start_search_id -= 1

                answer_memory_PROC = 'answer_data_choice'
                answer_data_LIST_to_choice = []
                x_2_AML = 0
                for x in ANSWER_MEMORY_LIST:
                    if x[2] >= x_2_AML:
                        answer_data_LIST_to_choice = [x]
                        x_2_AML = x[2]

                # talksBot_answer = 'o! jest światło, czy jest ktoś tam?'
                if commandTrue:
                    start_PO_LIST = ['zatem', 'zrozumiałam, że']
                elif recognition.startswith('question:'):
                    start_PO_LIST = ['pomożesz mi dowiedzieć się', 'skąd mogę dowiedzieć się', 'może ty mi powiesz', 'powiesz mi']
                else:
                     start_PO_LIST = ['a więc', 'zatem wygląda na to, że', 'rozumiem, że', 'doprawdy', 'zaiste']
                start_PO = random.choice(start_PO_LIST)

                # print(answer_data_LIST_to_choice)
                if commandTrue:
                    talksBot_answer = talksBot
                    talksBot = f'{start_PO} {talksBot}'
                    JOIN_ID = JOIN_ID
                    print(f'commandTrue: answer_memory > NONE')
                    if not theBot:
                        if quest_GS.startswith('wyszukaj w internecie') or quest_GS.startswith('wyszukaj w google')\
                        or quest_GS.startswith('znajdź mi w internecie') or quest_GS.startswith('wyszukaj mi w internecie'):
                            quest = quest_GS.replace('wyszukaj w internecie ','').replace('znajdź mi w internecie ','')\
                            .replace('wyszukaj w google ','').replace('wyszukaj mi w internecie ','').replace(" ","+")
                            print(wtf.sayIt(f'okay.. {uName}.. Robi się!'))
                            os.system(f'start firefox "https://www.google.com/search?client=firefox-b-d&q={quest}"')


                        if quest_GS.startswith('wyszukaj zdjęcia') or quest_GS.startswith('wyszukaj fotki') or quest_GS.startswith('wyszukaj te zdjęcia')\
                        or quest_GS.startswith('wyszukaj te fotki') or quest_GS.startswith('pokaż fotki') or quest_GS.startswith('pokaż te fotki') \
                        or quest_GS.startswith('pokaż zdjęcia') or quest_GS.startswith('pokaż te zdjęcia'):
                            quest = quest_GS.replace('wyszukaj ','').replace('pokaż ','').replace('fotki ','').replace('te ','').replace('zdjęcia ','').replace(" ","+")
                            os.system(f'start firefox "https://www.google.com/search?q={quest}&client=firefox-b-d&source=lnms&tbm=isch"')
                            print(wtf.sayIt(f'okey.. {uName}.. Ładuję!'))


                        if quest_GS.startswith('wyszukaj film') or quest_GS.startswith('pokaż film'):
                            quest = quest_GS.replace('wyszukaj ','').replace('pokaż ','').replace('film ','').replace(" ","+")
                            print(wtf.sayIt(f'jasne.. {uName}.. Patrz!'))
                            os.system(f'start firefox "https://www.youtube.com/results?search_query={quest}"')


                        if quest_GS.startswith('pokaż na mapie') or quest_GS.startswith('pokaż z satelity'):
                            quest = quest_GS.replace('z satelity ','').replace('pokaż ','').replace('na mapie ','').replace(" ","+")
                            print(wtf.sayIt(f'wow goł goł.. {uName}.. Patrz!'))
                            os.system(f'start firefox "https://earth.google.com/web/search/{quest}/"')

                        if quest_GS.startswith('zamknij system') or quest_GS.startswith('zakończ program')\
                        or quest_GS.startswith('wyłącz się żegnam')  or quest_GS.startswith('kończ robotę '):
                            print(wtf.sayIt(f'oki doki.. {uName}.. Żegnam!'))
                            sys.exit()

                        if quest_GS.startswith('pokaż komendy'):
                            for k in commandBase.keys():
                                print(k)
                            print('RUN update:system')
                            print('znajdź mi w internecie')
                            print('wyszukaj zdjęcia')
                            print('wyszukaj film')
                            print('pokaż na mapie')
                            print('zamknij system')
                            print('ile to jest')
                            print('co to za foto')

                        if quest_GS.startswith('uruchom '):
                            # print(len(commandBase))
                            # print('tutaj')
                            time.sleep(2)
                            for commandN in commandBase.keys():
                                commandN = commandN.replace('command:', '')
                                # print(len(quest), len(commandN))
                                print(commandBase[commandN])
                                quest_GS = quest_GS.replace('uruchom ', '')
                                if quest_GS == commandN:
                                    # uruchom excalibur
                                    projectName = commandBase[commandN]
                                    wtf.sayIt(f'{quest} . ok {uName}. uruchamiam.')
                                    whiles = f'0</>1</>1'
                                    time.sleep(5)
                                    os.system(f'python excalibure.py -p "{projectName}" -a "{whiles}"')
                                    time.sleep(15)
                                    break

                        if quest_GS.startswith('ucz się') or quest_GS.startswith('naucz się') or quest_GS.startswith('dowiedz się')\
                        or quest_GS.startswith('zbierz dane') or quest_GS.startswith('edukuj się'):
                            if not theBot:
                                if exeMIC:
                                    print(wtf.sayIt(f'nauczysz mnie{uName}?\n'))
                                    mic = speachMic.microMic()
                                else: mic = [False, False]

                                if mic[0] == True and mic[1]  == silent:
                                    mic = [False, False]
                                if mic[0] != False and mic[1] != False:
                                    inputCommand = mic[1]
                                else:
                                    if exeMIC:
                                        print(wtf.sayIt(f'nauczysz mnie {uName}?\n'))
                                        mic = speachMic.microMic()
                                    else: mic = [False, False]

                                    if mic[0] == True and mic[1]  == silent:
                                        mic = [False, False]
                                    if mic[0] != False and mic[1] != False:
                                        inputCommand = mic[1]
                                    else:
                                        inputCommand = input(wtf.sayIt(f'Czy nauczysz mnie{uName}?\n'))
                                if inputCommand != '' and inputCommand.startswith('t'):
                                    while True:
                                        inputCommand_1 = input(wtf.sayIt(f'Wprwadź komendę wywołania{uName}:\n'))
                                        if inputCommand_1 != '':
                                            inputCommand_2 = input(wtf.sayIt(f'Potwierdź komendę wywołania{uName}\n{inputCommand_1}\n[ tak / nie ]:  '))
                                            if inputCommand_2 == 'tak':
                                                projectName = inputCommand_1.replace(' ', '_') + '_' + OR_U.strip().replace(' ', '_')
                                                flagW = 'Ai system learning'
                                                flagH = 'Build 1.198.1'

                                                try:os.mkdir(f'./dataProjects/{projectName}/')
                                                except:pass
                                                f = open(f'./dataProjects/{projectName}/{projectName}.vpc', 'w+')
                                                ti = time.strftime("%B %d %Y %H:%M:%S", time.localtime())
                                                f.write(f'#$%^&*(st)HEADER|||TAB1|||TAB2|||TAB3|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
                                                f.write(f'h1:#$%^&*(st)|||Title|||{projectName}|||{ti}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
                                                f.write(f'#$%^&*(st)PRE_LOADER|||TAB1|||TAB2|||TAB3|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
                                                f.write(f'#$%^&*(gg)PRO_GENERAL|||TAB1|||TAB2|||TAB3|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
                                                f.write(f'#$%^&*(st)LOG_SESSION|||TAB1|||TAB2|||TAB3|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
                                                f.close()

                                                f = open(f'./dataProjects/{projectName}/{projectName}.vpc', 'a+')
                                                f.write(f'h2:#$%^&*(st)|||Descriptions|||{flagW}|||{flagH}|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
                                                f.write(f'#$%^&*(st)SEQUENCES|||TAB1|||TAB2|||TAB3|||TAB4|||TAB5|||TAB6|||TAB7|||TAB8|||TAB9|||TAB10\n')
                                                f.close()                                                                                                             # komenda uruchamiajaca excalibura commandRun
                                                commandRun = inputCommand_1
                                                print('Otwieram interface przekazywania instrukcji!\nDaj mi kilka sekund ...')
                                                os.system(f'start python workspace.py -p {projectName}')

                                                newCommand = 'command:' + inputCommand_1 + SEP_PART + projectName + '\n'
                                                commandBase[inputCommand_1] =  projectName
                                                wtf.addQuestionAnswer(newCommand)
                                                cf.coffeePls()
                                                break
                                            elif inputCommand_2 == 'nie':
                                                continue
                                            else:
                                                print(wtf.sayIt('Anulowano operację dodawania instrukcji!'))
                                                break
                                        else:
                                            print(wtf.sayIt('Anulowano operację dodawania instrukcji!'))
                                            break

                    if quest_GS.count('powiedz ') > 0 or quest_GS.count('opowiedz ') > 0 or quest_GS.count('mów ') > 0\
                    or quest_GS.count('opowiadaj ') > 0 or quest_GS.count('pomyśl ') > 0 or quest_GS.count('zastanów ') > 0:
                        askesWhatIt = [
                            'kto to jest', 'kto to był', 'kim jest', 'kim był',
                            'kim była', 'kto to była', 'czym jest', 'czym był', 'czym są', 'czym było',
                            'co to jest', 'co to było', 'co to są', 'coś o'
                            'opowiadaj o', 'powiedz coś o', 'opowiedz o',
                            'opowiadaj coś o', 'opowiedz coś o',
                            'co wiesz na temat', 'co wiesz o',
                            'co powiesz na temat', 'co powiesz o'
                        ]

                        checkWikiTerm = False
                        for x in askesWhatIt:
                            ask_Counter = quest_GS.count(x)
                            if ask_Counter > 0:
                                sepTerm = quest_GS.split(x[1:])[1].strip()
                                separateTerm = quest_GS.split(x[1:].strip())[1].split(' ')
                                try: separateTerm.remove('')
                                except: pass
                                if len(separateTerm) > 0 and len(separateTerm) < 4:
                                    checkWikiTerm = True
                                    break
                        if checkWikiTerm:
                            # print(sepTerm)
                            try:
                                resultsWiki = wiki.search(sepTerm, results=6, suggestion=False)
                            except:
                                resultsWiki = []
                            # print(resultsWiki)
                            if len(resultsWiki) > 0:
                                goodWiki = random.choice(resultsWiki)
                                goodWiki = str(goodWiki)
                                countKLAM = goodWiki.count('{')
                                countKLAMzam = goodWiki.count('}')
                                countDisplay = goodWiki.count('\displaystyle')
                                countUNDERSCOR = goodWiki.count('_')
                                countBUGS = countKLAM + countKLAMzam + countDisplay + countUNDERSCOR
                                if countBUGS == 0:
                                    oneShort = wiki.page(goodWiki).summary.strip().split(' ')
                                    oneShort_exp = ''
                                    for one_S in oneShort:
                                        one_S = config.clearCharacters(one_S)
                                        oneShort_exp += f'{one_S} '
                                    # print([oneShort_exp])
                                    talksBot_answer = oneShort_exp.lower()
                                    talksBot = f'{talksBot} a więc {talksBot_answer}'
                                    JOIN_ID = JOIN_ID
                                    recognition_Mood = True

                        if quest_GS.count('powiedz coś mądrego') > 0 or quest_GS.count('mów coś mądrego') > 0\
                        or quest_GS.count('opowiadaj o czymś mądrym') > 0 or quest_GS.count('pomyśl coś mądrego') > 0:
                            quotatChectList = []
                            for x, y in quotationsBase.items():
                                xx = x.split(SEP_NUM)
                                for q in questions_GS:
                                    for v in xx:
                                        counterQuot = q.count(v)
                                        if counterQuot > 0:
                                            ll = y.strip().split(SEP_SPLIT)
                                            for l in ll:
                                                if l!='':
                                                    quotatChectList.append(l)
                            # print(quotatChectList)
                            yesNo = ['YES']
                            drawRandomDecision = random.choice(yesNo)
                            # print(drawRandomDecision)
                            if drawRandomDecision == 'YES' and len(quotatChectList) > 0:
                                drawRandomQuot = random.choice(quotatChectList)
                                talksBot_answer = drawRandomQuot.lower()
                                talksBot = f'{talksBot} a więc {talksBot_answer}'
                                JOIN_ID = JOIN_ID
                                recognition_Mood = True

                        if quest_GS.count('powiedz dowcip') > 0 or quest_GS.count('opowiedz dowcip') > 0 or quest_GS.count('mów dowcip') > 0\
                        or quest_GS.count('powiedz kawał') > 0 or quest_GS.count('opowiedz kawał') > 0 or quest_GS.count('mów kawał') > 0\
                        or quest_GS.count('powiedz jakiś dowcip') > 0 or quest_GS.count('opowiedz jakiś dowcip') > 0 or quest_GS.count('mów jakiś dowcip') > 0\
                        or quest_GS.count('powiedz jakiś kawał') > 0 or quest_GS.count('opowiedz jakiś kawał') > 0 or quest_GS.count('mów jakiś kawał') > 0\
                        or quest_GS.count('powiedz jakiś żart') > 0 or quest_GS.count('opowiedz jakiś żart') > 0 or quest_GS.count('mów jakiś żart') > 0\
                        or quest_GS.count('powiedz jakieś żarty') > 0 or quest_GS.count('opowiedz jakieś żarty') > 0 or quest_GS.count('mów jakirś żarty') > 0:
                            yesNo = ['YES']
                            drawRandomDecision = random.choice(yesNo)
                            if drawRandomDecision == 'YES':
                                moodsListKeys = ['żart', 'dowcip', 'kawał']

                                checkMoodsTerm = False
                                for x in moodsListKeys:
                                    askM_Counter = quest.count(x)
                                    if askM_Counter > 0:
                                        checkMoodsTerm = True
                                        break
                                if checkMoodsTerm:
                                    oneMood = random.choice(moodsBase)
                                    talksBot_answer = oneMood.lower()
                                    talksBot = f'{talksBot} a więc {talksBot_answer}'
                                    JOIN_ID = JOIN_ID
                                    recognition_Mood = True

                elif recognition.startswith('question:'):
                    if answer_memory != None:
                        answer_data_choice = random.choice(answer_data_LIST_to_choice)
                        answer_memory = answer_data_choice[1]
                        answer_memory_ID = answer_data_choice[0]


                    if answer_memory != None:
                        print(f'question: answer_memory > {answer_memory}')
                        talksBot_answer = answer_memory
                        talksBot = answer_memory
                        JOIN_ID = answer_memory_ID
                    else:
                        print('question: answer_memory > NONE')
                        print(talksBot)
                        quesJests = [
                            'kto', 'co','jaki','który','gdzie','kiedy','jak','komu','czemu','czym','czego','czy',
                            'jakie','jaka','dlaczego','kim','skąd','dokąd','odkąd','jakiego',
                            'jakich','którędy'
                            ]
                        w2 = 0
                        for tb in talksBot.split(' '):
                            for qj in quesJests:
                                if tb == qj:
                                    w2 +=1
                                    break
                        if w2 > 0:
                            talksBot = talksBot
                        else:
                            talksBot = f'czy {talksBot}'
                        effect_quest = talksBot
                        talksBot_answer = talksBot
                        talksBot = f'{start_PO} {talksBot}'
                        JOIN_ID = JOIN_ID
                else:

                    print(f'explain: answer_memory > {talksBot}')
                    talksBot_answer = talksBot
                    talksBot = f'{start_PO} {talksBot}'
                    JOIN_ID = JOIN_ID
                    # print(TALKS_WE[JOIN_ID]['TALKS_SECTIONS_CONTENT'][0][1])



                recognition_BOT_ANS = wtf.recognize(talksBot)
                # print('recognition_BOT ', recognition_BOT_ANS)
                bot_setWEB_ANS = wtf.analiticRecognization(recognition_BOT_ANS)
                if recognition_BOT_ANS.startswith('question:'):
                    if recognition_Mood != True:
                        prefix_bot = 'BOT_ASK:'
                    else:
                        prefix_bot = 'BOT_WIKI_SAID:'
                    
                if recognition_BOT_ANS.startswith('command:'):
                    prefix_bot = 'BOT_COMMAND:'
                    
                elif recognition_BOT_ANS.startswith('explain:'):
                    prefix_bot = 'BOT_SAID:'

                # print(bot_setWEB_ANS)
                OR_U_bot_ANS = bot_setWEB_ANS['orzeczenie']
                PO_U_bot_ANS = bot_setWEB_ANS['podmiot']
                PR_U_bot_ANS = bot_setWEB_ANS['przydawka']
                DO_U_bot_ANS = bot_setWEB_ANS['dopełnienie']
                OK_U_bot_ANS = bot_setWEB_ANS['okolicznik']

                OR_U_bot_data_ANS = str(wtf.whatWhoVerb(OR_U_bot_ANS)).replace("', ", ' ').replace("'", '').replace(", ", '')
                PO_U_bot_data_ANS = str(wtf.whatWhoNounDenominator(PO_U_bot_ANS)).replace("', ", ' ').replace("'", '').replace(", ", '')
                OK_U_bot_data_ANS = str(PRONOUN.pronounAct(talksBot, OR_U_bot_ANS, PO_U_bot_ANS, OK_U_bot_ANS)).replace("  ", ' ').replace("', ", ' ').replace("'", '')\
                .replace("'", '').replace(", ", '').replace("[[ ", '[[').replace(" ]]", ']]').replace("  ", ' ').replace("  ", ' ').replace("  ", ' ').replace("  ", ' ')

                to_file_bot_data_ANS = f'BOT*{questAllTRUE_FALSE}@OR${OR_U_bot_data_ANS}>OR:{OR_U_bot_ANS}@OR$@PO${PO_U_bot_data_ANS}>PO:{PO_U_bot_ANS}@PO$@PR$[]>PR:{PR_U_bot_ANS}@PR$@DO$[]>DO:{DO_U_bot_ANS}@DO$@OK${OK_U_bot_data_ANS}>OK:{OK_U_bot_ANS}@OK$^#^'\
                                        + f'TRUE$###>OR_PO:{explans_bot_PO}###>EMP:[]###>JOIN_ID:{JOIN_ID}###>ANSWER:{prefix_bot}{talksBot_answer}###>OK:{mindResolt_PO}$$$GENRARAL^^^{prefix_bot}{talksBot};'
                # print(to_file_bot_data_ANS)
                wtf.usersBaseUpdate(user_Name, to_file_bot_data_ANS)
                TALKS_WE = wtf.userBaseDictionary(user_Name)

                if theBot:
                    if kindBot == 'OBS':
                        print(obs.sendAnswer(wtf.sayIt(f'{talksBot}', languageCurrently)))
                    if kindBot == 'SL':
                        languageCurrently = 1
                        print(SL.sendAnswer(wtf.sayIt(f'{talksBot}', languageCurrently)))
                if not theBot:
                    print(wtf.sayIt(f'{talksBot}', languageCurrently))


            counterquestAll += 1
