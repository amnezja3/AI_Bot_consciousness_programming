# import coffeeBrain as cf

# words = cf.coffeePls(False)[2]
# meaning = cf.coffeePls(False)[3]

# with open('show.neural', 'w', encoding='utf-8') as show_file:
#     for k, v in words.items():
#         v = str(v)
#         if v.count('#Wielki słownik ortograficzny PWN#*;') > 0 and v.count('•') > 0:
#             try: 
#                 xS = v.split('#Wielki słownik ortograficzny PWN#*;')[1]
#                 try: sc_1 = xS.split('#Synonimy#')[0]
#                 except: sc_1 = xS
#                 # print(k, meaning[k])
#                 mean = meaning[k]
#                 # exp = f'\nmeaning:{k}|{mean}|\n'
                
#                 sc_S = sc_1.split(';')
#                 if mean.startswith('#cz.mowy#czasownik przechodni dokonany'):
#                     # show_file.write(exp)
#                     for s in sc_S:
#                         s = s.strip()
#                         if k != s and s.startswith('-'):
#                             # print('tutaj')
#                             l_x = len(k) - 1
#                             for l in range(len(k)):                                
#                                 # print(k[l_x], s[1], l_x)
#                                 if k[l_x] == s[1]:
#                                     s_index = l_x
#                                     break
#                                 l_x -= 1
#                             baseKey = k[:s_index + 1]
#                             baseLetter = s[2:]
#                             baseList = s.strip().split(', ')

#                             for b in baseList:
#                                 baseLetter_selected = b[2:].replace('•', '').split(': ')[0]
#                                 exp_s = f'meaning:{baseKey}{baseLetter_selected}|{mean}\n'
#                                 show_file.write(exp_s)

#                 if mean.startswith('#cz.mowy#czasownik przechodni niedokonany'):
#                     # show_file.write(exp)
#                     for s in sc_S:
#                         s = s.strip()
#                         if k != s and s.startswith('-'):
#                             # print('tutaj')
#                             l_x = len(k) - 1
#                             for l in range(len(k)):                                
#                                 # print(k[l_x], s[1], l_x)
#                                 if k[l_x] == s[1]:
#                                     s_index = l_x
#                                     break
#                                 l_x -= 1
#                             baseKey = k[:s_index + 1]
#                             baseLetter = s[2:]
#                             baseList = s.strip().split(', ')

#                             for b in baseList:
#                                 baseLetter_selected = b[2:].replace('•', '')
#                                 exp_s = f'meaning:{baseKey}{baseLetter_selected}|{mean}\n'
#                                 show_file.write(exp_s)

#                 if mean.startswith('#cz.mowy#czasownik zwrotny dokonany'):
#                     # show_file.write(exp)
#                     for s in sc_S:
#                         s = s.strip()
#                         if k != s and s.startswith('-'):
#                             # print('tutaj')
#                             l_x = len(k) - 1
#                             for l in range(len(k)):                                
#                                 # print(k[l_x], s[1], l_x)
#                                 if k[l_x] == s[1]:
#                                     s_index = l_x
#                                     break
#                                 l_x -= 1
#                             baseKey = k[:s_index + 1]
#                             baseLetter = s[2:]
#                             baseList = s.strip().split(', ')

#                             for b in baseList:
#                                 baseLetter_selected = b[2:].replace('•', '').replace(' się', '')
#                                 exp_s = f'meaning:{baseKey}{baseLetter_selected}|{mean}\n'
#                                 show_file.write(exp_s)

#                 if mean.startswith('#cz.mowy#czasownik dokonany'):
#                     # show_file.write(exp)
#                     for s in sc_S:
#                         s = s.strip()
#                         if k != s and s.startswith('-'):
#                             # print('tutaj')
#                             l_x = len(k) - 1
#                             for l in range(len(k)):                                
#                                 # print(k[l_x], s[1], l_x)
#                                 if k[l_x] == s[1]:
#                                     s_index = l_x
#                                     break
#                                 l_x -= 1
#                             baseKey = k[:s_index + 1]
#                             baseLetter = s[2:]
#                             baseList = s.strip().split(', ')

#                             for b in baseList:
#                                 baseLetter_selected = b[2:].replace('•', '').replace(' się', '')
#                                 exp_s = f'meaning:{baseKey}{baseLetter_selected}|{mean}\n'
#                                 show_file.write(exp_s)


#                 if mean.startswith('#cz.mowy#czasownik niedokonany'):
#                     # show_file.write(exp)
#                     for s in sc_S:
#                         s = s.strip()
#                         if k != s and s.startswith('-'):
#                             # print('tutaj')
#                             l_x = len(k) - 1
#                             for l in range(len(k)):                                
#                                 # print(k[l_x], s[1], l_x)
#                                 if k[l_x] == s[1]:
#                                     s_index = l_x
#                                     break
#                                 l_x -= 1
#                             baseKey = k[:s_index + 1]
#                             baseLetter = s[2:]
#                             baseList = s.strip().split(', ')

#                             for b in baseList:
#                                 baseLetter_selected = b[2:].replace('•', '').replace(' się', '')
#                                 exp_s = f'meaning:{baseKey}{baseLetter_selected}|{mean}\n'
#                                 show_file.write(exp_s)

#             except: 
#                 xS = v.split('#Wielki słownik ortograficzny PWN#*;')[1]
#                 try: sc_1 = xS.split('#Synonimy#')[0]
#                 except: sc_1 = xS
#                 # print(f'brak cz.Mowy dla {k}\n')
#                 exp = f'brak cz.Mowy dla {k}|{sc_1}\n'
#                 # show_file.write(exp)
#                 # continue
            
        


# zdanie = 'widziałaś tę beznadziejną reklamę w telewizji'
# 'widzę'
# 'ta'
# 'beznadziejny'
# '# brak # reklama'
# 'w'
# '# brak # telewizji'

# word = 'rośnie'
# ortography = words[word].split('#Wielki słownik ortograficzny PWN#')[1] #.split('#Synonimy#')[0].split(';')
# # synonims = words[word].split('#Wielki słownik ortograficzny PWN#')[1].split('#Synonimy#')[1].replace('•', '').split('#')[0].split(';')

# # for z in zdanie.split(' '):
# #     for v in words.values():
# #         if v.replace('•', '').count(z) > 0 and len(z) > 2:
# #             print(z, v)


# # print(ortography)
# # print(synonims)
# # print(meaning[word])








# import wtf
# wtf.usersBaseUpdate('aimseptemduo', 'senten')

# def whatSentention(sentention):
#     sentention = str(sentention)
#     print(sentention)
#     '''
#     polskim wyróżnia się:
#     spójniki współrzędne (parataktyczne):
#     łączne, np. a, i, oraz, tudzież
#     rozłączne, np. albo, bądź, czy, lub
#     wykluczające, np. ani, ni
#     przeciwstawne, np. a, aczkolwiek, ale, jednak, lecz, natomiast, zaś
#     wyjaśniające, np. czyli, mianowicie, ponieważ, to jest
#     wynikowe, np. dlatego, i, przeto, tedy, więc, zatem, toteż
#     spójniki podrzędne (hipotaktyczne), np. aby, bowiem, choć, czy, jeżeli, ponieważ, że.
#     '''
#     categoryS = {
#         'łączne' : [],
#         'rozłączne' : [],
#         'wykluczające' : [],
#         'przeciwstawne' : [],
#         'wyjaśniające' : [],
#         'wynikowe' : [],
#         'hipotaktyczne' : [],

#         'sentention' : sentention
#              }

#     a = sentention.count(' a ')
#     i = sentention.count(' i ')
#     oraz = sentention.count(' oraz ')
#     tudziez = sentention.count(' tudzież ')
#     laczne = a + i + oraz + tudziez
#     if laczne > 0:
#         exp = f'łączne, a({a}), i({i}), oraz({oraz}), tudzież({tudziez})'
#         print(exp)
#         if a > 0: categoryS['łączne'] = categoryS['łączne'] + [' a ']
#         if i > 0: categoryS['łączne'] = categoryS['łączne'] + [' i ']
#         if oraz > 0: categoryS['łączne'] = categoryS['łączne'] + [' oraz ']
#         if tudziez > 0: categoryS['łączne'] = categoryS['łączne'] + [' tudzież ']

#     albo = sentention.count(' albo ')
#     badz = sentention.count(' bądź ')
#     czy = sentention.count(' czy ')
#     lub = sentention.count(' lub ')
#     rozlaczne = albo + badz + czy + lub
#     if rozlaczne > 0:
#         exp = f'rozłączne, albo({albo}), bądź({badz}), czy({czy}), lub({lub})'
#         print(exp)
#         if albo > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + [' albo ']
#         if badz > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + [' bądź ']
#         if czy > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + [' czy ']
#         if lub > 0: categoryS['rozłączne'] = categoryS['rozłączne'] + [' lub ']

#     ani = sentention.count(' ani ')
#     ni = sentention.count(' ni ')
#     wykluczajace = ani + ni
#     if wykluczajace > 0:
#         exp = f'wykluczające, ani({ani}), ni({ni})'
#         print(exp)
#         if ani > 0: categoryS['wykluczające'] = categoryS['wykluczające'] + [' ani ']
#         if ni > 0: categoryS['wykluczające'] = categoryS['wykluczające'] + [' ni ']

#     aP = sentention.count(' a ')
#     aczkolwiek = sentention.count(' aczkolwiek ')
#     ale = sentention.count(' ale ')
#     jednak = sentention.count(' jednak ')
#     lecz = sentention.count(' lecz')
#     natomiast = sentention.count(' natomiast ')
#     zas = sentention.count(' zaś ')
#     przeciwstawne = aP + aczkolwiek + ale + jednak + lecz + zas 
#     if przeciwstawne > 0:
#         exp = f'przeciwstawne, np. a({aP}), aczkolwiek({aczkolwiek}), ale({ale}), jednak({jednak}), lecz({lecz}), natomiast({natomiast}), zas({zas})'
#         print(exp)
#         if aP > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' a ']
#         if aczkolwiek > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' aczkolwiek ']
#         if ale > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' ale ']
#         if jednak > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' jednak ']
#         if lecz > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' lecz ']
#         if natomiast > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' natomiast ']
#         if zas > 0: categoryS['przeciwstawne'] = categoryS['przeciwstawne'] + [' zaś ']

#     czyli = sentention.count(' czyli ')
#     mianowicie = sentention.count(' mianowicie')
#     poniewaz = sentention.count(' ponieważ ')
#     tojest = sentention.count(' to jest ')
#     wyjasniajace = czyli + mianowicie + poniewaz + tojest
#     if wyjasniajace > 0:
#         exp = f'wyjaśniające, czyli({czyli}), mianowicie({mianowicie}), poniewaz({poniewaz}), to jest({tojest})'
#         print(exp)
#         if czyli > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + [' czyli ']
#         if mianowicie > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + [' mianowicie ']
#         if poniewaz > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + [' ponieważ ']
#         if tojest > 0: categoryS['wyjaśniające'] = categoryS['wyjaśniające'] + [' to jest ']


    
#     dlatego = sentention.count(' dlatego ')
#     iW = sentention.count(' i ')
#     przeto = sentention.count(' przeto ')
#     tedy = sentention.count(' tedy ')
#     wiec = sentention.count(' więc ')
#     zatem = sentention.count(' zatem ')
#     totez = sentention.count(' toteż ')
#     wynikowe = dlatego + iW + przeto + tedy + wiec + zatem + totez
#     if wynikowe > 0:
#         exp = f'wynikowe, dlatego({dlatego}), i({iW}), przeto({przeto}), tedy({tedy}) wiec({wiec}) zatem({zatem}) toteż({totez}) '
#         print(exp)
#         if dlatego > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' dlatego ']
#         if iW > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' i ']
#         if przeto > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' przeto ']
#         if tedy > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' tedy ']
#         if wiec > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' więc ']
#         if zatem > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' zatem ']
#         if totez > 0: categoryS['wynikowe'] = categoryS['wynikowe'] + [' toteż ']


    
#     aby = sentention.count(' aby ')
#     bowiem = sentention.count(' bowiem ')
#     choc = sentention.count(' choć ')
#     czyP = sentention.count(' czy ')
#     jezeli = sentention.count(' jeżeli ')
#     poniewaz = sentention.count(' ponieważ ')
#     ze = sentention.count(' że ')
#     podrzedne = aby+ bowiem + choc + czyP + jezeli + poniewaz + ze
#     if podrzedne > 0:
#         exp = f'spójniki podrzędne (hipotaktyczne), np. aby({aby}), bowiem({bowiem}), choć({choc}) czy({czyP}) jeżeli({jezeli}) ponieważ({poniewaz}) że({ze}) '
#         print(exp)
#         if aby > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' aby ']
#         if bowiem > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' bowiem ']
#         if choc > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' choć ']
#         if jezeli > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' jeżeli ']
#         if poniewaz > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' ponieważ ']
#         if ze > 0: categoryS['hipotaktyczne'] = categoryS['hipotaktyczne'] + [' że ']
    
#     return categoryS

# def splitSententionNum(sentention):
#     sentention = str(sentention)
#     print(sentention)
#     exp = set()
#     whatWho = whatSentention(sentention)
#     for k, v in whatWho.items():
#         if len(whatWho[k]) > 0 and k != 'sentention':
#             for a in v:
#                 exp.add(a)

#     for b in exp:
#         sentention = sentention.replace(b, '|').replace(',', '|').replace('||', '|')
#     expA = sentention.split('|')
#     return expA, exp, whatWho


# sent = 'Chcę wyjechać, ale obawiam się podróży, więc odkładam decyzję na później i słabo mi to idzie.'
# print(splitSententionNum(sent)[0])


# whatSentention(sent)
# print()
# whatSentention('Kupiłabym ci prezent, lecz ostatnio zachowujesz się niemile, dlatego nie dostaniesz ode mnie nic!')
# print()
# whatSentention('Chcę, by była już wiosna, ponieważ zimowy krajobraz mnie przygnębia.')
# print()
# whatSentention('Ola, kiedy to usłyszała, zaczęła płakać, więc postanowiliśmy ją pocieszyć, ale nasze działania nie przyniosły rezultatu.')
# print()
# whatSentention('On poszedł z psem aby pomóć mu sie wysikać i zrobić kupę, trzemając go na rękach.')
# print()

# import coffeeBrain as cf

# words = cf.coffeePls(False)[2]
# meaning = cf.coffeePls(False)[3]

# zdanie = 'widziałaś tę beznadziejną reklamę w telewizji'
# 'widzę'
# 'ta'
# 'beznadziejny'
# '# brak # reklama'
# 'w'
# '# brak # telewizji'

# # word = 'widzę'
# # ortography = words[word].split('#Wielki słownik ortograficzny PWN#')[1].split('#Synonimy#')[0].split(';')
# # synonims = words[word].split('#Wielki słownik ortograficzny PWN#')[1].split('#Synonimy#')[1].replace('•', '').split('#')[0].split(';')

# for z in zdanie.split(' '):
#     for v in words.values():
#         if v.replace('•', '').count(z) > 0 and len(z) > 2:
#             print(z, v)


# print(ortography)
# print(synonims)
# print(meaning[word])



# import config
# userDataDict = config.usersBase('aimseptemduo')
# print(userDataDict)

# f = open('brain.neural', 'r', encoding='utf-8')
# file = f.readlines()
# f.close()

# p = open('brain.neural', 'w', encoding='utf-8')
# for a in file:
#     try:
#         p.write(a)
#     except:
#         continue
# p.close()


# import wordConverter as WC
# wcl = WC.wordsNumbersList(True, 'partykuła', 6, 1000)
# for i in wcl:
#     # print(i[0])
#     if i[0].endswith('asz'):
#         print(i[0])
# # print(wcl)





# inp = input('>>>')
# def positionVerb(inp):
#     inp = str(inp)
#     if inp.endswith('eś'):
#         inp = inp.replace('eś', 'em')
#         return inp
#     if inp.endswith('aś'):
#         inp = inp.replace('aś', 'am')
#         return inp
        

#     if inp.endswith(f'asz'):
#         inp = inp.replace(f'asz', f'am')
#         return inp


#     if inp.endswith(f'jesz'):
#         inp = inp.replace(f'jesz', f'ję')
#         return inp

#     elif inp.endswith(f'ziesz'):
#         inp = inp.replace(f'ziesz', f'ę')
#         return inp

#     elif inp.endswith(f'iesz'):
#         inp = inp.replace(f'iesz', f'ę').replace('ź', 'z')
#         return inp

#     elif inp.endswith(f'żesz'):
#         inp = inp.replace(f'żesz', f'gę')
#         return inp

#     elif inp.endswith(f'esz'):
#         inp = inp.replace(f'esz', f'em')
#         return inp


#     if inp.endswith(f'lisz'):
#         inp = inp.replace(f'lisz', f'lę')
#         return inp

#     elif inp.endswith(f'isz'):
#         inp = inp.replace(f'isz', f'ię')
#         return inp


#     if inp.endswith(f'czysz'):
#         inp = inp.replace(f'czysz', f'czę')
#         return inp


    

# print(inp)







# import random
# with open('../sentencje.txt', 'r', encoding='utf-8') as file:
#     listMoods = file.readlines()

# addList = [
#     'żecze -', 'mawia -', 'mówi -'
# ]

# with open('../sentencje_clear.txt', 'w+', encoding='utf-8') as file:
#     counter = 0
#     for x in listMoods:
#         x = x.strip()
#         if x!='' and x!='***':
#             if x.endswith(':'):
                
#                 x = x.replace(':', '')
#                 added = random.choice(addList)
#                 exp = x + f' {added} ' + listMoods[counter - 1].replace(':', '')
#                 print(exp)
#                 file.write('quotations: |' + exp + '\n')
#         counter += 1






# with open('../dowcipy_do_ai.txt', 'r', encoding='utf-8') as file:
#     listMoods = file.readlines()

# with open('../dowcipy_do_ai_clear.txt', 'w+', encoding='utf-8') as file:
#     for x in listMoods:
#         x = x.strip()
#         if x!='':
#             file.write('mood:' + x + '\n')


# import obsControl as obs
# string = 'witam co to jest?'
# print(obs.sendAnswer(string))




# import random
# import wikipedia as wiki
# wiki.set_lang('PL')
# resultsWiki = wiki.search('buddsdasd', results=10, suggestion=False)
# if len(resultsWiki) > 0:
#     print(wiki.page(random.choice(resultsWiki)).summary.strip())


# pip install googlesearch-python
# googlesearch.search(str: term, int: num_results=10, str: lang="en") -> list



# resultNucked = search("Google")
# def checkWeb(pharse):
#     from googlesearch import search
#     from requests import get
#     u_MAIN_agent = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                         'Chrome/61.0.3163.100 Safari/537.36'}
#     resultFull = search(pharse, num_results=10, lang="pl")
#     export = set()
#     for url_i in resultFull:
#         try:
#             res = get(url_i, headers=u_MAIN_agent, proxies=None)    
#             res.raise_for_status()
#             i = res.text
#         except: continue
#         headON = i.count('<head>')
#         headOFF = i.count('</head>')
#         enCODING = i.count('utf')
#         if headON == 1 and headOFF == 1 and enCODING > 0:
#             try: ix = i.split('<head>')[1].split('</head>')[0]
#             except: continue            
#             iy = ix.split('<meta name="')
#             if len(iy) > 1:
#                 for iz in iy:
#                     iiz = iz.split('\n')
#                     for iw in iiz:
#                         iw = str(iw).strip()
#                         if not iw.startswith('<') and iw.endswith('/>'):
#                             countPharse = ix.count(pharse)
#                             if countPharse > 0:
#                                 iiw = iw.replace('"/>', '').split('"')
#                                 for iaw in iiw:
#                                     countDOT = iaw.count('.')

#                                     countIQU = iaw.count('=')
#                                     countHTTP = iaw.count('http')
#                                     countZL = iaw.count('zł')
#                                     countPL = iaw.count('.pl')
#                                     countCOM = iaw.count('.com')
#                                     countORG = iaw.count('.org')
#                                     countWordPress = iaw.count('WordPress')
#                                     countQUOT = iaw.count('&quot;')                               

#                                     MAX_COUNTER = countORG + countCOM + countIQU + countHTTP + countZL + countPL + countWordPress + countQUOT
#                                     if countDOT > 0 and len(iaw) > 70 and MAX_COUNTER == 0:
#                                         export.add(iaw)
#     return export

# print(checkWeb('statek kosmiczny'))

# import wtf

# improve = wtf.leanguageDetector('ola')

# print(improve)




# from googletrans import Translator
# import wtf


# translator = Translator()

# universal = 'ocal mnie'


# detector = translator.detect(universal)
# strDetector = str(detector).replace('Detected(lang=', '').split(', confidence=')[0]

# print(strDetector)
# if strDetector == 'pl':
#     srce = strDetector
#     deste = 'en'
#     speak = 1

# elif strDetector == 'en':
#     srce = strDetector
#     deste = 'pl'
#     speak = 0

# else:
#     srce = 'pl'
#     deste = 'pl'
#     speak = 0

# transEnPl = translator.translate(universal, src=srce, dest=deste)

# strPL = str(transEnPl).split('text=')[1].split(', pronunciation=')[0]

# # print(strPL)

# print(wtf.sayIt(strPL, speak))

# text = 'nie mam pary'
# text1 = 'what are you doing madafaka'

# transEnPl = translator.translate(universal, src='en', dest='pl')
# transPlEn = translator.translate(text, src='pl', dest='en')






# import obsControl as obs

# answerToOBS = obs.obsStart('Fraza')
# print(answerToOBS)


# import neuralWordsNet as nwn
# import wordConverter as wcn


# sentence = 'aha on ty my wy oni niewinny paskuda nadużywanie'
# wordsList = sentence.split(' ')

# testingList = wcn.getDataForWord(wordsList)

# effectAI = nwn.neuralNet(testingList, None, None, None, None, 'kindSpeach', None, None)
# print(effectAI)


# '''
# testingList,
# settingTR, 
# useOldMemory, 
# maxLoops, 
# curcharacters, 
# memoryName,
# kindSpeach,
# maxExample

# '''





# wordConvert = wcn.getKindMemories()
# # print(wordConvert)

# for x in wordConvert:
#     if x[1] == 12:
#         print(x[0])




# import time 
# amountGroun = 12
# rndScor = ['-1', '-x', '-2'] # , 'e', 'o', 'k', 'w', 'p', 'h'

# if len(rndScor) > 6:
#     rndScor = rndScor[:6]

# lenCheckList = len(rndScor)



# print(rndScor)
# amountGroun += 1
# manualList = [a for a in range(0, amountGroun)]

# startTime = time.time()
# trendLists = []
# for r in rndScor:
#     for a in range(len(manualList)):
#         if lenCheckList == 1:
#             exp = f'{a} + "."{r}'
#             trendLists.append(exp)        
#         for b in range(len(manualList)):
#             if lenCheckList == 2:
#                 exp =f'{a}.{b}.{r}'
#                 trendLists.append(exp)                
#             for c in range(len(manualList)):
#                 if lenCheckList == 3:
#                     exp =f'{a}.{b}.{c}.{r}'
#                     trendLists.append(exp)
#                 for d in range(len(manualList)):
#                     if lenCheckList == 4:
#                         exp =f'{a}.{b}.{c}.{d}.{r}'
#                         trendLists.append(exp)
#                     for e in range(len(manualList)):
#                         if lenCheckList == 5:
#                             exp =f'{a}.{b}.{c}.{d}.{e}.{r}'
#                             trendLists.append(exp)
#                         for f in range(len(manualList)):
#                             if lenCheckList == 6:
#                                 exp =f'{a}.{b}.{c}.{d}.{e}.{f}.{r}'
#                                 trendLists.append(exp)

# endTime = time.time()
# print(endTime - startTime)
# print(lenCheckList)
# print(len(trendLists))
# for b in trendLists:
#     print(b)








# e = wtf.partSpeech('być')
# print(e)

# character = 'czy python jest długi'

# # find unicode of P
# for c in character:    
#     unicode_char = ord(c)
#     print(unicode_char)
    
# print(chr(unicode_char))

# f = open('ascii_image.txt', 'r')
# openImage = f.readlines()
# f.close()

# for x in openImage:
#     print(x.strip())

'''
Przez przypadki odmieniają się:
                                rzeczowniki, 
                                przymiotniki, 
                                imiesłowy przymiotnikowe, 
                                część liczebników i zaimków.
(mianownik kto? co?, dopełniacz kogo? czego?, celownik komu? czemu?, biernik kogo? co?, narzędnik z kim? z czym?, miejscownik o kim? o czym?)
'''