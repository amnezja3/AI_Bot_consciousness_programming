def pronounAct(senten, OR, PO, ZAS):
    senten = str(senten)
    OR = str(OR)
    PO = str(PO)
    OK = str(ZAS)
    list_OR = OR.split(' ')
    list_PO = PO.split(' ')
    list_OK = ZAS.split(' ')
    # print(senten)
    pack = {}
    co = 1
    new_senten = ''
    for sn in senten.split(' '):
        for z in list_OK:
            if z == sn:
                z = sn.replace(f'{sn}', f'OK_{co}')
                new_senten += f' {z}  '
                pack[f'OK_{co}'] = f'{sn}'
                co += 1
                break
        new_senten += f'{sn} '
    for z in list_OK:
        new_senten = new_senten.replace(z, '').strip()
    senten = new_senten
    co = 1
    new_senten = ''
    for sn in senten.split(' '):
        for o in list_OR:
            if o == sn:
                o = sn.replace(f'{sn}', f'OR_{co}')
                new_senten += f'{o} '
                pack[f'OR_{co}'] = f'{sn}'
                co += 1
                break
        new_senten += f'{sn} '
    for o in list_OR:
        new_senten = new_senten.replace(o, '').strip()
    senten = new_senten
    co = 1
    new_senten = ''
    for sn in senten.split(' '):
        for p in list_PO:
            if p == sn:
                p = sn.replace(f'{sn}', f'PO_{co}')
                new_senten += f'{p} '
                pack[f'PO_{co}'] = f'{sn}'
                co += 1
                break
        new_senten += f'{sn} '
    for p in list_PO:
        new_senten = new_senten.replace(p, '').strip()
    senten = new_senten
    senList = senten.split(' ')
    co = 1
    sent_zam = []
    for s in senList:
        try: int(s[len(s) - 1])
        except: continue
        if s.endswith(str(co)):
            sent_zam.append(s)
        else: 
            sent_zam.append('&%!')
            sent_zam.append(s)
            co += 1
    finishSent = ''
    for sz in sent_zam:
        if sz != '|':
            try: finishSent += pack[sz] + ' '
            except KeyError: finishSent += sz + ' '
        else:
            finishSent += sz + ' '
    # print()
    # print(senten)
    # print(pack)
    # print(sent_zam)
    # print(finishSent)

    return [finishSent.split(' &%! ')]
if __name__ == "__main__":
    export = pronounAct(
        'czarny kot siedzi na wysokim piecu w kuchni i mruczy w głos', 
        'siedzi mruczy', 
        'kot piecu kuchni głos', 
        'na w w'
        )
    print(export)