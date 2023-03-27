import speech_recognition as sr
import pyttsx3 as tts 
from time import sleep
from os import system

def microMic():
    r = sr.Recognizer()
    engine = tts.init()
    engine.setProperty('rate', 125)

    def getText():
        print('Nasłuchiwanie rozpocznie się za 3 sec..')
        with sr.Microphone() as source:
            sleep(1)
            try:
                system('color 40')            
                print('Nasłuchiwanie..')            
                audio = r.listen(source)
                text = r.recognize_google(audio, language='pl-PL') 
                print(f'Rozpoznano: {text}')                
                if text != "":
                    return text
                return 0
            except:
                return 0


    txt = getText()
    # print(txt)
    if not txt == 0:
        # print(txt)
        exp = [True, txt.lower()]
        system('color 0D')
        # print(exp)
        return exp
    else:
        exp = [False, False]
        system('color 0D')
        # print(exp)
        return exp


    
