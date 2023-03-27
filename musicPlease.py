#  po uruchomieniu beda odtwarzane 3 mp3 losowo
import random
import os
import playsound


dd = os.listdir('./mp3')
cc = []
for d in dd:
    if d.endswith('mp3'):
        cc.append(d)

while True:
    r = random.choice(cc)
    w = playsound.playsound(f'./mp3/{r}', True) 