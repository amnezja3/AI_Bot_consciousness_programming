import percNet as P
from time import sleep

def levels(
            convertInput, 
            memoryLoops_D = 12, 
            memoryLoops_H = 12,
            memoryLoops_O = 12,
            memoryName = '',
            mem = 'draw', 
            data_D = 'all',):
    
    if data_D == 'first': high_L = memoryLoops_D
    if data_D == 'deep': high_L = memoryLoops_D + memoryLoops_H
    if data_D == 'all': high_L = memoryLoops_D + memoryLoops_H + memoryLoops_O
    
    # Memory    
    dictWeights = {}
    for m in range(high_L):
        dictWeights[f'weights_D_0{m}'] = P.getMemeory(f'memory_{memoryName}_{mem}_0{m}.csv')[0]
        dictWeights[f'g_0_Par_D_0{m}'] = P.getMemeory(f'memory_{memoryName}_{mem}_0{m}.csv')[1]
    # print(mem)
    # print(f'dictWeights {data_D}')
    # print(dictWeights)
    # sleep(5)




    # LV 0     
    dictData_D = {}
    for m in range(memoryLoops_D):  
        if P.perceptronCalc(
                            convertInput, 
                            dictWeights[f'weights_D_0{m}']
                            ) + dictWeights[f'g_0_Par_D_0{m}'] > 0:
            
            dictData_D[f'calcPer_MD_0{m}'] = 1
        else:
            dictData_D[f'calcPer_MD_0{m}'] = 0
    # print(mem)
    # print('dictData_D')
    # print(dictData_D)
    # sleep(5)




    dictDeepData = {}  
    for d in range(memoryLoops_H):
        dictDeepData[f'deep0{d}'] = [e for e in dictData_D.values()]
        # print(dictDeepData[f'deep0{d}'])
    # print(mem)
    # print('dictDeepData')
    # print(dictDeepData)
    # sleep(5)





    # LV 1
    if data_D == 'deep' or data_D == 'all':
        dictData_MD = {}
        counter = 0
        for m in range(memoryLoops_D, memoryLoops_D + memoryLoops_H, 1):
            # print(dictDeepData[f'deep0{counter}'])
            if P.perceptronCalc(
                            dictDeepData[f'deep0{counter}'], 
                            dictWeights[f'weights_D_0{m}']
                            ) + dictWeights[f'g_0_Par_D_0{m}'] > 0:
                dictData_MD[f'deep_MD_0{counter}'] = 1
            else:
                dictData_MD[f'deep_MD_0{counter}'] = 0    
            # print(dictData_MD[f'deep_MD_0{counter}'])
            counter += 1
            
        # print(mem)
        # print('dictDeepData')
        # print(dictDeepData)
        # sleep(5)
        dictOutData = {}  
        for d in range(memoryLoops_H):
            dictOutData[f'output_0{d}'] = [e for e in dictData_MD.values()]
            # print(dictOutData[f'output_0{d}'])




    # LV 2
    if data_D == 'all':
        dictData_OUT = {}
        counter = 0
        for m in range(memoryLoops_D + memoryLoops_H, memoryLoops_D + memoryLoops_H + memoryLoops_O, 1):
            if P.perceptronCalc(
                            dictOutData[f'output_0{counter}'], 
                            dictWeights[f'weights_D_0{m}']
                            ) + dictWeights[f'g_0_Par_D_0{m}'] > 0:
                dictData_OUT[f'deep_OUT_0{counter}'] = 1
            else:
                dictData_OUT[f'deep_OUT_0{counter}'] = 0    
            counter += 1
        # print(mem)
        # print('dictData_OUT')
        # print(dictData_OUT)
        # sleep(5)




    if data_D == 'first':
        data_F = [dictData_D[f'calcPer_MD_0{c}'] for c in range(len(dictData_D.values()))]
        # print('first')
        # print(data_F)
        # sleep(1)
        return data_F
    
    if data_D == 'deep':
        deep_MD = [dictData_MD[f'deep_MD_0{c}'] for c in range(len(dictData_MD.values()))]
        # print('deep')
        # print(deep_MD)
        # sleep(5)
        return deep_MD
    
    if data_D == 'all':
        outputReturn = [dictData_OUT[f'deep_OUT_0{c}'] for c in range(len(dictData_OUT.values()))]
        calc = 0
        for x in outputReturn:
            if x > 0: calc += 1
        exp = [calc, calc / memoryLoops_D]
        # print('exp')
        # print(exp)
        # sleep(5)
        return exp 
    
    
# convertInput = ['name', 154, -580, -1580, 111, 51, 711, -12, -2887, 2125, 315, 3547, 13, 'True']
# print(levels(convertInput[1:], 12, 'home', 'first'))