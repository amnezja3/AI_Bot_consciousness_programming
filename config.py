def brain(witch):
    witch = str(witch)
    if witch == 'brain': 
        MAIN_FILE_BRAIN = 'brain.neural'
        return MAIN_FILE_BRAIN
    if witch == 'wiki': 
        TMP_FILE_WIKI = 'filter_wiki.recognizer'
        return TMP_FILE_WIKI


def clearCharacters(quest):
    quest = str(quest)
    quest = quest.replace('?', '').replace('np.', '').replace('..', '').replace('...', '')\
        .replace(',', '').replace('!', '').replace('$', '').replace('\r', '').replace('\t', '')\
            .replace('\n', '').replace('-', ' ').replace('+', ' ').replace('*', ' ').replace('/', ' ')\
                .replace('#', '').replace('@', '').replace(':', ' ').replace(';', '').replace("'", '')\
                    .replace("(", '').replace(")", '').replace("[", '').replace("]", '').replace("{", '')\
                        .replace("}", '').replace("«", '').replace("»", '').replace('\xe0', '').replace('\xc5', '')\
                            .replace('\u03bc', '').replace('\u03bc', '').replace('\xa3', '').replace('•', '').replace('⊕', '2').lower()
    return quest

def clearCharactersLOW(quest):
    quest = str(quest)
    quest = quest.replace(':', '').replace('m.', 'm').replace('b.', 'b').replace('c.', 'c').replace('l.', 'l').replace('g.', 'g')\
        .replace('e.', 'e').replace('k.', 'k').replace('n.', 'k').replace('s.', 'k').replace('l.', 'l').replace('np.', '')\
            .replace('r.', 'r').replace('w.', 'w').replace('lat.', '').replace('ang.', '').replace('wł.', '').replace('..', '')\
                .replace('...', '').replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace('\r', '')\
                    .replace('\t', '').replace('\n', '').replace('\xe0', '').replace('\xc5', '').replace('\u03bc', '')\
                        .replace('\u03bc', '').replace('\xa3', '').lower()
    return quest

def botAdmin():
    return 'Nadawcagods_heretic'

def botSL_Admin():
    return 'seembaixador'

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
            userData[int(aa[0].replace('task_id:', ''))] = [[aa[1]], [b for b in aa[2:]]]


        if a.startswith('user_name:'):
            un = a.split(':')[1]
            userData['USER_NAME'] = un

    return userData
