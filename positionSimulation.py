def positionVerb(inp):
    inp = str(inp)
    if inp.endswith('eś'):
        inp = inp.replace('eś', 'em')
    elif inp.endswith('aś'):
        inp = inp.replace('aś', 'am')
    elif inp.endswith(f'asz'):
        inp = inp.replace(f'asz', f'am')
    elif inp.endswith(f'jesz'):
        inp = inp.replace(f'jesz', f'ję')
    elif inp.endswith(f'ziesz'):
        inp = inp.replace(f'ziesz', f'ę')
    elif inp.endswith(f'wiesz'):
        inp = inp.replace(f'wiesz', f'wiem')
    elif inp.endswith(f'miesz'):
        inp = inp.replace(f'miesz', f'mię')
    elif inp.endswith(f'iesz'):
        inp = inp.replace(f'iesz', f'ę').replace('ź', 'z').replace('ż', 'z')
    elif inp.endswith(f'ażesz'):
        inp = inp.replace(f'ażesz', f'ażę')
    elif inp.endswith(f'ożesz'):
        inp = inp.replace(f'ożesz', f'ogę')
    elif inp.endswith(f'cesz'):
        inp = inp.replace(f'cesz', f'cę')
    elif inp.endswith(f'esz'):
        inp = inp.replace(f'esz', f'em')
    elif inp.endswith(f'lisz'):
        inp = inp.replace(f'lisz', f'lę')
    elif inp.endswith(f'dzisz'):
        inp = inp.replace(f'dzisz', f'dzę')
    elif inp.endswith(f'zisz'):
        inp = inp.replace(f'zisz', f'żę')
    elif inp.endswith(f'sisz'):
        inp = inp.replace(f'sisz', f'szę')
    elif inp.endswith(f'isz'):
        inp = inp.replace(f'isz', f'ię')
    elif inp.endswith(f'czysz'):
        inp = inp.replace(f'czysz', f'czę')
    elif inp.endswith(f'szysz'):
        inp = inp.replace(f'szysz', f'szę')
    elif inp.endswith(f'żysz'):
        inp = inp.replace(f'żysz', f'żę')
    elif inp.endswith(f'rzysz'):
        inp = inp.replace(f'rzysz', f'rzę')
    elif inp.endswith(f'byś'):
        inp = inp.replace(f'byś', f'bym')
    return inp

def positionUnVerb(inp):
    inp = str(inp)
    if inp.endswith('rzam'):
        inp = inp.replace('rzam', 'rzasz')
    elif inp == 'mam':
        inp = inp.replace('mam', 'masz')
    elif inp.endswith('am'):
        inp = inp.replace('am', 'asz')
    elif inp.endswith('uję'):
        inp = inp.replace('uję', 'ujesz')
    elif inp.endswith('uję'):
        inp = inp.replace('uję', 'ujesz')
    elif inp.endswith('będę'):
        inp = inp.replace('będę', 'będziesz')
    elif inp.endswith('gę'):
        inp = inp.replace('gę', 'żesz')
    elif inp.endswith('żę'):
        inp = inp.replace('żę', 'żysz')
    elif inp.endswith('czę'):
        inp = inp.replace('czę', 'czysz')
    elif inp.endswith('oszę'):
        inp = inp.replace('oszę', 'osisz')
    elif inp.endswith('szę'):
        inp = inp.replace('szę', 'szysz')
    elif inp.endswith('chcę'):
        inp = inp.replace('chcę', 'chcesz')
    elif inp.endswith('cę'):
        inp = inp.replace('cę', 'cisz')
    elif inp.endswith('wiem'):
        inp = inp.replace('wiem', 'wiesz')
    elif inp.endswith('em'):
        inp = inp.replace('em', 'eś')
    elif inp.endswith('ię'):
        inp = inp.replace('ię', 'isz')
    elif inp.endswith('lę'):
        inp = inp.replace('lę', 'lisz')
    return inp

def positionVerbInfinitive(inp):
    inp = str(inp)
    temp = 'mogę '
    if inp.endswith('aj'):
        inp = temp + inp.replace('aj', 'ać')
    elif inp.endswith('ap'):
        inp = temp + inp.replace('ap', 'apić')
    elif inp.endswith('adź'):
        inp = temp + inp.replace('adź', 'adzić')
    elif inp.endswith('ądź'):
        inp = temp + inp.replace('ądź', 'adać')
    elif inp.endswith('el'):
        inp = temp + inp.replace('el', 'elieć')
    elif inp.endswith('edz'):
        inp = temp + inp.replace('edz', 'edzieć')
    elif inp.endswith('mij'):
        inp = temp + inp.replace('mij', 'mować')
    elif inp.endswith('szcz'):
        inp = temp + inp.replace('szcz', 'szczyć')
    elif inp.endswith('weź'):
        inp = temp + inp.replace('weź', 'wźąć')
    elif inp.endswith('lcz'):
        inp = temp + inp.replace('lcz', 'lczeć')
    elif inp.endswith('ów'):
        inp = temp + inp.replace('ów', 'ówić')
    elif inp.endswith('ucz'):
        inp = temp + inp.replace('ucz', 'uczyć')
    elif inp.endswith('ieź'):
        inp = temp + inp.replace('ieź', 'osić')
    elif inp.endswith('ieś'):
        inp = temp + inp.replace('ieś', 'ozić')
    elif inp.endswith('aż'):
        inp = temp + inp.replace('aż', 'azać')
    elif inp.endswith('erz'):
        inp = temp + inp.replace('erz', 'erać')
    elif inp.endswith(f'ób'):
        inp = temp + inp.replace(f'ób', f'obić')
    elif inp.endswith(f'okuj'):
        inp = temp + inp.replace(f'okuj', f'okoić')
    elif inp.endswith(f'uj'):
        inp = temp + inp.replace(f'uj', f'ować')
    elif inp.endswith(f'iń'):
        inp = temp + inp.replace(f'iń', f'ijać')
    elif inp.endswith(f'nij'):
        inp = temp + inp.replace(f'nij', f'nąć')
    elif inp.endswith(f'ńcz'):
        inp = temp + inp.replace(f'ńcz', f'ńczyć')
    elif inp.endswith(f'ącz'):
        inp = temp + inp.replace(f'ącz', f'ączyć')
    elif inp.endswith(f'ań'):
        inp = temp + inp.replace(f'ań', f'ać')
    elif inp.endswith(f'um'):
        inp = temp + inp.replace(f'um', f'umieć')
    elif inp.endswith(f'om'):
        inp = temp + inp.replace(f'om', f'omić')
    elif inp.endswith(f'yśl'):
        inp = temp + inp.replace(f'yśl', f'yśleć')
    elif inp.endswith(f'nów'):
        inp = temp + inp.replace(f'nów', f'nowić')
    
    return inp
'szcz szczyć, lcz lczeć, weź wźąć, w ieź w ozić, n ieś n osić, '

def positionPronoun(inp):
    inp = str(inp)
    if inp == 'ci': inp = 'mi'
    elif inp == 'mnie': inp = 'ciebie'
    elif inp == 'ciebie': inp = 'mnie'
    elif inp == 'tobie': inp = 'mnie'
    elif inp == 'twój': inp = 'mój'
    elif inp == 'mi': inp = 'Ci'
    elif inp == 'twoim': inp = 'moim'
    elif inp == 'moim': inp = 'twoim'
    elif inp == 'mój': inp = 'twój'
    elif inp == 'moje': inp = 'twoje'
    elif inp == 'twoje': inp = 'moje'
    elif inp == 'cię': inp = 'mnie'
    elif inp == 'ty': inp = 'ja'
    elif inp == 'ja': inp = 'ty'
    elif inp == 'mną': inp = 'tobą'
    return inp



'''
str(k).endswith('aj') or str(k).endswith('adź') or str(k).endswith('ądź') or str(k).endswith('edz') or str(k).endswith('eź')
'''