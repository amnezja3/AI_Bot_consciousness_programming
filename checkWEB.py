def checkWeb(pharse):
    from GSEARCH import search
    from requests import get
    u_MAIN_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/61.0.3163.100 Safari/537.36'}
    resultFull = search(pharse, num_results=5, lang="pl")
    export = set()
    for url_i in resultFull:
        try:
            res = get(url_i, headers=u_MAIN_agent, proxies=None)    
            res.raise_for_status()
            i = res.text
        except: continue
        headON = i.count('<head>')
        headOFF = i.count('</head>')
        enCODING = i.count('utf')
        if headON == 1 and headOFF == 1 and enCODING > 0:
            try: ix = i.split('<head>')[1].split('</head>')[0]
            except: continue            
            iy = ix.split('<meta name="')
            if len(iy) > 1:
                for iz in iy:
                    iiz = iz.split('\n')
                    for iw in iiz:
                        iw = str(iw).strip()
                        if not iw.startswith('<') and iw.endswith('/>'):
                            countPharse = ix.count(pharse)
                            if countPharse > 0:
                                iiw = iw.replace('"/>', '').split('"')
                                for iaw in iiw:
                                    countDOT = iaw.count('.')

                                    countIQU = iaw.count('=')
                                    countHTTP = iaw.count('http')
                                    countZL = iaw.count('zł')
                                    countPL = iaw.count('.pl')
                                    countCOM = iaw.count('.com')
                                    countORG = iaw.count('.org')
                                    countWordPress = iaw.count('WordPress')
                                    countQUOT = iaw.count('&quot;')                               

                                    MAX_COUNTER = countORG + countCOM + countIQU + countHTTP + countZL + countPL + countWordPress + countQUOT
                                    if countDOT > 0 and len(iaw) > 70 and MAX_COUNTER == 0:
                                        export.add(iaw)
    exp = []
    for e in export:
        exp.append(e)
    return exp

# print(checkWeb('statek kosmiczny'))