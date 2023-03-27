import wtf

def beganTalk(sub, quest):
    pass



userName = 'anonymous'
while True:
    # print(userName)
    inputText = input('co tam? >>> ')
    if inputText == 'hej':
        inputName = input('kto tam? >>> ')
        if inputName != '' and inputName != userName:
            userName = inputName
            questA = input('w czym mogę Ci pomóc ' + userName + '? >>> ')
            recognition = wtf.recognize(questA)
            print(recognition)
        