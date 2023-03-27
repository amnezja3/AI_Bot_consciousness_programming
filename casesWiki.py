def partSpeech(word):
    import requests
    import config

    TMP_WIKI = str(config.brain('wiki'))


    url = f'https://pl.wiktionary.org/wiki/{word}'  
    r = requests.get(url)
    htmlSTR = r.text 
    exp = []
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
        f = str(f).strip()
        if f.count('liczba mnoga') > 0:
            ff = f.split('<td class="') #[1].replace('</td>', '')
            for a in ff:                
                if a.startswith('mianownik">'):
                    
                    try: mianownik = a.replace('mianownik">', '').replace('</td>', '').replace('</tr><tr class="forma">', '') # .split('<')[0]
                    except: mianownik = ''
                    if mianownik.count('>') > 0:
                        listMianownik = mianownik.split('>')
                        for lm in listMianownik:
                            if lm.startswith(word[:int(len(word) * 0.7)]):
                                mianownik = lm.split('<')[0].replace(' / ', '')
                                if len(mianownik) > 0 and len(mianownik) < len(word) + 4:                            
                                    expM = 'meaning:' + mianownik + '|#cz.mowy#rzeczownik odmiana mianownik;'
                                    exp.append(expM)
                                    break
                    else:
                        if len(mianownik) > 0 and len(mianownik) < len(word) + 4:
                            expM = 'meaning:' + mianownik + '|#cz.mowy#rzeczownik odmiana mianownik;'
                            exp.append(expM)

            aa = f.split('title="')
            for a in aa:
                if a.startswith('dopełniacz'):
                    # print(a)
                    try: dopelniaczLP = a.replace('dopełniacz">dopełniacz</a></td><td>', '').split('</td><td>')[0]
                    except: dopelniaczLP = ''
                    try: dopelniaczLM = a.replace('dopełniacz">dopełniacz</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                    except: dopelniaczLM = ''
                    # print(dopelniaczLP, dopelniaczLM)
                    if len(dopelniaczLP) > 0 and len(dopelniaczLP) < len(word) + 4:
                        expDLP = 'meaning:' + dopelniaczLP + '|#cz.mowy#rzeczownik odmiana dopełniacz;'
                        exp.append(expDLP)
                    if len(dopelniaczLM) > 0 and len(dopelniaczLM) < len(word) + 4:
                        expDLM = 'meaning:' + dopelniaczLM + '|#cz.mowy#rzeczownik odmiana dopełniacz;'
                        exp.append(expDLM)
                if a.startswith('celownik'):
                    # print(a)
                    try: celownikLP = a.replace('celownik">celownik</a></td><td>', '').split('</td><td>')[0]
                    except: celownikLP = ''
                    try: celownikLM = a.replace('celownik">celownik</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                    except: celownikLM = ''
                    # print(celownikLP, celownikLM)
                    if len(celownikLP) > 0 and len(celownikLP) < len(word) + 4:
                        expcLP = 'meaning:' + celownikLP + '|#cz.mowy#rzeczownik odmiana celownik;'
                        exp.append(expcLP)
                    if len(celownikLM) > 0 and len(celownikLM) < len(word) + 4:
                        expcLM = 'meaning:' + celownikLM + '|#cz.mowy#rzeczownik odmiana celownik;'
                        exp.append(expcLM)
                if a.startswith('biernik'):
                    # print(a)
                    try: biernikLP = a.replace('biernik">biernik</a></td><td>', '').split('</td><td>')[0]
                    except: biernikLP = ''
                    try: biernikLM = a.replace('biernik">biernik</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                    except: biernikLM = ''
                    # print(biernikLP, biernikLM)
                    if len(biernikLP) > 0 and len(biernikLP) < len(word) + 4:
                        expBLP = 'meaning:' + biernikLP + '|#cz.mowy#rzeczownik odmiana biernik;'
                        exp.append(expBLP)
                    if len(biernikLM) > 0 and len(biernikLM) < len(word) + 4:
                        expBLM = 'meaning:' + biernikLM + '|#cz.mowy#rzeczownik odmiana biernik;'
                        exp.append(expBLM)
                if a.startswith('narzędnik'):
                    # print(a)
                    try: narzednikLP = a.replace('narzędnik">narzędnik</a></td><td>', '').split('</td><td>')[0]
                    except: narzednikLP = ''
                    try: narzednikLM = a.replace('narzędnik">narzędnik</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                    except: narzednikLM = ''
                    # print(narzednikLP, narzednikLM)
                    if len(narzednikLP) > 0 and len(narzednikLP) < len(word) + 4:
                        expBLP = 'meaning:' + narzednikLP + '|#cz.mowy#rzeczownik odmiana narzędnik;'
                        exp.append(expBLP)
                    if len(narzednikLM) > 0 and len(narzednikLM) < len(word) + 4:
                        expBLM = 'meaning:' + narzednikLM + '|#cz.mowy#rzeczownik odmiana narzędnik;'
                        exp.append(expBLM)
                if a.startswith('miejscownik'):
                    # print(a)
                    try: miejscownikLP = a.replace('miejscownik">miejscownik</a></td><td>', '').split('</td><td>')[0]
                    except: miejscownikLP = ''
                    try: miejscownikLM = a.replace('miejscownik">miejscownik</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                    except: miejscownikLM = ''
                    # print(miejscownikLP, narzednikLM)
                    if len(miejscownikLP) > 0 and len(miejscownikLP) < len(word) + 4:
                        expBLP = 'meaning:' + miejscownikLP + '|#cz.mowy#rzeczownik odmiana miejscownik;'
                        exp.append(expBLP)
                    if len(miejscownikLM) > 0 and len(miejscownikLM) < len(word) + 4:
                        expBLM = 'meaning:' + miejscownikLM + '|#cz.mowy#rzeczownik odmiana miejscownik;'
                        exp.append(expBLM)
                if a.startswith('wołacz'):
                    # print(a)
                    try: wolaczLP = a.replace('wołacz">wołacz</a></td><td>', '').split('</td><td>')[0]
                    except: wolaczLP = ''
                    try: wolaczLM = a.replace('wołacz">wołacz</a></td><td>', '').split('</td><td>')[1].split('<')[0].replace(' / ', '')
                    except: wolaczLM = ''
                    # print(wolaczLP, wolaczLM)
                    if len(wolaczLP) > 0 and len(wolaczLP) < len(word) + 4:
                        expBLP = 'meaning:' + wolaczLP + '|#cz.mowy#rzeczownik odmiana wołacz;'
                        exp.append(expBLP)
                    if len(wolaczLM) > 0 and len(wolaczLM) < len(word) + 4:
                        expBLM = 'meaning:' + wolaczLM + '|#cz.mowy#rzeczownik odmiana wołacz;'
                        exp.append(expBLM)
            
                    # break
        ind +=1
    # print('sprawdzam wiki ..') 
    return exp

# print(partSpeech('usługa'))
import coffeeBrain as cf
wordsNo = cf.coffeePls(False)[3]
for r, z in wordsNo.items():
    z = str(z)
    if z.startswith('#cz.mowy#rzeczownik'):
        clsSet = set()
        for x in partSpeech(r):
            clsSet.add(x)

        wordsSet = set()
        dictFinal = {}
        for cl in clsSet:
            cl = str(cl)
            clName = cl.split('|')[0].replace('meaning:', '')
            wordsSet.add(clName)
            dictFinal[clName] = ''


        for a in clsSet:
            for b in wordsSet:
                clName = a.split('|')[0].replace('meaning:', '')
                clval = a.split('|')[1]
                if b == clName:
                    dictFinal[b] += clval
                    # print(b, clval)

        import wtf
        for d, i in dictFinal.items():
            answer = f'meaning:{d}|{i}\n'
            wtf.addQuestionAnswer(answer)
            print(answer)
    # print(dictFinal)