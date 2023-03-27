import random, os
from time import sleep

def perceptronCalc(x_input, w_weights):
    weighted_sum = 0
    for x,w in zip(x_input, w_weights):
        weighted_sum += x * w
        # print(weighted_sum)
    return weighted_sum


def perceptron(trData, inputs = [[None], None], maxLoops = 1000000):    
    export = None        
    loops = 0
    while True:
        isRing = 1
        isPen = -1
        speed = 0.02

#################################################################################################             
######################################## FIRST GENERATION ########################################    
        try: 
            weights = inputs[0]
            g_0_Par = inputs[1]
        except IndexError:
            i_weights = [[None], None]
            i_g_0_Par = [[None], None]
            weights = i_weights[0]
            g_0_Par = i_g_0_Par[1]            
        
        
        if inputs[0][0] == None and inputs[1] == None:
            losNegative = [1, -1]
            losSmall = [0.001, 0.01, 0.1, 1, 2]
            weights = []
            for l in range(len(trData[0]) - 1):
                weights.append(
                    random.choice(losNegative) * random.randrange(-5, 5) * (random.randrange(0, 255) * random.choice(losSmall) + l)
                    )            
            # print(weights)            
            g_0_Par = random.randrange(1, 18) * random.choice(losSmall)
        else:
            weights = inputs[0]
            g_0_Par = inputs[1]
            
        li = 0
        wrongRing = []
        wrongPen = []
        for a in trData:
            calcPer = perceptronCalc(a, weights) + g_0_Par
            if calcPer > 0: action = 'True'
            else: action = 'False'            
            if action == a[len(a) - 1]: res = 'Good'        
            else: 
                res = 'Wrong'
                if a[len(a) - 1] == 'True': wrongRing.append(li)
                if a[len(a) - 1] == 'False': wrongPen.append(li)

            result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
            # print(result)
            # sleep(0.17)
            li += 1
        # os.system('color E0')

        wRanRing = None
        wRanPen = None
        if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
        elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
        else: 
            export = [weights , g_0_Par]
            return export
        
#################################################################################################             
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else:
            recognition = False

        if recognition:
            w = 0
            w_1_L = []
            for b in weights:
                g_1_X = b + newDataTraining[w] * recognition * speed
                w_1_L.append(g_1_X)
                w += 1
                  
            g_1_Par = g_0_Par + (recognition * speed)
            
            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_1_L) + g_1_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)                
                li += 1
            # os.system('color 30')

            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_1_L , g_1_Par]
                return export

#################################################################################################             
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_2_L = []
            for b in weights:
                g_2_X = b + newDataTraining[w] * recognition * speed
                w_2_L.append(g_2_X)
                w += 1
           
            g_2_Par = g_1_Par + (recognition * speed)
            
            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_2_L) + g_2_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 50')
            
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_2_L, g_2_Par]
                return export

#################################################################################################             
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_3_L = []
            for b in weights:
                g_3_X = b + newDataTraining[w] * recognition * speed
                w_3_L.append(g_3_X)
                w += 1
                
            g_3_Par = g_2_Par + (recognition * speed)

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_3_L) + g_3_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 60')
            
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_3_L, g_3_Par]
                return export
            
#################################################################################################           
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_4_L = []
            for b in weights:
                g_4_X = b + newDataTraining[w] * recognition * speed
                w_4_L.append(g_4_X)
                w += 1
            g_4_Par = g_3_Par + (recognition * speed)

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_4_L) + g_4_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_4_L, g_4_Par]        
                return export

#################################################################################################             
######################################## NEXT GENERATION ########################################           
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_5_L = []
            for b in weights:
                g_5_X = b + newDataTraining[w] * recognition * speed
                w_5_L.append(g_5_X)
                w += 1
            g_5_Par = g_4_Par + (recognition * speed)

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_5_L) + g_5_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_5_L, g_5_Par]        
                return export        
            
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_6_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_6_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_6_L.append(g_6_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_6_Par = g_5_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_6_L) + g_6_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_6_L, g_6_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_7_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_7_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_7_L.append(g_7_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_7_Par = g_6_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_7_L) + g_7_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_7_L, g_7_Par]   # Tu zmienić w_?_L i g_?_Par
                return export      
            
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_8_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_8_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_8_L.append(g_8_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_8_Par = g_7_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_8_L) + g_8_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_8_L, g_8_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
            
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_9_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_9_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_9_L.append(g_9_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_9_Par = g_8_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_9_L) + g_9_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_9_L, g_9_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
            
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_10_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_10_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_10_L.append(g_10_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_10_Par = g_9_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_10_L) + g_10_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_10_L, g_10_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
            
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_11_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_11_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_11_L.append(g_11_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_11_Par = g_10_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_11_L) + g_11_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_11_L, g_11_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
                     
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_12_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_12_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_12_L.append(g_12_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_12_Par = g_11_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_12_L) + g_12_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_12_L, g_12_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
            
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_13_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_13_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_13_L.append(g_13_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_13_Par = g_12_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_13_L) + g_13_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_13_L, g_13_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
                
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_14_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_14_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_14_L.append(g_14_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_14_Par = g_13_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_14_L) + g_14_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_14_L, g_14_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
            
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_15_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_15_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_15_L.append(g_15_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_15_Par = g_14_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_15_L) + g_15_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_15_L, g_15_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
               
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_16_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_16_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_16_L.append(g_16_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_16_Par = g_15_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_16_L) + g_16_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_16_L, g_16_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
             
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_17_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_17_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_17_L.append(g_17_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_17_Par = g_16_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_17_L) + g_17_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_17_L, g_17_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
             
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_18_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_18_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_18_L.append(g_18_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_18_Par = g_17_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_18_L) + g_18_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_18_L, g_18_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
             
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_19_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_19_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_19_L.append(g_19_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_19_Par = g_18_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_19_L) + g_19_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_19_L, g_19_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
             
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_20_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_20_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_20_L.append(g_20_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_20_Par = g_19_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_20_L) + g_20_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_20_L, g_20_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
             
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_21_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_21_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_21_L.append(g_21_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_21_Par = g_20_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_21_L) + g_21_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_21_L, g_21_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
             
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_22_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_22_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_22_L.append(g_22_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_22_Par = g_21_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_22_L) + g_22_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_22_L, g_22_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
             
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_23_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_23_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_23_L.append(g_23_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_23_Par = g_22_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_23_L) + g_23_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_23_L, g_23_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
             
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_24_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_24_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_24_L.append(g_24_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_24_Par = g_23_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_24_L) + g_24_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_24_L, g_24_Par]   # Tu zmienić w_?_L i g_?_Par
                return export
             
#################################################################################################            
######################################## NEXT GENERATION ########################################
        if wRanRing != None:
            newDataTraining = trData[wRanRing]
            recognition = isRing
        elif wRanPen != None:
            newDataTraining = trData[wRanPen]
            recognition = isPen
        else: recognition = False

        if recognition:
            w = 0
            w_25_L = [] # Tu zmienić w_?_L
            for b in weights:
                g_25_X = b + newDataTraining[w] * recognition * speed # Tu zmienić G_?_X
                w_25_L.append(g_25_X) # Tu zmienić w_?_L i g_?_X
                w += 1
            g_25_Par = g_24_Par + (recognition * speed)  # Tu zmienić g_?_Par = g_ (? - 1) _Par

            li = 0
            wrongRing = []
            wrongPen = []
            for a in trData:
                calcPer = perceptronCalc(a, w_25_L) + g_25_Par  # Tu zmienić w_?_L i g_?_Par
                if calcPer > 0: action = 'True'
                else: action = 'False'
                
                if action == a[len(a) - 1]: res = 'Good'        
                else:
                    res = 'Wrong'
                    if a[len(a) - 1] == 'True': wrongRing.append(li)
                    if a[len(a) - 1] == 'False': wrongPen.append(li)
                    
                result = str(li) + '! for:' + str(calcPer) + ' as: ' + str(action) + ' should be: ' + str(a[len(a) - 1]) + ' is ' + res
                # print(result)
                # sleep(0.17)
                li += 1
            # os.system('color 70')
             
            wRanRing = None
            wRanPen = None
            if len(wrongRing) > 0: wRanRing = random.choice(wrongRing)
            elif len(wrongPen) > 0: wRanPen = random.choice(wrongPen)
            else:
                export = [w_25_L, g_25_Par]   # Tu zmienić w_?_L i g_?_Par
                return export

######################################## END OF FUNCTION EXIT OR LOOP AGAIN ########################################
        loops += 1
        examples = len(trData)
        if export != None or loops > maxLoops:
            export = [[None], None] # [w_25_L, g_25_Par]   # Tu zmienić w_?_L i g_?_Par
            print(f'-Export pack : {examples}')
            return export
            # os.system('color 02')
            # break
        else:     
            inputs = [w_25_L, g_25_Par] # [[None], None]      
            # os.system('color 90')            
            # print(f'-Export pack : {examples} --Wrong Trues: {len(wrongRing)}----Wrong Falses: {len(wrongPen)}------ loop: {loops}')



if __name__ == '__main__':
   pass